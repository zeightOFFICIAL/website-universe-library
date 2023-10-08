var i = 0,
    n = 1,
    x = 0,
    y = 0,
    h = 0,
    w = 0,
    r = 0,
    f = 1,
    blur = 0,
    rotation = 65,
    starDirection = 0,
    star, starAlpha, starsBig = [],
    starsSmall = [],
    inProgress = 0,
    canvas = document.getElementById("SPACE_CANVAS"),
    ctx, varTop, varLeft, tenth, mousePos = {
        xPos: 0,
        yPos: 0
    },
    rng = 0,
    BGrng = 0,
    oldColor = [21, 71, 67],
    newColor = [21, 71, 67],
    colorStep = [0, 0, 0],
    colorDiff = [0, 0, 0],
    colorDisplay = [0, 0, 0],
    spaceColors = new Array(),
    nebula = new Array(),
    sparity = 1500;

//setup
nebula.push("1.jpg");
nebula.push("2.jpg");
nebula.push("3.jpg");
nebula.push("4.jpg");
nebula.push("5.jpg");
var nebula_choice = nebula[Math.floor(Math.random() * nebula.length)];
canvas.height = window.innerHeight / 2;
canvas.width = window.innerWidth + 100;
ctx = canvas.getContext("2d");
h = canvas.height;
w = canvas.width;

ctx.fillStyle = "white";
ctx.strokeStyle = "white";

spaceColors[0] = new Array(21, 71, 67);
spaceColors[1] = new Array(76, 0, 1);
spaceColors[2] = new Array(48, 43, 99);
spaceColors[3] = new Array(83, 52, 109);
spaceColors[4] = new Array(102, 102, 0);

//star properties
function Star(xPos, yPos, alpha) {
    this.xPos = xPos;
    this.yPos = yPos;
    this.alpha = alpha;
}

// to create stars
function populate(x, y) {
    r = Math.floor((Math.random() * sparity) + 1);
    if (r == sparity) {
        if (Math.floor(Math.random() * 10) <= 1) {
            starAlpha = .7 + Math.random() * .3;
            star = new Star(x, y, starAlpha);
            starsBig.push(star);
        } else {
            starAlpha = .5 + Math.random() * .3;
            star = new Star(x, y, starAlpha);
            starsSmall.push(star);
        }
    }
}

// draw stars
function draw() {
    if (blur === 1) {
        ctx.clearRect(0, 0, w, h);
        blur = 0;
    } else {
        blur = 1;
    }
    for (i = 0; i < starsBig.length; i++) {
        x = starsBig[i].xPos;
        y = starsBig[i].yPos;
        ctx.globalAlpha = starsBig[i].alpha;
        ctx.beginPath();
        ctx.ellipse(x, y, 2, 2 * n, rotation * Math.PI / 180, 0, 2 * Math.PI);
        ctx.fill();
    }
    for (i = 0; i < starsSmall.length; i++) {
        x = starsSmall[i].xPos;
        y = starsSmall[i].yPos;
        ctx.globalAlpha = starsSmall[i].alpha;
        ctx.beginPath();
        ctx.ellipse(x, y, 1, 1 * n, rotation * Math.PI / 180, 0, 2 * Math.PI);
        ctx.fill();
    }
}

// moves stars
function moveStars() {
    var xDir, yDir
    switch (starDirection) {
        case 0:
            xDir = -1;
            yDir = 1;
            rotation = -64;
            break;
        case 1:
            xDir = 1;
            yDir = 1;
            rotation = 64;
            break;
        case 2:
            xDir = 1;
            yDir = -1;
            rotation = -64;
            break;
        case 3:
            xDir = -1;
            yDir = -1;
            rotation = 64;
            break;
    }
    // move
    for (i = 0; i < starsBig.length; i++) {
        starsBig[i].xPos += ((-2 * xDir) / 20) * n;
        starsBig[i].yPos += ((1 * yDir) / 20) * n;
    }
    for (i = 0; i < starsSmall.length; i++) {
        starsSmall[i].xPos += ((-1 * xDir) / 30) * n;
        starsSmall[i].yPos += ((0.5 * yDir) / 30) * n;
    }
    // wrap
    for (i = 0; i < starsBig.length; i++) {
        if (starsBig[i].xPos <= 0) {
            starsBig[i].xPos = w + starsBig[i].xPos;
        } else if (starsBig[i].xPos >= w) {
            starsBig[i].xPos = starsBig[i].xPos - w;
        }
        if (starsBig[i].yPos <= 0) {
            starsBig[i].yPos = h + starsBig[i].yPos;
        } else if (starsBig[i].yPos >= h) {
            starsBig[i].yPos = starsBig[i].yPos - h;
        }
    }
    for (i = 0; i < starsSmall.length; i++) {
        if (starsSmall[i].xPos <= 0) {
            starsSmall[i].xPos = w + starsSmall[i].xPos;
        } else if (starsSmall[i].xPos >= w) {
            starsSmall[i].xPos = starsSmall[i].xPos - w;
        }
        if (starsSmall[i].yPos <= 0) {
            starsSmall[i].yPos = h + starsSmall[i].yPos;
        } else if (starsSmall[i].yPos >= h) {
            starsSmall[i].yPos = starsSmall[i].yPos - h;
        }
    }
}

// animation controller
function starfield() {
    draw();
    moveStars();
    window.requestAnimationFrame(starfield);
}

// generate beginning stars
function generate() {
    starsBig = [];
    starsSmall = [];
    for (x = 0; x < w; x++) {
        for (y = 0; y < h; y++) {
            populate(x, y);
        }
    }
    canvas.style.background = "url('../static/Images/BackNav/" + nebula_choice + "') center";
}

// engage
function engage() {
    if (inProgress === 0) {
        inProgress = 1;
        oldColor.length = 0;
        oldColor.push.apply(oldColor, newColor);
        rng = Math.floor(Math.random() * spaceColors.length);
        newColor.length = 0;
        newColor.push.apply(newColor, spaceColors[rng]);
        colorStep.length = 0;
        colorStep.push.apply(colorStep, oldColor);
        starDirection = Math.round(Math.random() * 3);
        var engageTrans = setInterval(function () {
            if (f == 1) {
                n = n * 2;
            } else {
                n = n / 2;
            }
            for (i = 0; i < starsBig.length; i++) {
                starsBig[i].alpha = 1;
            }
            for (i = 0; i < starsSmall.length; i++) {
                starsSmall[i].alpha = .5;
            }
            for (i = 0; i < 3; i++) {
                colorDiff[i] = oldColor[i] - newColor[i];
                colorStep[i] = colorStep[i] - colorDiff[i] / 20;
                colorDisplay[i] = Math.ceil(colorStep[i]);
            }
            document.body.style.background = "linear-gradient(to top, #000000, rgb(" + colorDisplay + ")";
        }, 50);
        window.setTimeout(function () {
            generate();
            f = 0;
        }, 500);
        window.setTimeout(function () {
            clearInterval(engageTrans);
            document.body.style.background = "linear-gradient(to top, #000000, rgb(" + newColor + ")";
            n = 1;
            f = 1;
            inProgress = 0;
            for (i = 0; i < starsBig.length; i++) {
                starsBig[i].alpha = .5 + Math.random() * .5;
            }
            for (i = 0; i < starsSmall.length; i++) {
                starsSmall[i].alpha = .3 + Math.random() * .5;
            }
        }, 1000);
    }
}

generate();
window.requestAnimationFrame(starfield);

window.addEventListener("resize", function () {
    canvas.height = window.innerHeight / 2;
    canvas.width = window.innerWidth + 100;
    ctx = canvas.getContext("2d");
    h = canvas.height;
    w = canvas.width;
    ctx.fillStyle = "white";
    ctx.strokeStyle = "white";
    if (this.window.innerWidth > 2000) {
        sparity = 10000;
    }
    else {
        sparity = 1500;
    }
    generate();
});


function navPanelEnter() {
    var nav = document.getElementById("NAV_PANEL");
    var btn = document.getElementById("BACK_BUTTON");
    var btn2 = document.getElementById("ARTC_BUTTON");
    var btn3 = document.getElementById("CALC_BUTTON");
    var btn4 = document.getElementById("OBJS_BUTTON");
    var btn5 = document.getElementById("SPAC_BUTTON");
    nav.style.height = "25%";
    nav.style.filter = "brightness(40%)";

    btn.style.top = "0%";
    btn.style.animation = "spin 1s";
    btn2.style.top = "0";

    btn2.style.left = "28%";
    btn2.style.width = "15%";

    btn3.style.top = "0";
    btn3.style.left = "57%";
    btn3.style.width = "15%";

    btn4.style.top = "0";
    btn4.style.left = "13%";
    btn4.style.width = "15%";

    btn5.style.top = "0";
    btn5.style.left = "72%";
    btn5.style.width = "15%";
}

function navPanelLeave() {
    var nav = document.getElementById("NAV_PANEL");
    var btn = document.getElementById("BACK_BUTTON");
    var btn2 = document.getElementById("ARTC_BUTTON");
    var btn3 = document.getElementById("CALC_BUTTON");
    var btn4 = document.getElementById("OBJS_BUTTON");
    var btn5 = document.getElementById("SPAC_BUTTON");
    nav.style.height = "8%";
    nav.style.filter = "brightness(100%)";
    btn.style.top = "-100%";
    btn.style.animation = "spin_back 1s"

    btn2.style.top = "-100%";
    btn2.style.left = "50%";
    btn2.style.width = "0";

    btn3.style.top = "-100%";
    btn3.style.left = "50%";
    btn3.style.width = "0";

    btn4.style.top = "-100%";
    btn4.style.left = "50%";
    btn4.style.width = "0";

    btn5.style.top = "-100%";
    btn5.style.left = "50%";
    btn5.style.width = "0";
}