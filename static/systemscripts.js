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
    document.getElementById("solarSidepanel").style.width = "17%";
    movePanel("18%");
    document.querySelector(".star-system").style.left = "48%";
    document.querySelector(".star-system").style.width = "52%";
}
function closeSidepanel() {
    document.getElementById("solarSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "41%";
    document.querySelector(".star-system").style.width = "59%";
}
function openSystempanel() {
    document.getElementById("starSidepanel").style.width = "17%";
    movePanel("18%");
    document.querySelector(".star-system").style.left = "48%";
    document.querySelector(".star-system").style.width = "52%";
}
function closeSystempanel() {
    document.getElementById("starSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "41%";
    document.querySelector(".star-system").style.width = "59%";
}

function movePanel(percent) {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.left = percent;
    })
}
