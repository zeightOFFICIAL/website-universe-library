import * as THREE from "three";
import { OrbitControls } from "three/addons/controls/OrbitControls.js";

/*
 * Galaxy view of the main page.
 *
 * Scene units are kilo-light-years (1 unit = 1000 ly). The galactic centre is the
 * origin, the disk lies in the XZ plane and +Y points to the north galactic pole.
 * The Sun sits on +Z; galactic longitude 0 points from the Sun to the centre (-Z)
 * and longitude 90 (the direction of galactic rotation) points to -X.
 *
 * The star field is sampled from the backdrop artwork: each star takes its position
 * and colour from a pixel, so the 3D galaxy and the backdrop show the same arms in
 * the same colours. The backdrop itself is drawn as a stack of slices, which gives
 * the disk thickness so it still reads when seen edge-on.
 *
 * Two levels of detail:
 *   galaxy - the whole Milky Way, arm names, landmarks, one marker for the Sun
 *   local  - camera close to the Sun; real systems at their true directions with
 *            log-scaled distances, so a 4 ly and a 430 ly system both stay readable
 */

const DATA = JSON.parse(document.getElementById("GALAXY_DATA").textContent);
const SUN = new THREE.Vector3(0, (DATA.sunHeight || 0) / 1000, DATA.sunDistance / 1000);

const GALAXY_RADIUS = 50;
const ARM_PITCH = THREE.MathUtils.degToRad(12);
const ARM_K = Math.tan(ARM_PITCH);

// radius (kly) at which each arm crosses the Sun-centre line; the four crossings are
// spaced by exp(2*pi*k/4), which puts Sagittarius inside the Sun and Perseus outside
const ARMS = [
    { name: "Norma Arm", crossing: 10.8, label: 13, outerLabel: "Outer Arm" },
    { name: "Scutum–Centaurus Arm", crossing: 15.0, label: 21 },
    { name: "Sagittarius Arm", crossing: 21.0, label: 16 },
    { name: "Perseus Arm", crossing: 29.3, label: 36 },
];
const ORION_SPUR = { name: "Orion Spur", crossing: 26.3, rMin: 23, rMax: 30.5 };

/*
 * The backdrop is R. Hurt's face-on artist's concept (NASA/JPL-Caltech, public
 * domain). Its bar sits at 47 degrees in image coordinates; rotating the plane by
 * 16 degrees lines that up with the bar direction we use for the arm skeleton. It
 * is an artist's impression, not a survey, so treat it as a backdrop and not as
 * ground truth.
 */
const BACKDROP = {
    rotation: THREE.MathUtils.degToRad(16),
    size: GALAXY_RADIUS * 2.3,
    opacity: 0.62,
    slices: 11,
    halfThickness: 1.5,
    sampleSize: 384,
    stars: 300000,
    gas: 7000,
    knots: 1200,
};

const LOCAL_LOG_SCALE = 0.5;
const LOCAL_RINGS_LY = [10, 100, 1000];
const LOCAL_ENTER = 9;
const LOCAL_FULL = 5;
const DEEP_SKY_LABEL_DISTANCE = 45;

const OVERVIEW = { target: new THREE.Vector3(0, 0, 0), distance: 85, polar: 0.9, azimuth: 0.45 };

const DEEP_SKY_STYLE = {
    nebula: { color: "#ff6b8a", size: 12, label: "Nebula" },
    remnant: { color: "#ff9d6b", size: 11, label: "Supernova remnant" },
    planetary: { color: "#7de2c3", size: 9, label: "Planetary nebula" },
    open: { color: "#bcd8ff", size: 10, label: "Open cluster" },
    globular: { color: "#ffd9a0", size: 12, label: "Globular cluster" },
    structure: { color: "#9ecbff", size: 10, label: "Structure" },
};

/* ---------- helpers ---------- */

function mulberry32(seed) {
    return function () {
        seed |= 0;
        seed = (seed + 0x6d2b79f5) | 0;
        let t = Math.imul(seed ^ (seed >>> 15), 1 | seed);
        t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
        return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
}

const rand = mulberry32(19650701);

function gauss() {
    let u = 0;
    while (u === 0) u = rand();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * rand());
}

function armPhase(crossing) {
    return Math.PI / 2 + Math.log(crossing) / ARM_K;
}

function armAngle(phase, r) {
    return phase - Math.log(r) / ARM_K;
}

function armPoint(phase, r) {
    const theta = armAngle(phase, r);
    return new THREE.Vector3(r * Math.cos(theta), 0, r * Math.sin(theta));
}

function directionFromSun(l, b) {
    const lr = THREE.MathUtils.degToRad(l);
    const br = THREE.MathUtils.degToRad(b);
    return new THREE.Vector3(-Math.sin(lr) * Math.cos(br), Math.sin(br), -Math.cos(lr) * Math.cos(br));
}

// true position, in kly, of something d light-years away in direction (l, b)
function truePosition(l, b, d) {
    return directionFromSun(l, b).multiplyScalar(d / 1000).add(SUN);
}

// local view: true direction, log-scaled distance, so everything nearby stays readable
function localRadius(ly) {
    return LOCAL_LOG_SCALE * Math.log10(1 + ly);
}

function localPosition(placement) {
    return directionFromSun(placement.l, placement.b).multiplyScalar(localRadius(placement.d)).add(SUN);
}

function formatLy(ly) {
    if (ly >= 1e6) return `${(ly / 1e6).toLocaleString("en-US", { maximumFractionDigits: 2 })} million ly`;
    if (ly >= 1000) return `${Math.round(ly).toLocaleString("en-US")} ly`;
    return `${ly.toLocaleString("en-US", { maximumFractionDigits: 2 })} ly`;
}

function smoothstep(edge0, edge1, x) {
    const t = THREE.MathUtils.clamp((x - edge0) / (edge1 - edge0), 0, 1);
    return t * t * (3 - 2 * t);
}

/* ---------- particle layers ---------- */

class Layer {
    constructor(capacity) {
        this.positions = new Float32Array(capacity * 3);
        this.colors = new Float32Array(capacity * 3);
        this.sizes = new Float32Array(capacity);
        this.alphas = new Float32Array(capacity);
        this.count = 0;
        this.capacity = capacity;
    }

    add(p, color, size, alpha) {
        if (this.count >= this.capacity) return;
        const i = this.count++;
        this.positions.set([p.x, p.y, p.z], i * 3);
        this.colors.set([color.r, color.g, color.b], i * 3);
        this.sizes[i] = size;
        this.alphas[i] = alpha;
    }

    geometry() {
        const g = new THREE.BufferGeometry();
        g.setAttribute("position", new THREE.BufferAttribute(this.positions.subarray(0, this.count * 3), 3));
        g.setAttribute("color", new THREE.BufferAttribute(this.colors.subarray(0, this.count * 3), 3));
        g.setAttribute("aSize", new THREE.BufferAttribute(this.sizes.subarray(0, this.count), 1));
        g.setAttribute("aAlpha", new THREE.BufferAttribute(this.alphas.subarray(0, this.count), 1));
        return g;
    }
}

const VERTEX_SHADER = /* glsl */ `
    attribute float aSize;
    attribute float aAlpha;
    uniform float uScale;
    uniform float uMaxSize;
    uniform float uNearFade;
    uniform float uAttenuate;
    varying vec3 vColor;
    varying float vAlpha;
    void main() {
        vec4 mv = modelViewMatrix * vec4(position, 1.0);
        float dist = -mv.z;
        float size = mix(aSize, aSize * uScale / dist, uAttenuate);
        float alpha = aAlpha;
        // keep sub-pixel points as dim 1px points instead of losing them
        if (size < 1.0) {
            alpha *= size;
            size = 1.0;
        }
        gl_PointSize = min(size, uMaxSize);
        vColor = color;
        vAlpha = alpha * smoothstep(uNearFade * 0.25, uNearFade, dist);
        gl_Position = projectionMatrix * mv;
    }
`;

const FRAGMENT_SHADER = /* glsl */ `
    uniform float uSharpness;
    uniform float uOpacity;
    varying vec3 vColor;
    varying float vAlpha;
    void main() {
        // r2 is 0 at the centre and 1 at the sprite's edge; the window forces zero there
        float r2 = dot(gl_PointCoord - 0.5, gl_PointCoord - 0.5) * 4.0;
        if (r2 >= 1.0) discard;
        float a = exp(-r2 * uSharpness) * (1.0 - r2) * vAlpha * uOpacity;
        if (a < 0.002) discard;
        gl_FragColor = vec4(vColor, a);
    }
`;

function pointsMaterial({ maxSize, nearFade = 0.02, sharpness = 16, attenuate = 1, blending = THREE.AdditiveBlending }) {
    return new THREE.ShaderMaterial({
        uniforms: {
            uScale: { value: 1 },
            uMaxSize: { value: maxSize },
            uNearFade: { value: nearFade },
            uAttenuate: { value: attenuate },
            uSharpness: { value: sharpness },
            uOpacity: { value: 1 },
        },
        vertexShader: VERTEX_SHADER,
        fragmentShader: FRAGMENT_SHADER,
        vertexColors: true,
        transparent: true,
        depthWrite: false,
        blending,
    });
}

function glowSprite(color, size, opacity = 1) {
    const canvas = document.createElement("canvas");
    canvas.width = canvas.height = 256;
    const ctx = canvas.getContext("2d");
    const gradient = ctx.createRadialGradient(128, 128, 0, 128, 128, 128);
    gradient.addColorStop(0, "rgba(255,255,255,1)");
    gradient.addColorStop(0.15, "rgba(255,255,255,.55)");
    gradient.addColorStop(0.45, "rgba(255,255,255,.12)");
    gradient.addColorStop(1, "rgba(255,255,255,0)");
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 0, 256, 256);
    const sprite = new THREE.Sprite(
        new THREE.SpriteMaterial({
            map: new THREE.CanvasTexture(canvas),
            color,
            blending: THREE.AdditiveBlending,
            depthWrite: false,
            transparent: true,
            opacity,
        })
    );
    sprite.scale.setScalar(size);
    return sprite;
}

/* ---------- the backdrop, as a stack of slices ---------- */

// the transform that puts the artwork into the galaxy plane; star sampling uses the
// same matrix, so stars land exactly on the features they were sampled from
const BACKDROP_MATRIX = new THREE.Matrix4().makeRotationFromEuler(
    new THREE.Euler(-Math.PI / 2, 0, BACKDROP.rotation, "XYZ")
);

const BACKDROP_VERTEX = /* glsl */ `
    varying vec2 vUv;
    void main() {
        vUv = uv;
        gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
    }
`;

/*
 * The artwork sits on black and is blended additively, so its background keys out
 * for free - no alpha channel needed. uEdge trims the plane's corners, uOpacity
 * carries the layer toggle and the fades.
 */
const BACKDROP_FRAGMENT = /* glsl */ `
    uniform sampler2D uMap;
    uniform float uOpacity;
    varying vec2 vUv;
    void main() {
        vec3 c = texture2D(uMap, vUv).rgb;
        float edge = 1.0 - smoothstep(0.42, 0.5, length(vUv - 0.5));
        gl_FragColor = vec4(c * uOpacity * edge, 1.0);
    }
`;

function buildBackdropVolume(texture) {
    const group = new THREE.Group();
    group.matrixAutoUpdate = false;
    group.matrix.copy(BACKDROP_MATRIX);
    group.matrixWorldNeedsUpdate = true;

    const geometry = new THREE.PlaneGeometry(BACKDROP.size, BACKDROP.size);
    const materials = [];
    const half = (BACKDROP.slices - 1) / 2;
    let total = 0;
    const weights = [];
    for (let i = 0; i < BACKDROP.slices; i++) {
        const t = (i - half) / Math.max(half, 1); // -1 .. 1
        const w = Math.exp(-(t * t) * 2.2);
        weights.push(w);
        total += w;
    }
    for (let i = 0; i < BACKDROP.slices; i++) {
        const t = (i - half) / Math.max(half, 1);
        const material = new THREE.ShaderMaterial({
            uniforms: { uMap: { value: texture }, uOpacity: { value: 0 } },
            vertexShader: BACKDROP_VERTEX,
            fragmentShader: BACKDROP_FRAGMENT,
            transparent: true,
            depthWrite: false,
            blending: THREE.AdditiveBlending,
            side: THREE.DoubleSide,
        });
        material.userData.weight = weights[i] / total;
        const mesh = new THREE.Mesh(geometry, material);
        mesh.position.z = t * BACKDROP.halfThickness;
        // outer slices are slightly smaller, so the stack reads as a lens edge-on
        const shrink = 1 - 0.28 * Math.pow(Math.abs(t), 1.4);
        mesh.scale.set(shrink, shrink, 1);
        mesh.renderOrder = -1;
        group.add(mesh);
        materials.push(material);
    }
    return { group, materials };
}

/* ---------- star field sampled from the backdrop ---------- */

function imageSampler(image, n) {
    const canvas = document.createElement("canvas");
    canvas.width = canvas.height = n;
    const ctx = canvas.getContext("2d", { willReadFrequently: true });
    ctx.drawImage(image, 0, 0, n, n);
    const pixels = ctx.getImageData(0, 0, n, n).data;

    // cumulative brightness, so a random number picks a pixel in proportion to how
    // bright it is: bright arms get many stars, dust lanes get almost none
    const cdf = new Float64Array(n * n);
    let sum = 0;
    for (let i = 0; i < n * n; i++) {
        const r = pixels[i * 4] / 255;
        const g = pixels[i * 4 + 1] / 255;
        const b = pixels[i * 4 + 2] / 255;
        const lum = 0.25 * r + 0.6 * g + 0.15 * b;
        sum += Math.pow(lum, 1.35);
        cdf[i] = sum;
    }

    const pick = () => {
        const target = rand() * sum;
        let lo = 0;
        let hi = n * n - 1;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (cdf[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };

    return { pixels, n, pick, total: sum };
}

// pixel index -> world position in the galaxy plane, plus disk radius in kly
function pixelToPlane(index, n) {
    const ix = index % n;
    const iy = Math.floor(index / n);
    const x = ((ix + rand()) / n - 0.5) * BACKDROP.size;
    // the texture's v axis runs up the plane, so image row 0 is +Y
    const y = (0.5 - (iy + rand()) / n) * BACKDROP.size;
    const p = new THREE.Vector3(x, y, 0).applyMatrix4(BACKDROP_MATRIX);
    return { p, r: Math.hypot(x, y) };
}

function pixelColor(sampler, index) {
    const { pixels } = sampler;
    return {
        r: pixels[index * 4] / 255,
        g: pixels[index * 4 + 1] / 255,
        b: pixels[index * 4 + 2] / 255,
    };
}

function buildGalaxyFromImage(image) {
    const sampler = imageSampler(image, BACKDROP.sampleSize);
    const stars = new Layer(BACKDROP.stars);
    const gas = new Layer(BACKDROP.gas);
    const knots = new Layer(BACKDROP.knots);
    const color = new THREE.Color();

    for (let i = 0; i < BACKDROP.stars; i++) {
        const index = sampler.pick();
        const c = pixelColor(sampler, index);
        const peak = Math.max(c.r, c.g, c.b);
        if (peak < 0.04) continue;
        const { p, r } = pixelToPlane(index, sampler.n);
        // thin disk, thickening into a round bulge towards the centre
        const sigma = 0.1 + 0.014 * r + 2.2 * Math.exp(-r / 2.6);
        p.y += gauss() * sigma;
        // keep the pixel's hue, vary the brightness per star
        const norm = 1 / peak;
        const mix = rand() * 0.25;
        color.setRGB(
            THREE.MathUtils.lerp(c.r * norm, 1, mix),
            THREE.MathUtils.lerp(c.g * norm, 1, mix),
            THREE.MathUtils.lerp(c.b * norm, 1, mix)
        );
        const size = 1.0 + Math.pow(rand(), 3) * 2.0;
        const alpha = (0.05 + Math.pow(rand(), 3) * 0.45) * (0.35 + 0.65 * peak);
        stars.add(p, color, size, alpha);
    }

    for (let i = 0; i < BACKDROP.gas; i++) {
        const index = sampler.pick();
        const c = pixelColor(sampler, index);
        const { p, r } = pixelToPlane(index, sampler.n);
        if (r < 3.5) continue;
        p.y += gauss() * (0.25 + 0.01 * r + 1.4 * Math.exp(-r / 3));
        color.setRGB(c.r, c.g, c.b);
        gas.add(p, color, 45 + rand() * 90, 0.004 + rand() * 0.008);
    }

    // star-forming regions: the artwork paints them pink, so pick the pink pixels
    let tries = 0;
    while (knots.count < BACKDROP.knots && tries < BACKDROP.knots * 60) {
        tries++;
        const index = sampler.pick();
        const c = pixelColor(sampler, index);
        if (!(c.r > 0.22 && c.r > c.b * 1.12 && c.r > c.g * 1.08)) continue;
        const { p, r } = pixelToPlane(index, sampler.n);
        p.y += gauss() * (0.12 + 0.006 * r);
        color.setRGB(Math.min(c.r * 1.2, 1), c.g * 0.85, c.b * 0.95);
        knots.add(p, color, 1.6 + rand() * 2.6, 0.18 + rand() * 0.3);
    }

    return { stars, gas, knots };
}

function buildBackdropStars() {
    const layer = new Layer(15000);
    const white = new THREE.Color(1.0, 0.97, 0.93);
    const blue = new THREE.Color(0.62, 0.74, 1.0);
    const warm = new THREE.Color(1.0, 0.78, 0.58);
    for (let i = 0; i < 15000; i++) {
        const p = new THREE.Vector3(gauss(), gauss(), gauss()).normalize().multiplyScalar(2500);
        const pick = rand();
        layer.add(p, pick < 0.58 ? white : pick < 0.84 ? blue : warm, 1.0 + Math.pow(rand(), 4) * 2.0, 0.16 + Math.pow(rand(), 3) * 0.7);
    }
    return layer;
}

/*
 * The centre is the densest place in the galaxy: a nuclear star cluster a few
 * light-years across around Sgr A*, holding millions of stars and, models say,
 * thousands of stellar-mass black holes. At this zoom none of that resolves, so it
 * is drawn as a bright, clearly three-dimensional bulb rather than a flat blob.
 */
function buildCore() {
    const group = new THREE.Group();
    const points = new Layer(40000);
    const color = new THREE.Color();
    for (let i = 0; i < 40000; i++) {
        const dir = new THREE.Vector3(gauss(), gauss(), gauss()).normalize();
        const r = 2.4 * Math.pow(rand(), 2.6);
        const p = dir.multiplyScalar(r);
        p.y *= 0.85;
        const warmth = rand();
        color.setRGB(1.0, THREE.MathUtils.lerp(0.72, 0.95, warmth), THREE.MathUtils.lerp(0.42, 0.82, warmth));
        points.add(p, color, 1.0 + Math.pow(rand(), 2) * 1.5, 0.02 + Math.pow(rand(), 2) * 0.1);
    }
    const material = pointsMaterial({ maxSize: 3.0, nearFade: 0.06, sharpness: 16 });
    const cloud = new THREE.Points(points.geometry(), material);
    cloud.renderOrder = 5;
    cloud.frustumCulled = false;
    group.add(cloud);

    // three dashed circles: a simple, readable outline of the dense nuclear region
    const shellMaterial = new THREE.LineDashedMaterial({
        color: 0xffd9a0,
        transparent: true,
        opacity: 0.3,
        depthWrite: false,
        dashSize: 0.22,
        gapSize: 0.18,
    });
    const CORE_SHELL_RADIUS = 1.6;
    for (const axis of ["x", "y", "z"]) {
        const pts = [];
        for (let i = 0; i <= 128; i++) {
            const a = (i / 128) * Math.PI * 2;
            const c = Math.cos(a) * CORE_SHELL_RADIUS;
            const d = Math.sin(a) * CORE_SHELL_RADIUS;
            pts.push(axis === "x" ? new THREE.Vector3(0, c, d) : axis === "y" ? new THREE.Vector3(c, 0, d) : new THREE.Vector3(c, d, 0));
        }
        const circle = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), shellMaterial);
        circle.computeLineDistances();
        circle.renderOrder = 7;
        group.add(circle);
    }

    const shells = [
        glowSprite(new THREE.Color(1.0, 0.88, 0.7), 3.4, 0.22),
        glowSprite(new THREE.Color(0.95, 0.72, 0.45), 9, 0.13),
        glowSprite(new THREE.Color(0.55, 0.42, 0.62), 18, 0.07),
    ];
    for (const shell of shells) {
        shell.renderOrder = 6;
        group.add(shell);
    }
    return { group, material, shells, shellMaterial, shellRadius: CORE_SHELL_RADIUS };
}

function buildArmOutlines() {
    const group = new THREE.Group();
    const material = new THREE.LineDashedMaterial({
        color: 0x8fa7d8,
        transparent: true,
        opacity: 0.22,
        depthWrite: false,
        dashSize: 0.9,
        gapSize: 0.7,
    });
    const draw = (phase, rMin, rMax) => {
        const points = [];
        for (let i = 0; i <= 160; i++) points.push(armPoint(phase, THREE.MathUtils.lerp(rMin, rMax, i / 160)));
        const line = new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), material);
        line.computeLineDistances();
        group.add(line);
    };
    for (const arm of ARMS) draw(armPhase(arm.crossing), 8.5, GALAXY_RADIUS);
    draw(armPhase(ORION_SPUR.crossing), ORION_SPUR.rMin, ORION_SPUR.rMax);
    return { group, material };
}

function buildDeepSky(objects) {
    const layer = new Layer(objects.length);
    for (const o of objects) layer.add(o.position, new THREE.Color(DEEP_SKY_STYLE[o.kind].color), DEEP_SKY_STYLE[o.kind].size, 0.9);
    const material = pointsMaterial({ maxSize: 18, sharpness: 6, attenuate: 0 });
    const points = new THREE.Points(layer.geometry(), material);
    points.renderOrder = 8;
    points.frustumCulled = false;
    return { points, material };
}

function galaxySprite(url, size, opacity) {
    const texture = new THREE.TextureLoader().load(url);
    texture.colorSpace = THREE.SRGBColorSpace;
    const sprite = new THREE.Sprite(
        new THREE.SpriteMaterial({
            map: texture,
            blending: THREE.AdditiveBlending,
            depthWrite: false,
            transparent: true,
            opacity,
        })
    );
    sprite.scale.setScalar(size);
    return sprite;
}

function buildGalaxies(galaxies, backgroundImages, baseUrl) {
    const group = new THREE.Group();
    const sprites = [];
    for (const g of galaxies) {
        // no image: a soft glow, which is honest for a shredded dwarf galaxy
        const sprite = g.image
            ? galaxySprite(`${baseUrl}${g.image}`, g.size / 1000, 0.85)
            : glowSprite(new THREE.Color(0.85, 0.8, 0.95), g.size / 1000, 0.32);
        sprite.position.copy(truePosition(g.l, g.b, g.display));
        sprite.renderOrder = 9;
        group.add(sprite);
        sprites.push(sprite);
    }
    // decorative far field: real photographs, scattered, deliberately nameless
    for (let i = 0; i < 18 && backgroundImages.length; i++) {
        const image = backgroundImages[Math.floor(rand() * backgroundImages.length)];
        const sprite = galaxySprite(`${baseUrl}${image}`, 60 + rand() * 190, 0.2 + rand() * 0.35);
        const dir = new THREE.Vector3(gauss(), gauss() * 0.7, gauss()).normalize();
        sprite.position.copy(dir.multiplyScalar(900 + rand() * 1100));
        sprite.renderOrder = 9;
        group.add(sprite);
        sprites.push(sprite);
    }
    return { group, sprites };
}

/* ---------- local neighbourhood ---------- */

function buildLocal(systems, structures) {
    const group = new THREE.Group();
    const lineMaterial = new THREE.LineBasicMaterial({ color: 0x9ecbff, transparent: true, opacity: 0.35, depthWrite: false });
    const structureMaterial = new THREE.LineDashedMaterial({
        color: 0x9ecbff,
        transparent: true,
        opacity: 0.4,
        depthWrite: false,
        dashSize: 0.05,
        gapSize: 0.04,
    });

    const ring = (radius, material) => {
        const pts = [];
        for (let i = 0; i <= 160; i++) {
            const a = (i / 160) * Math.PI * 2;
            pts.push(new THREE.Vector3(SUN.x + radius * Math.cos(a), SUN.y, SUN.z + radius * Math.sin(a)));
        }
        const line = new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), material);
        line.computeLineDistances();
        group.add(line);
    };

    for (const ly of LOCAL_RINGS_LY) ring(localRadius(ly), lineMaterial);
    for (const s of structures) ring(localRadius(s.radius), structureMaterial);

    // drop lines from each system to the galactic plane
    const drops = [];
    const dots = new Layer(systems.length);
    for (const s of systems) {
        drops.push(s.position, new THREE.Vector3(s.position.x, SUN.y, s.position.z));
        dots.add(s.position, new THREE.Color(s.color), 10, 1);
    }
    group.add(new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(drops), lineMaterial));
    const dotMaterial = pointsMaterial({ maxSize: 14, sharpness: 10, attenuate: 0 });
    group.add(new THREE.Points(dots.geometry(), dotMaterial));

    return { group, materials: [lineMaterial, structureMaterial], dotMaterial };
}

/* ---------- labels ---------- */

class Marker {
    constructor({
        position,
        name,
        sub = "",
        level,
        layer = "systems",
        maxDistance = Infinity,
        kind = "link",
        href = null,
        color = null,
        fictional = false,
        onClick = null,
        priority = null,
        tangent = null,
    }) {
        this.position = position;
        this.level = level;
        this.layer = layer;
        this.maxDistance = maxDistance;
        this.tangent = tangent;
        const el = document.createElement(href ? "a" : "div");
        el.className = `GalaxyMarker ${kind === "region" ? "Region" : kind === "ring" ? "Ring" : "Link"}${fictional ? " Fictional" : ""}`;
        if (href) el.href = href;
        if (color) el.style.setProperty("--marker-color", color);
        if (kind === "link") {
            const icon = document.createElement("span");
            icon.className = "GalaxyMarkerIcon";
            el.appendChild(icon);
        }
        const text = document.createElement("span");
        text.className = "GalaxyMarkerText";
        text.innerHTML = `<span class="GalaxyMarkerName"></span>${sub ? '<span class="GalaxyMarkerSub"></span>' : ""}`;
        text.querySelector(".GalaxyMarkerName").textContent = name;
        if (sub) text.querySelector(".GalaxyMarkerSub").textContent = sub;
        el.appendChild(text);
        if (onClick) {
            el.addEventListener("click", (event) => {
                event.preventDefault();
                onClick();
            });
        }
        this.el = el;
        this.centered = kind !== "link";
        this.visible = false;
        // lower wins when two labels overlap: our systems first, then structure, then landmarks
        this.priority = priority ?? (kind === "link" ? 0 : kind === "ring" ? 3 : layer === "arms" ? 1 : 2);
    }

    // project to screen space; the view decides afterwards which labels survive
    project(camera, width, height, allowed, cameraDistance) {
        const p = this.position.clone().project(camera);
        this.onScreen = p.z < 1 && Math.abs(p.x) < 1.1 && Math.abs(p.y) < 1.1;
        this.screenX = (p.x * 0.5 + 0.5) * width;
        this.screenY = (-p.y * 0.5 + 0.5) * height;
        this.candidate = allowed && this.onScreen && cameraDistance < this.maxDistance;
        if (this.tangent) {
            // lay the label along the arm by following it to a second point
            const q = this.tangent.clone().project(camera);
            const dx = (q.x - p.x) * width;
            const dy = -(q.y - p.y) * height;
            let angle = (Math.atan2(dy, dx) * 180) / Math.PI;
            if (angle > 90) angle -= 180;
            if (angle < -90) angle += 180;
            this.angle = angle;
        }
        return this.candidate;
    }

    // label box in pixels, measured once and after a resize
    measure() {
        if (!this.width || !this.height) {
            this.width = this.el.offsetWidth;
            this.height = this.el.offsetHeight;
        }
        return this.width > 0;
    }

    apply(visible, iconHalf) {
        if (visible !== this.visible) {
            this.el.classList.toggle("Visible", visible);
            this.visible = visible;
        }
        if (!this.onScreen) return;
        const rotate = this.angle ? ` rotate(${this.angle.toFixed(1)}deg)` : "";
        this.el.style.transform = this.centered
            ? `translate(${this.screenX}px, ${this.screenY}px) translate(-50%, -50%)${rotate}`
            : `translate(${this.screenX - iconHalf}px, ${this.screenY}px) translate(0, -50%)`;
    }
}

/* ---------- view ---------- */

class GalaxyView {
    constructor() {
        this.root = document.getElementById("GALAXY_VIEW");
        this.canvas = document.getElementById("GALAXY_CANVAS");
        this.labels = document.getElementById("GALAXY_LABELS");
        this.readout = document.getElementById("GALAXY_READOUT");
        this.scaleNote = document.getElementById("GALAXY_SCALE_NOTE");
        this.objectList = document.getElementById("GALAXY_OBJECT_LIST");
        this.running = false;
        this.flight = null;
        this.lastInteraction = 0;
        this.lastListUpdate = 0;
        this.listKey = "";
        this.layerState = {};
        this.markers = [];

        this.renderer = new THREE.WebGLRenderer({ canvas: this.canvas, antialias: false, powerPreference: "high-performance" });
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.setClearColor(0x000000, 1);

        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(50, 1, 0.01, 9000);

        this.controls = new OrbitControls(this.camera, this.canvas);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.08;
        this.controls.minDistance = 0.8;
        this.controls.maxDistance = 600;
        this.controls.maxPolarAngle = THREE.MathUtils.degToRad(88);
        this.controls.screenSpacePanning = false;
        this.controls.zoomSpeed = 1.2;
        this.controls.autoRotate = true;
        this.controls.autoRotateSpeed = 0.2;
        // left button moves the map, right button tilts and turns it
        this.controls.mouseButtons = { LEFT: THREE.MOUSE.PAN, MIDDLE: THREE.MOUSE.DOLLY, RIGHT: THREE.MOUSE.ROTATE };
        this.controls.addEventListener("start", () => {
            this.flight = null;
            this.controls.autoRotate = false;
            this.lastInteraction = performance.now();
        });

        this.buildScene();
        this.buildMarkers();
        this.bindControls();
        this.bindPanels();
        this.placeCamera(OVERVIEW);

        window.addEventListener("resize", () => this.resize());
        this.resize();
    }

    buildScene() {
        this.materials = {
            stars: pointsMaterial({ maxSize: 3.2, nearFade: 0.08, sharpness: 18 }),
            gas: pointsMaterial({ maxSize: 900, nearFade: 3.5, sharpness: 2.5 }),
            knots: pointsMaterial({ maxSize: 12, nearFade: 0.6, sharpness: 9 }),
            backdropStars: pointsMaterial({ maxSize: 4, sharpness: 18, attenuate: 0 }),
        };
        const backdropStars = new THREE.Points(buildBackdropStars().geometry(), this.materials.backdropStars);
        backdropStars.frustumCulled = false;
        this.scene.add(backdropStars);

        this.core = buildCore();
        this.scene.add(this.core.group);

        this.arms = buildArmOutlines();
        this.scene.add(this.arms.group);

        this.deepSky = (DATA.deepSky || [])
            .filter((o) => o.kind !== "structure")
            .map((o) => ({ ...o, position: truePosition(o.l, o.b, o.d) }));
        this.structures = (DATA.deepSky || []).filter((o) => o.kind === "structure");
        this.deepSkyPoints = buildDeepSky(this.deepSky);
        this.scene.add(this.deepSkyPoints.points);

        this.galaxies = DATA.galaxies || [];
        this.galaxyGroup = buildGalaxies(this.galaxies, DATA.backgroundGalaxies || [], this.root.dataset.galaxies);
        this.scene.add(this.galaxyGroup.group);

        this.localSystems = DATA.systems
            .filter((s) => !s.placement.fictional && s.placement.d > 0)
            .map((s) => ({ ...s, position: localPosition(s.placement) }));
        this.local = buildLocal(this.localSystems, this.structures);
        this.local.group.renderOrder = 7;
        this.scene.add(this.local.group);

        // the artwork drives both the backdrop and the star field, so everything that
        // depends on it is built once the image arrives
        new THREE.TextureLoader().load(this.root.dataset.backdrop, (texture) => {
            texture.colorSpace = THREE.SRGBColorSpace;
            this.backdrop = buildBackdropVolume(texture);
            this.scene.add(this.backdrop.group);
            const galaxy = buildGalaxyFromImage(texture.image);
            for (const [key, order] of [["gas", 1], ["stars", 2], ["knots", 4]]) {
                const points = new THREE.Points(galaxy[key].geometry(), this.materials[key]);
                points.renderOrder = order;
                points.frustumCulled = false;
                this.scene.add(points);
            }
            this.root.classList.add("Ready");
        });
    }

    buildMarkers() {
        this.markers = [];
        this.registry = [];
        const add = (options) => {
            const marker = new Marker(options);
            this.labels.appendChild(marker.el);
            this.markers.push(marker);
            return marker;
        };

        for (const arm of ARMS) {
            const phase = armPhase(arm.crossing);
            add({
                position: armPoint(phase, arm.label),
                tangent: armPoint(phase, arm.label * 1.08),
                name: arm.name,
                level: "galaxy",
                layer: "arms",
                kind: "region",
            });
            if (arm.outerLabel) {
                add({
                    position: armPoint(phase, 41),
                    tangent: armPoint(phase, 44),
                    name: arm.outerLabel,
                    level: "galaxy",
                    layer: "arms",
                    kind: "region",
                });
            }
        }
        const spurPhase = armPhase(ORION_SPUR.crossing);
        add({
            position: armPoint(spurPhase, 29.5).add(new THREE.Vector3(2.5, 0, 0)),
            tangent: armPoint(spurPhase, 30.5).add(new THREE.Vector3(2.5, 0, 0)),
            name: ORION_SPUR.name,
            level: "galaxy",
            layer: "arms",
            kind: "region",
        });
        add({
            position: new THREE.Vector3(0, 0, 0),
            name: "Sgr A*",
            sub: "Supermassive black hole · 4.3 million suns",
            level: "galaxy",
            layer: "arms",
            color: "#ffd9a0",
            priority: 0.5,
            onClick: () => this.flyTo({ target: new THREE.Vector3(0, 0, 0), distance: 12, polar: 1.05 }),
        });

        add({
            position: new THREE.Vector3(0, this.core.shellRadius, 0),
            name: "Nuclear bulge",
            sub: "Densest stars and black holes in the galaxy",
            level: "galaxy",
            layer: "arms",
            maxDistance: 60,
            kind: "region",
            priority: 0.6,
        });

        const sun = DATA.systems.find((s) => s.placement.d === 0 && !s.placement.fictional);
        add({
            position: SUN,
            name: "Sol",
            sub: `Local neighbourhood · ${this.localSystems.length} systems`,
            level: "galaxy",
            color: "#9ecbff",
            onClick: () => this.flyToSun(),
        });
        if (sun) {
            const marker = add({ position: SUN, name: "Sun", sub: "Solar System · you are here", level: "local", href: sun.href, color: sun.color });
            this.registry.push({ group: "Star systems", name: "Sun", sub: "Solar System", marker, fly: () => this.flyToSun() });
        }
        for (const s of this.localSystems) {
            const marker = add({ position: s.position, name: s.name, sub: formatLy(s.placement.d), level: "local", href: s.href, color: s.color });
            this.registry.push({
                group: "Star systems",
                name: s.name,
                sub: formatLy(s.placement.d),
                marker,
                fly: () => this.flyTo({ target: s.position.clone(), distance: 1.6 }),
            });
        }
        for (const s of DATA.systems.filter((s) => s.placement.fictional)) {
            const position = new THREE.Vector3(s.placement.x / 1000, 0, s.placement.z / 1000);
            add({ position, name: s.name, sub: `Fictional · ${s.placement.source}`, level: "galaxy", href: s.href, color: s.color, fictional: true });
        }
        for (const o of this.deepSky) {
            const style = DEEP_SKY_STYLE[o.kind];
            const marker = add({
                position: o.position,
                name: o.name,
                sub: `${o.alias} · ${style.label} · ${formatLy(o.d)}`,
                level: "galaxy",
                layer: "deepsky",
                maxDistance: DEEP_SKY_LABEL_DISTANCE,
                kind: "region",
            });
            this.registry.push({
                group: "Nebulae & clusters",
                name: o.name,
                sub: `${style.label} · ${formatLy(o.d)}`,
                marker,
                fly: () => this.flyTo({ target: o.position.clone(), distance: 8 }),
            });
        }
        for (const g of this.galaxies) {
            const position = truePosition(g.l, g.b, g.display);
            const compressed = g.display !== g.d ? " · shown closer" : "";
            const marker = add({
                position,
                name: g.name,
                sub: `${g.alias} · ${formatLy(g.d)}${compressed}`,
                level: "galaxy",
                layer: "galaxies",
                kind: "region",
            });
            this.registry.push({
                group: "Galaxies",
                name: g.name,
                sub: `${formatLy(g.d)}${compressed}`,
                marker,
                fly: () => this.flyTo({ target: position.clone(), distance: (g.size / 1000) * 2.2 }),
            });
        }
        for (const s of this.structures) {
            const marker = add({
                position: SUN.clone().add(new THREE.Vector3(0, 0, -localRadius(s.radius))),
                name: s.name,
                sub: `${s.alias} · about ${formatLy(s.radius * 2)} across`,
                level: "local",
                layer: "deepsky",
                kind: "region",
            });
            this.registry.push({ group: "Nebulae & clusters", name: s.name, sub: s.alias, marker, fly: () => this.flyToSun() });
        }
        for (const ly of LOCAL_RINGS_LY) {
            add({ position: SUN.clone().add(new THREE.Vector3(0, 0, -localRadius(ly))), name: formatLy(ly), level: "local", kind: "ring" });
        }
    }

    bindControls() {
        this.root.querySelectorAll(".GalaxyControls button").forEach((button) => {
            button.addEventListener("click", () => {
                const action = button.dataset.action;
                if (action === "overview") this.flyTo(OVERVIEW);
                if (action === "sun") this.flyToSun();
                if (action === "zoom-in") this.zoomBy(0.6);
                if (action === "zoom-out") this.zoomBy(1 / 0.6);
            });
        });
    }

    bindPanels() {
        this.root.querySelectorAll("[data-panel]").forEach((button) => {
            const panel = document.getElementById(button.dataset.panel);
            button.addEventListener("click", () => {
                const open = panel.classList.toggle("Open");
                button.classList.toggle("Active", open);
                button.setAttribute("aria-expanded", String(open));
            });
        });
        this.root.querySelectorAll(".GalaxyLayer input").forEach((input) => {
            const key = input.dataset.layer;
            let saved = null;
            try {
                saved = localStorage.getItem(`galaxyLayer:${key}`);
            } catch (e) {}
            if (saved !== null) input.checked = saved === "1";
            this.layerState[key] = input.checked;
            input.addEventListener("change", () => {
                this.layerState[key] = input.checked;
                try {
                    localStorage.setItem(`galaxyLayer:${key}`, input.checked ? "1" : "0");
                } catch (e) {}
            });
        });
    }

    spherical() {
        return new THREE.Spherical().setFromVector3(this.camera.position.clone().sub(this.controls.target));
    }

    placeCamera({ target, distance, polar, azimuth }) {
        this.controls.target.copy(target);
        this.camera.position.copy(target).add(new THREE.Vector3().setFromSphericalCoords(distance, polar, azimuth));
        this.controls.update();
    }

    flyTo({ target, distance, polar, azimuth }, duration = 1600) {
        const from = this.spherical();
        this.flight = {
            start: performance.now(),
            duration,
            fromTarget: this.controls.target.clone(),
            toTarget: target.clone(),
            fromSph: from,
            toSph: new THREE.Spherical(THREE.MathUtils.clamp(distance, this.controls.minDistance, this.controls.maxDistance), polar ?? from.phi, azimuth ?? from.theta),
        };
        this.controls.autoRotate = false;
        this.lastInteraction = performance.now();
    }

    flyToSun() {
        this.flyTo({ target: SUN, distance: 3.4, polar: 1.0 });
    }

    zoomBy(factor) {
        const s = this.spherical();
        this.flyTo({ target: this.controls.target.clone(), distance: s.radius * factor }, 600);
    }

    stepFlight(now) {
        const f = this.flight;
        const t = Math.min((now - f.start) / f.duration, 1);
        const e = t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
        // interpolate the distance logarithmically so long zooms feel even
        const radius = Math.exp(THREE.MathUtils.lerp(Math.log(f.fromSph.radius), Math.log(f.toSph.radius), e));
        let dTheta = f.toSph.theta - f.fromSph.theta;
        dTheta = Math.atan2(Math.sin(dTheta), Math.cos(dTheta));
        const target = f.fromTarget.clone().lerp(f.toTarget, e);
        const offset = new THREE.Vector3().setFromSphericalCoords(
            radius,
            THREE.MathUtils.lerp(f.fromSph.phi, f.toSph.phi, e),
            f.fromSph.theta + dTheta * e
        );
        this.controls.target.copy(target);
        this.camera.position.copy(target).add(offset);
        if (t >= 1) this.flight = null;
    }

    resize() {
        const width = this.root.clientWidth || window.innerWidth;
        const height = this.root.clientHeight || window.innerHeight;
        this.renderer.setSize(width, height, false);
        this.camera.aspect = width / height;
        this.camera.updateProjectionMatrix();
        this.width = width;
        this.height = height;
        // point sizes are authored for a ~900px tall view seen from ~80 units away
        const scale = (height / 900) * this.renderer.getPixelRatio() * 80;
        for (const m of [...Object.values(this.materials), this.local.dotMaterial, this.deepSkyPoints.material, this.core.material]) {
            m.uniforms.uScale.value = scale;
        }
        this.iconHalf = Math.min(width, height) * 0.0055;
        // label boxes are sized in vmin, so they change with the viewport
        for (const marker of this.markers) {
            marker.width = 0;
            marker.height = 0;
        }
    }

    updateObjectList(now) {
        if (now - this.lastListUpdate < 350) return;
        this.lastListUpdate = now;
        const groups = new Map();
        for (const entry of this.registry) {
            if (!entry.marker.candidate && !entry.marker.onScreenAllowed) continue;
            if (!groups.has(entry.group)) groups.set(entry.group, []);
            groups.get(entry.group).push(entry);
        }
        const key = [...groups].map(([g, list]) => `${g}:${list.length}`).join("|");
        if (key === this.listKey) return;
        this.listKey = key;
        this.objectList.textContent = "";
        if (!groups.size) {
            const empty = document.createElement("p");
            empty.className = "GalaxyPanelNote";
            empty.textContent = "Nothing in view. Zoom out or switch layers on.";
            this.objectList.appendChild(empty);
            return;
        }
        for (const [group, list] of groups) {
            const heading = document.createElement("p");
            heading.className = "GalaxyListHeading";
            heading.textContent = `${group} · ${list.length}`;
            this.objectList.appendChild(heading);
            for (const entry of list) {
                const row = document.createElement("button");
                row.type = "button";
                row.className = "GalaxyListRow";
                row.innerHTML = `<span class="GalaxyListName"></span><span class="GalaxyListSub"></span>`;
                row.querySelector(".GalaxyListName").textContent = entry.name;
                row.querySelector(".GalaxyListSub").textContent = entry.sub;
                row.addEventListener("click", () => entry.fly());
                this.objectList.appendChild(row);
            }
        }
    }

    frame(now) {
        if (!this.running) return;
        requestAnimationFrame((t) => this.frame(t));

        if (this.flight) this.stepFlight(now);
        if (!this.flight && !this.controls.autoRotate && now - this.lastInteraction > 25000 && this.spherical().radius > 20) {
            this.controls.autoRotate = true;
        }
        this.controls.update();

        // keep the target inside the galaxy and near the plane
        const target = this.controls.target;
        if (target.length() > GALAXY_RADIUS * 8) target.setLength(GALAXY_RADIUS * 8);
        target.y = THREE.MathUtils.clamp(target.y, -GALAXY_RADIUS, GALAXY_RADIUS);

        const cameraDistance = this.spherical().radius;
        const sunDistance = this.camera.position.distanceTo(SUN);
        const local = 1 - smoothstep(LOCAL_FULL, LOCAL_ENTER, sunDistance);

        this.local.group.visible = local > 0.01 && this.layerState.systems !== false;
        for (const m of this.local.materials) m.opacity = 0.35 * local;
        this.local.dotMaterial.uniforms.uOpacity.value = local;
        this.materials.gas.uniforms.uOpacity.value = 1 - 0.6 * local;

        /*
         * The backdrop stays visible at every angle, including edge-on, because the
         * slices give it thickness. It only fades as the camera comes close, where
         * its resolution runs out and our own stars carry the detail.
         */
        if (this.backdrop) {
            const closeFade = smoothstep(5, 24, cameraDistance);
            const on = this.layerState.backdrop !== false;
            this.backdrop.group.visible = on;
            for (const m of this.backdrop.materials) {
                m.uniforms.uOpacity.value = BACKDROP.opacity * m.userData.weight * closeFade;
            }
        }

        this.arms.group.visible = this.layerState.arms !== false && local < 0.99;
        this.arms.material.opacity = 0.22 * (1 - local);
        this.core.shellMaterial.opacity = 0.3 * (1 - local) * (this.layerState.arms !== false ? 1 : 0);
        this.deepSkyPoints.points.visible = this.layerState.deepsky !== false && local < 0.99;
        this.deepSkyPoints.material.uniforms.uOpacity.value = 1 - local;
        this.galaxyGroup.group.visible = this.layerState.galaxies !== false;
        this.scaleNote.classList.toggle("Visible", local > 0.5);

        const candidates = [];
        for (const marker of this.markers) {
            const levelMatches = marker.level === "local" ? local > 0.5 : local < 0.5;
            const layerOn = this.layerState[marker.layer] !== false;
            const allowed = levelMatches && layerOn;
            if (marker.project(this.camera, this.width, this.height, allowed, cameraDistance)) candidates.push(marker);
            // the object list cares about what is in view, not about label collisions
            marker.onScreenAllowed = allowed && marker.onScreen;
        }
        // drop labels whose box would overlap a more important one
        candidates.sort((a, b) => a.priority - b.priority);
        const kept = [];
        for (const marker of candidates) {
            marker.measure();
            // region labels are centred on the point, link labels sit to the right of their icon
            marker.boxX = marker.centered ? marker.screenX : marker.screenX + marker.width / 2;
            const clash = kept.some(
                (other) =>
                    Math.abs(other.boxX - marker.boxX) < (other.width + marker.width) * 0.5 + 8 &&
                    Math.abs(other.screenY - marker.screenY) < (other.height + marker.height) * 0.5 + 2
            );
            if (!clash) kept.push(marker);
            marker.keep = !clash;
        }
        for (const marker of this.markers) marker.apply(Boolean(marker.candidate && marker.keep), this.iconHalf);

        this.updateObjectList(now);

        const fromCore = Math.round(target.length() * 1000);
        const fromSun = Math.round(target.distanceTo(SUN) * 1000);
        this.readout.textContent = local > 0.5
            ? "Sol-centred · rings at 10 / 100 / 1,000 ly"
            : `Target · ${fromCore.toLocaleString("en-US")} ly from core · ${fromSun.toLocaleString("en-US")} ly from Sol`;

        this.renderer.render(this.scene, this.camera);
    }

    start() {
        if (this.running) return;
        this.running = true;
        this.resize();
        requestAnimationFrame((t) => this.frame(t));
    }

    stop() {
        this.running = false;
    }
}

let view = null;

function onView(name) {
    if (name === "galaxy") {
        view ??= new GalaxyView();
        window.galaxyView = view; // handy for tuning from the console
        view.start();
    } else if (view) {
        view.stop();
    }
}

document.addEventListener("mainview", (event) => onView(event.detail));
if (document.body.classList.contains("ViewGalaxy")) onView("galaxy");
