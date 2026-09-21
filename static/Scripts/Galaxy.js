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
const BAR_ANGLE = THREE.MathUtils.degToRad(117);
const BAR_HALF_LENGTH = 9;

// radius (kly) at which each arm crosses the Sun-centre line; the four crossings are
// spaced by exp(2*pi*k/4), which puts Sagittarius inside the Sun and Perseus outside
const ARMS = [
    { name: "Norma Arm", crossing: 10.8, weight: 0.8, label: 13, outerLabel: "Outer Arm" },
    { name: "Scutum–Centaurus Arm", crossing: 15.0, weight: 1.3, label: 21 },
    { name: "Sagittarius Arm", crossing: 21.0, weight: 0.9, label: 16 },
    { name: "Perseus Arm", crossing: 29.3, weight: 1.3, label: 36 },
];
const ORION_SPUR = { name: "Orion Spur", crossing: 26.3, rMin: 23, rMax: 30.5 };

/*
 * The backdrop is R. Hurt's face-on artist's concept (NASA/JPL-Caltech, public
 * domain). Its bar sits at 47 degrees in image coordinates; rotating the plane by
 * 16 degrees lines that up with the bar we generate, which also brings the
 * artwork's own Sun to within ~16 degrees of our Sol marker. It is an artist's
 * impression, not a survey, so treat it as a backdrop and not as ground truth.
 */
const BACKDROP = { rotation: THREE.MathUtils.degToRad(16), size: GALAXY_RADIUS * 2.3, opacity: 0.5 };

const LOCAL_LOG_SCALE = 0.5;
const LOCAL_RINGS_LY = [10, 100, 1000];
const LOCAL_ENTER = 9;
const LOCAL_FULL = 5;
const DEEP_SKY_LABEL_DISTANCE = 45;

const OVERVIEW = { target: new THREE.Vector3(0, 0, 0), distance: 85, polar: 0.9, azimuth: 0.45 };

const DEEP_SKY_STYLE = {
    nebula: { layer: "nebulae", color: "#ff6b8a", size: 13, label: "Nebula" },
    open: { layer: "clusters", color: "#bcd8ff", size: 10, label: "Open cluster" },
    globular: { layer: "clusters", color: "#ffd9a0", size: 12, label: "Globular cluster" },
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
function localPosition(placement) {
    const r = LOCAL_LOG_SCALE * Math.log10(1 + placement.d);
    return directionFromSun(placement.l, placement.b).multiplyScalar(r).add(SUN);
}

function formatLy(ly) {
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
    }

    add(p, color, size, alpha) {
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

const COLORS = {
    bulge: new THREE.Color(1.0, 0.8, 0.55),
    bulgeWhite: new THREE.Color(1.0, 0.93, 0.8),
    armBlue: new THREE.Color(0.62, 0.74, 1.0),
    white: new THREE.Color(1.0, 0.97, 0.93),
    warm: new THREE.Color(1.0, 0.78, 0.58),
    diskOld: new THREE.Color(0.95, 0.86, 0.74),
    gasBlue: new THREE.Color(0.3, 0.45, 0.95),
    gasPink: new THREE.Color(0.95, 0.38, 0.6),
    gasCore: new THREE.Color(1.0, 0.72, 0.42),
    hii: new THREE.Color(1.0, 0.42, 0.62),
    dust: new THREE.Color(0.018, 0.012, 0.01),
};

function tint(base, amount) {
    return base.clone().offsetHSL((rand() - 0.5) * amount, 0, (rand() - 0.5) * amount);
}

function barPoint(spreadAlong, spreadAcross, spreadY) {
    const u = gauss() * spreadAlong;
    const v = gauss() * spreadAcross;
    const cos = Math.cos(BAR_ANGLE);
    const sin = Math.sin(BAR_ANGLE);
    return new THREE.Vector3(u * cos - v * sin, gauss() * spreadY, u * sin + v * cos);
}

function sampleArmRadius(rMin) {
    let r;
    do {
        r = rMin - Math.log(1 - rand()) * 13;
    } while (r > GALAXY_RADIUS);
    return r;
}

// a point near an arm: offset across the arm (negative = towards the centre) and in height
function scatterFromArm(phase, r, across, height) {
    const theta = armAngle(phase, r);
    const rr = r + across;
    return new THREE.Vector3(rr * Math.cos(theta), height, rr * Math.sin(theta));
}

function buildGalaxy() {
    const stars = new Layer(340000);
    const gas = new Layer(9000);
    const dust = new Layer(8000);
    const knots = new Layer(1600);

    const arms = [...ARMS.map((a) => ({ ...a, phase: armPhase(a.crossing), rMin: 8.5, rMax: GALAXY_RADIUS })),
        { ...ORION_SPUR, weight: 0.35, phase: armPhase(ORION_SPUR.crossing) }];
    const totalWeight = arms.reduce((s, a) => s + a.weight, 0);

    // young stars along the arms, partly in clumps
    for (const arm of arms) {
        const count = Math.round((170000 * arm.weight) / totalWeight);
        let clumpR = 0;
        let clumpAcross = 0;
        for (let i = 0; i < count; i++) {
            let r = arm.rMax < GALAXY_RADIUS ? THREE.MathUtils.lerp(arm.rMin, arm.rMax, rand()) : sampleArmRadius(arm.rMin);
            const width = 0.7 + 0.05 * r;
            let across = gauss() * width;
            if (i % 40 === 0) {
                clumpR = r;
                clumpAcross = across;
            } else if (rand() < 0.3) {
                r = clumpR + gauss() * 0.35;
                across = clumpAcross + gauss() * 0.25;
            }
            const p = scatterFromArm(arm.phase, r, across, gauss() * (0.18 + 0.006 * r));
            const pick = rand();
            const color = pick < 0.68 ? tint(COLORS.armBlue, 0.06) : pick < 0.9 ? tint(COLORS.white, 0.04) : tint(COLORS.warm, 0.05);
            stars.add(p, color, 1.0 + Math.pow(rand(), 3) * 2.2, 0.1 + Math.pow(rand(), 3) * 0.55);
        }

        // gas glow, dust lane on the inner edge, star-forming knots
        const gasCount = Math.round((5200 * arm.weight) / totalWeight);
        for (let i = 0; i < gasCount; i++) {
            const r = arm.rMax < GALAXY_RADIUS ? THREE.MathUtils.lerp(arm.rMin, arm.rMax, rand()) : sampleArmRadius(arm.rMin);
            const p = scatterFromArm(arm.phase, r, gauss() * (0.9 + 0.06 * r), gauss() * 0.3);
            const color = rand() < 0.22 ? tint(COLORS.gasPink, 0.05) : tint(COLORS.gasBlue, 0.05);
            gas.add(p, color, 50 + rand() * 90, 0.006 + rand() * 0.01);
        }
        const dustCount = Math.round((6500 * arm.weight) / totalWeight);
        for (let i = 0; i < dustCount; i++) {
            const r = arm.rMax < GALAXY_RADIUS ? THREE.MathUtils.lerp(arm.rMin, arm.rMax, rand()) : sampleArmRadius(arm.rMin);
            const width = 0.7 + 0.05 * r;
            const p = scatterFromArm(arm.phase, r, -width * 0.7 + gauss() * width * 0.45, gauss() * 0.1);
            dust.add(p, COLORS.dust, 24 + rand() * 30, 0.025 + rand() * 0.05);
        }
        const knotCount = Math.round((900 * arm.weight) / totalWeight);
        for (let i = 0; i < knotCount; i++) {
            const r = arm.rMax < GALAXY_RADIUS ? THREE.MathUtils.lerp(arm.rMin, arm.rMax, rand()) : sampleArmRadius(arm.rMin);
            const p = scatterFromArm(arm.phase, r, gauss() * (0.3 + 0.02 * r), gauss() * 0.1);
            knots.add(p, tint(COLORS.hii, 0.05), 1.5 + rand() * 2.5, 0.2 + rand() * 0.35);
        }
    }

    // old disk population between the arms
    for (let i = 0; i < 75000; i++) {
        let r;
        do {
            r = -Math.log(1 - rand()) * 11;
        } while (r > GALAXY_RADIUS || r < 2);
        const theta = rand() * Math.PI * 2;
        const p = new THREE.Vector3(r * Math.cos(theta), gauss() * (0.3 + 0.01 * r), r * Math.sin(theta));
        stars.add(p, tint(COLORS.diskOld, 0.05), 1.0 + rand() * 0.8, 0.045 + rand() * 0.12);
    }

    // bar and bulge
    for (let i = 0; i < 55000; i++) {
        const p = barPoint(BAR_HALF_LENGTH * 0.42, 1.5, 1.0);
        stars.add(p, rand() < 0.6 ? tint(COLORS.bulge, 0.04) : tint(COLORS.bulgeWhite, 0.03), 1.0 + rand() * 1.4, 0.03 + rand() * 0.09);
    }
    for (let i = 0; i < 20000; i++) {
        const p = new THREE.Vector3(gauss() * 1.6, gauss() * 1.2, gauss() * 1.6);
        stars.add(p, tint(COLORS.bulgeWhite, 0.03), 1.2 + rand() * 1.5, 0.035 + rand() * 0.09);
    }
    for (let i = 0; i < 700; i++) {
        const p = barPoint(BAR_HALF_LENGTH * 0.4, 2.0, 0.8);
        gas.add(p, tint(COLORS.gasCore, 0.04), 60 + rand() * 80, 0.012 + rand() * 0.015);
    }

    // thin stellar halo
    for (let i = 0; i < 7000; i++) {
        const p = new THREE.Vector3(gauss(), gauss(), gauss()).multiplyScalar(18);
        stars.add(p, tint(COLORS.diskOld, 0.05), 1.0, 0.06 + rand() * 0.12);
    }

    return { stars, gas, dust, knots };
}

function buildBackdropStars() {
    const layer = new Layer(15000);
    for (let i = 0; i < 15000; i++) {
        const p = new THREE.Vector3(gauss(), gauss(), gauss()).normalize().multiplyScalar(900);
        const pick = rand();
        const color = pick < 0.58 ? COLORS.white : pick < 0.84 ? COLORS.armBlue : COLORS.warm;
        layer.add(p, color, 1.0 + Math.pow(rand(), 4) * 2.0, 0.16 + Math.pow(rand(), 3) * 0.7);
    }
    return layer;
}

function glowSprite(color, size) {
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
    const material = new THREE.SpriteMaterial({
        map: new THREE.CanvasTexture(canvas),
        color,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
        transparent: true,
    });
    const sprite = new THREE.Sprite(material);
    sprite.scale.setScalar(size);
    return sprite;
}

/*
 * The artwork sits on black, so additive blending keys the background out for
 * free - no alpha channel needed. uFade dims it towards the edge of the plane and
 * uOpacity handles the layer toggle and the fades.
 */
function buildBackdrop(url, onLoad) {
    const texture = new THREE.TextureLoader().load(url, onLoad);
    texture.colorSpace = THREE.SRGBColorSpace;
    const material = new THREE.ShaderMaterial({
        uniforms: { uMap: { value: texture }, uOpacity: { value: BACKDROP.opacity } },
        vertexShader: /* glsl */ `
            varying vec2 vUv;
            void main() {
                vUv = uv;
                gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
            }
        `,
        fragmentShader: /* glsl */ `
            uniform sampler2D uMap;
            uniform float uOpacity;
            varying vec2 vUv;
            void main() {
                vec3 c = texture2D(uMap, vUv).rgb;
                float edge = 1.0 - smoothstep(0.42, 0.5, length(vUv - 0.5));
                gl_FragColor = vec4(c * uOpacity * edge, 1.0);
            }
        `,
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
        side: THREE.DoubleSide,
    });
    const mesh = new THREE.Mesh(new THREE.PlaneGeometry(BACKDROP.size, BACKDROP.size), material);
    mesh.rotation.x = -Math.PI / 2;
    mesh.rotation.z = BACKDROP.rotation;
    mesh.renderOrder = -1;
    return mesh;
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
        for (let i = 0; i <= 160; i++) {
            points.push(armPoint(phase, THREE.MathUtils.lerp(rMin, rMax, i / 160)));
        }
        const line = new THREE.Line(new THREE.BufferGeometry().setFromPoints(points), material);
        line.computeLineDistances();
        group.add(line);
    };
    for (const arm of ARMS) draw(armPhase(arm.crossing), 8.5, GALAXY_RADIUS);
    draw(armPhase(ORION_SPUR.crossing), ORION_SPUR.rMin, ORION_SPUR.rMax);
    return { group, material };
}

function buildDeepSky(objects) {
    const layers = { nebulae: new Layer(64), clusters: new Layer(64) };
    for (const o of objects) {
        const style = DEEP_SKY_STYLE[o.kind];
        layers[style.layer].add(o.position, new THREE.Color(style.color), style.size, 0.9);
    }
    const groups = {};
    for (const [key, layer] of Object.entries(layers)) {
        const material = pointsMaterial({ maxSize: 18, sharpness: 6, attenuate: 0 });
        const points = new THREE.Points(layer.geometry(), material);
        points.renderOrder = 8;
        points.frustumCulled = false;
        groups[key] = { points, material };
    }
    return groups;
}

/* ---------- local neighbourhood ---------- */

function buildLocal(systems) {
    const group = new THREE.Group();
    const lineMaterial = new THREE.LineBasicMaterial({ color: 0x9ecbff, transparent: true, opacity: 0.35, depthWrite: false });

    for (const ly of LOCAL_RINGS_LY) {
        const r = LOCAL_LOG_SCALE * Math.log10(1 + ly);
        const pts = [];
        for (let i = 0; i <= 128; i++) {
            const a = (i / 128) * Math.PI * 2;
            pts.push(new THREE.Vector3(SUN.x + r * Math.cos(a), SUN.y, SUN.z + r * Math.sin(a)));
        }
        group.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), lineMaterial));
    }

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

    return { group, materials: [lineMaterial], dotMaterial };
}

/* ---------- labels ---------- */

class Marker {
    constructor({ position, name, sub = "", level, layer = "systems", maxDistance = Infinity, kind = "link", href = null, color = null, fictional = false, onClick = null, priority = null }) {
        this.position = position;
        this.level = level;
        this.layer = layer;
        this.maxDistance = maxDistance;
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
        this.el.style.transform = this.centered
            ? `translate(${this.screenX}px, ${this.screenY}px) translate(-50%, -50%)`
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
        this.running = false;
        this.flight = null;
        this.lastInteraction = 0;
        this.layerState = {};

        this.renderer = new THREE.WebGLRenderer({ canvas: this.canvas, antialias: false, powerPreference: "high-performance" });
        this.renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        this.renderer.setClearColor(0x000000, 1);

        this.scene = new THREE.Scene();
        this.camera = new THREE.PerspectiveCamera(50, 1, 0.01, 5000);

        this.controls = new OrbitControls(this.camera, this.canvas);
        this.controls.enableDamping = true;
        this.controls.dampingFactor = 0.08;
        this.controls.minDistance = 0.8;
        this.controls.maxDistance = 180;
        this.controls.maxPolarAngle = THREE.MathUtils.degToRad(84);
        this.controls.screenSpacePanning = false;
        this.controls.zoomSpeed = 1.2;
        this.controls.autoRotate = true;
        this.controls.autoRotateSpeed = 0.2;
        this.controls.addEventListener("start", () => {
            this.flight = null;
            this.controls.autoRotate = false;
            this.lastInteraction = performance.now();
        });

        this.buildScene();
        this.buildMarkers();
        this.bindControls();
        this.bindLayers();
        this.placeCamera(OVERVIEW);

        window.addEventListener("resize", () => this.resize());
        this.resize();
    }

    buildScene() {
        const galaxy = buildGalaxy();
        this.materials = {
            stars: pointsMaterial({ maxSize: 3.2, nearFade: 0.08, sharpness: 18 }),
            gas: pointsMaterial({ maxSize: 900, nearFade: 3.5, sharpness: 2.5 }),
            dust: pointsMaterial({ maxSize: 700, nearFade: 3.0, sharpness: 2.5, blending: THREE.NormalBlending }),
            knots: pointsMaterial({ maxSize: 12, nearFade: 0.6, sharpness: 9 }),
            backdropStars: pointsMaterial({ maxSize: 4, sharpness: 18, attenuate: 0 }),
        };
        const add = (layer, material, order) => {
            const points = new THREE.Points(layer.geometry(), material);
            points.renderOrder = order;
            points.frustumCulled = false;
            this.scene.add(points);
        };
        add(buildBackdropStars(), this.materials.backdropStars, 0);
        add(galaxy.gas, this.materials.gas, 1);
        add(galaxy.stars, this.materials.stars, 2);
        add(galaxy.dust, this.materials.dust, 3);
        add(galaxy.knots, this.materials.knots, 4);

        this.backdrop = buildBackdrop(this.root.dataset.backdrop, () => {
            this.backdropReady = true;
        });
        this.scene.add(this.backdrop);

        this.coreGlow = glowSprite(new THREE.Color(0.55, 0.42, 0.28), 26);
        this.coreGlow.renderOrder = 5;
        this.scene.add(this.coreGlow);
        this.sunGlow = glowSprite(new THREE.Color(0.62, 0.8, 1.0), 1.4);
        this.sunGlow.position.copy(SUN);
        this.sunGlow.renderOrder = 6;
        this.scene.add(this.sunGlow);

        this.arms = buildArmOutlines();
        this.scene.add(this.arms.group);

        this.deepSky = (DATA.deepSky || []).map((o) => ({ ...o, position: truePosition(o.l, o.b, o.d) }));
        this.deepSkyGroups = buildDeepSky(this.deepSky);
        for (const group of Object.values(this.deepSkyGroups)) this.scene.add(group.points);

        this.localSystems = DATA.systems
            .filter((s) => !s.placement.fictional && s.placement.d > 0)
            .map((s) => ({ ...s, position: localPosition(s.placement) }));
        this.local = buildLocal(this.localSystems);
        this.local.group.renderOrder = 7;
        this.scene.add(this.local.group);
    }

    buildMarkers() {
        this.markers = [];
        const add = (options) => {
            const marker = new Marker(options);
            this.labels.appendChild(marker.el);
            this.markers.push(marker);
        };

        for (const arm of ARMS) {
            const phase = armPhase(arm.crossing);
            add({ position: armPoint(phase, arm.label), name: arm.name, level: "galaxy", layer: "arms", kind: "region" });
            if (arm.outerLabel) add({ position: armPoint(phase, 41), name: arm.outerLabel, level: "galaxy", layer: "arms", kind: "region" });
        }
        add({ position: armPoint(armPhase(ORION_SPUR.crossing), 29.5).add(new THREE.Vector3(2.5, 0, 0)), name: ORION_SPUR.name, level: "galaxy", layer: "arms", kind: "region" });
        add({ position: new THREE.Vector3(0, 0, 0), name: "Galactic Centre · Sgr A*", level: "galaxy", layer: "arms", kind: "region", priority: 0.5 });

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
            add({ position: SUN, name: "Sun", sub: "Solar System · you are here", level: "local", href: sun.href, color: sun.color });
        }
        for (const s of this.localSystems) {
            add({ position: s.position, name: s.name, sub: formatLy(s.placement.d), level: "local", href: s.href, color: s.color });
        }
        for (const s of DATA.systems.filter((s) => s.placement.fictional)) {
            const position = new THREE.Vector3(s.placement.x / 1000, 0, s.placement.z / 1000);
            add({ position, name: s.name, sub: `Fictional · ${s.placement.source}`, level: "galaxy", href: s.href, color: s.color, fictional: true });
        }
        for (const o of this.deepSky) {
            const style = DEEP_SKY_STYLE[o.kind];
            add({
                position: o.position,
                name: o.name,
                sub: `${o.alias} · ${style.label} · ${formatLy(o.d)}`,
                level: "galaxy",
                layer: style.layer,
                maxDistance: DEEP_SKY_LABEL_DISTANCE,
                kind: "region",
            });
        }
        for (const ly of LOCAL_RINGS_LY) {
            const r = LOCAL_LOG_SCALE * Math.log10(1 + ly);
            add({ position: SUN.clone().add(new THREE.Vector3(0, 0, -r)), name: formatLy(ly), level: "local", kind: "ring" });
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

    bindLayers() {
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
            toSph: new THREE.Spherical(distance, polar ?? from.phi, azimuth ?? from.theta),
        };
        this.controls.autoRotate = false;
        this.lastInteraction = performance.now();
    }

    flyToSun() {
        this.flyTo({ target: SUN, distance: 3.4, polar: 1.0 });
    }

    zoomBy(factor) {
        const s = this.spherical();
        const distance = THREE.MathUtils.clamp(s.radius * factor, this.controls.minDistance, this.controls.maxDistance);
        this.flyTo({ target: this.controls.target.clone(), distance }, 600);
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
        const materials = [...Object.values(this.materials), this.local.dotMaterial,
            ...Object.values(this.deepSkyGroups).map((g) => g.material)];
        for (const m of materials) m.uniforms.uScale.value = scale;
        this.iconHalf = Math.min(width, height) * 0.0055;
        // label boxes are sized in vmin, so they change with the viewport
        for (const marker of this.markers || []) {
            marker.width = 0;
            marker.height = 0;
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
        if (target.length() > GALAXY_RADIUS * 1.1) target.setLength(GALAXY_RADIUS * 1.1);
        target.y = THREE.MathUtils.clamp(target.y, -3, 3);

        const cameraDistance = this.spherical().radius;
        const sunDistance = this.camera.position.distanceTo(SUN);
        const local = 1 - smoothstep(LOCAL_FULL, LOCAL_ENTER, sunDistance);

        this.local.group.visible = local > 0.01 && this.layerState.systems !== false;
        for (const m of this.local.materials) m.opacity = 0.35 * local;
        this.local.dotMaterial.uniforms.uOpacity.value = local;
        this.materials.gas.uniforms.uOpacity.value = 1 - 0.6 * local;
        this.sunGlow.material.opacity = (1 - local) * (this.layerState.systems === false ? 0.35 : 1);

        // the backdrop is a flat plane, so fade it out when seen edge-on or up close
        const elevation = Math.abs(this.camera.position.y - target.y) / Math.max(cameraDistance, 0.001);
        this.backdrop.visible = this.layerState.backdrop !== false;
        this.backdrop.material.uniforms.uOpacity.value =
            BACKDROP.opacity * (1 - local) * smoothstep(0.12, 0.4, elevation);

        this.arms.group.visible = this.layerState.arms !== false && local < 0.99;
        this.arms.material.opacity = 0.22 * (1 - local);
        for (const [key, group] of Object.entries(this.deepSkyGroups)) {
            group.points.visible = this.layerState[key] !== false && local < 0.99;
            group.material.uniforms.uOpacity.value = 1 - local;
        }
        this.scaleNote.classList.toggle("Visible", local > 0.5);

        const candidates = [];
        for (const marker of this.markers) {
            const levelMatches = marker.level === "local" ? local > 0.5 : local < 0.5;
            const layerOn = this.layerState[marker.layer] !== false;
            if (marker.project(this.camera, this.width, this.height, levelMatches && layerOn, cameraDistance)) {
                candidates.push(marker);
            }
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
