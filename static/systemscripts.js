
function onLoadSolar() {
    objClicked("systemInfo");
    randomShift = Math.floor(Math.random() * 23);
    document.getElementById('venus-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 9);
    document.getElementById('mercury-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 37);
    document.getElementById('earth-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 1076);
    document.getElementById('saturn-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 434);
    document.getElementById('jupiter-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 3069);
    document.getElementById('uranus-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 6001);
    document.getElementById('neptune-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 69);
    document.getElementById('mars-spin').style.animationDelay = "-" + randomShift + "s";
}

function onLoadAlpha() {
    objClicked("systemInfo");
    randomShift = Math.floor(Math.random() * 10);
    document.getElementById('alpha-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 45);
    document.getElementById('beta-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 325);
    document.getElementById('prox-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 1928);
    document.getElementById('proxc-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 11);
    document.getElementById('proxb-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 5);
    document.getElementById('proxd-spin').style.animationDelay = "-" + randomShift + "s";
}

function onLoadTrebia() {
    objClicked('systemInfo');
    randomShift = Math.floor(Math.random() * 6);
    document.getElementById('aventen-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 12);
    document.getElementById('caelax-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 40);
    document.getElementById('palaven-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 130);
    document.getElementById('impera-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 4300);
    document.getElementById('essenus-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 6700);
    document.getElementById('datriux-spin').style.animationDelay = "-" + randomShift + "s";
}

function onLoadTrapp() {
    objClicked('systemInfo');
    randomShift = Math.floor(Math.random() * 5);
    document.getElementById('trapb-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 8);
    document.getElementById('trapc-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 12);
    document.getElementById('trapd-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 18);
    document.getElementById('trape-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 27);
    document.getElementById('trapf-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 36);
    document.getElementById('trapg-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 65);
    document.getElementById('traph-spin').style.animationDelay = "-" + randomShift + "s";
}


function objClicked(revealName) {
    hideAllInfo();
    document.getElementById(revealName).style.textIndent = '0';
    document.getElementById(revealName).style.top = '0';
}

function hideAllInfo() {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.textIndent = '-1000em';
        item.style.top = '200vh';
        item.scrollTop = '0';
    })
    try {
        document.getElementById('video').contentWindow.postMessage('{"event":"command","func":"stopVideo","args":""}', '*');
    }
    catch (TypeError) {
        console.log("Video files were not found as this page.");
    }
    try {
        sound.pause();
        sound.currentTime = 0;
    }
    catch (TypeError) {
        console.log("Sound files were not found as this page.");
    }
}

function openSidepanel() {
    document.getElementById("solarSidepanel").style.width = "16%";
    movePanel("20%");
    document.querySelector(".star-system").style.left = "57%";
    document.querySelector(".star-system").style.width = "40%";
}
function closeSidepanel() {
    document.getElementById("solarSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "46%";
    document.querySelector(".star-system").style.width = "54%";
}
function openSystempanel() {
    document.getElementById("starSidepanel").style.width = "16%";
    movePanel("20%");
    document.querySelector(".star-system").style.left = "57%";
    document.querySelector(".star-system").style.width = "40%";
}
function closeSystempanel() {
    document.getElementById("starSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "46%";
    document.querySelector(".star-system").style.width = "54%";
}

function movePanel(percent) {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.left = percent;
    })
}
