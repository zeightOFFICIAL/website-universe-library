function onLoadSolar() {
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('venus-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('mercury-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('earth-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('saturn-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('jupiter-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('uranus-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('neptune-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('mars-spin').style.animationDelay = "-" + randomShift + "s";
    objClicked("systemInfo");
}

function objClicked(revealName) {
    hideAllInfo();
    document.getElementById(revealName).style.textIndent = '0';
}

function hideAllInfo() {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.textIndent = '-1000em';
    })
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
