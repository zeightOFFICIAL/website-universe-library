function objClicked(idToReveal) {
    hideAllObjects();
    let object = document.getElementById(idToReveal);
    object.style.textIndent = '0';
    object.style.top = '0';
}

function hideAllObjects() {
    let leftPanels = document.querySelectorAll(".LeftPanel")
    leftPanels.forEach((panel) => {
        panel.style.textIndent = '-1000em';
        panel.style.top = '200vh';
        panel.scrollTop = '0';
    })
}

function openSidepanel() {
    document.getElementById("STAR_SIDEPANEL").style.width = "16%";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "20%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "46%";
    right_side.style.width = "54%";
}
function closeSidepanel() {
    document.getElementById("STAR_SIDEPANEL").style.width = "0";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "10%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "40%";
    right_side.style.width = "57%";
}
function openSystempanel() {
    document.getElementById("UNIVERSE_SIDEPANEL").style.width = "16%";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "20%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "46%";
    right_side.style.width = "54%";
}
function closeSystempanel() {
    document.getElementById("UNIVERSE_SIDEPANEL").style.width = "0";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "10%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "40%";
    right_side.style.width = "57%";
}

function movePanel(panels, percent) {
    panels.forEach((item) => {
        item.style.left = percent;
    })
}