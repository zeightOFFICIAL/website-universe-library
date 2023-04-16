function objClicked(nameToReveal) {
    hideAllObjects();
    let object = document.querySelector(nameToReveal);
    object.style.textIndent = '0';
    object.style.top = '0';
}

function hideAllObjects() {
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
    document.querySelector("starSidepanel").style.width = "16%";
    let left_side = document.querySelectorAll(".left-panel");
    movePanel(left_side, "20%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "46%";
    right_side.style.width = "54%";
}
function closeSidepanel() {
    document.querySelector("starSidepanel").style.width = "0";
    let left_side = document.querySelectorAll(".left-panel");
    movePanel(left_side, "10%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "46%";
    right_side.style.width = "54%";
}
function openSystempanel() {
    document.querySelector("universePanel").style.width = "16%";
    let left_side = document.querySelectorAll(".left-panel");
    movePanel(left_side, "20%");
    document.querySelector(".star-system").style.left = "57%";
    document.querySelector(".star-system").style.width = "40%";
}
function closeSystempanel() {
    document.querySelector("universePanel").style.width = "0";
    movePanel("10%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "46%";
    right_side.style.width = "54%";
}

function movePanel(panels, percent) {
    panels.forEach((item) => {
        item.style.left = percent;
    })
}