function onLoadAny() {
    objClicked("SYSTEM_INFO");
    let sliders = document.querySelectorAll(".Slider");
    let slidersIdList = []
    sliders.forEach((slider) => {
        if (!slidersIdList.includes(slider.id)) {
            slidersIdList.push(slider.id);
        }
    })
    slidersIdList.forEach((slider) => {
        showSlides(1, slider);
    })
}

function onHoverEnter(id, color) {
    let object = document.getElementById(id);
    object.style.textShadow = color + ' 1px 1px 7px';
    object.style.color = color;
    object.style.paddingLeft = "1.5%"
    object.style.fontSize = "4.5vmin";
}

function onHoverLeave(id) {
    let object = document.getElementById(id);
    object.style.textShadow = "#000 0px 0px 0px";
    object.style.color = "#aaa";
    object.style.paddingLeft = "0%";
    object.style.fontSize = "3.5vmin";
}

function onHoverEnterButton(id, fore_color, back_color) {

}

function onHoverLeaveButton(id, fore_color, back_color) {

}

function objClicked(idToReveal) {
    hideAllObjects();
    let object = document.getElementById(idToReveal);
    object.style.textIndent = '0';
    object.style.top = '0';
}

function hideAllObjects() {
    let leftPanels = document.querySelectorAll(".LeftPanel");
    leftPanels.forEach((panel) => {
        panel.style.textIndent = '-1000em';
        panel.style.top = '200vh';
        panel.scrollTop = '0';
    })
}

function openSidepanel() {
    document.getElementById("STAR_SIDEPANEL").style.width = "16%";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "17%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "52%";
    right_side.style.width = "48%";
}
function closeSidepanel() {
    document.getElementById("STAR_SIDEPANEL").style.width = "0";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "6%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "43%";
    right_side.style.width = "57%";
}
function openSystempanel() {
    document.getElementById("UNIVERSE_SIDEPANEL").style.width = "16%";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "17%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "52%";
    right_side.style.width = "48%";
}
function closeSystempanel() {
    document.getElementById("UNIVERSE_SIDEPANEL").style.width = "0";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "6%");
    let right_side = document.querySelector(".star-system");
    right_side.style.left = "43%";
    right_side.style.width = "57%";
}

function movePanel(panels, percent) {
    panels.forEach((item) => {
        item.style.left = percent;
    })
}