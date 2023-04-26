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
function objClicked(idToReveal) {
    hideAllObjects();
    let object = document.getElementById(idToReveal);
    object.style.textIndent = '0';
    object.style.top = '0';

    if (idToReveal != "SYSTEM_INFO") {
        idToHover = idToReveal.split("_")[0] + "_OBJ";
        console.log(idToHover);
        onHoverEnterAddClass(idToHover, "HoveredObjectForced");
    }
}

function onHoverEnterAddClass(id, className) {
    document.getElementById(id).classList.add(className);
}

function onHoverLeaveRemoveClass(id, className) {
    document.getElementById(id).classList.remove(className);
}

function onHoverLeaveForced() {
    let firstObject = document.getElementById("UNIV_CLOSEBUTTON");
    let secondObject = document.getElementById("STAR_CLOSEBUTTON");
    firstObject.classList.remove("HoveredBorderButton");
    secondObject.classList.remove("HoveredBorderButton");
}

function onHoverSidepanelTitle(id, color) {
    let object = document.getElementById(id);
    object.style.color = color;
    object.style.textShadow = `${color} 1px 1px 10px`;
    object.style.paddingLeft = "1.5%";
    object.style.fontSize = "4.5vmin";
    let idObjToHover = id.split("_")[0] + "_OBJ";
    onHoverEnterAddClass(idObjToHover, "HoveredObject");
}

function onHoverSidepanelTitleLeave(id) {
    let object = document.getElementById(id);
    object.style.color = "#aaa";
    object.style.textShadow = `#000 0px 0px 0px`;
    object.style.paddingLeft = "0%";
    object.style.fontSize = "3.5vmin";
    let idObjToHover = id.split("_")[0] + "_OBJ";
    onHoverLeaveRemoveClass(idObjToHover, "HoveredObject");
}

function hideAllObjects() {
    let leftPanels = document.querySelectorAll(".LeftPanel");
    leftPanels.forEach((panel) => {
        panel.style.textIndent = '-1000em';
        panel.style.top = '200vh';
        panel.scrollTop = '0';
    })
    let objects = document.querySelectorAll(".Object");
    objects.forEach((obj) => {
        obj.classList.remove("HoveredObjectForced");
    })
}

function openSidepanel() {
    document.getElementById("STAR_SIDEPANEL").style.width = "16%";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "17%");
    let right_side = document.querySelector(".StarSystem");
    right_side.style.left = "52%";
    right_side.style.width = "48%";
}
function closeSidepanel() {
    document.getElementById("STAR_SIDEPANEL").style.width = "0";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "6%");
    let right_side = document.querySelector(".StarSystem");
    right_side.style.left = "43%";
    right_side.style.width = "57%";
}
function openSystempanel() {
    document.getElementById("UNIVERSE_SIDEPANEL").style.width = "16%";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "17%");
    let right_side = document.querySelector(".StarSystem");
    right_side.style.left = "52%";
    right_side.style.width = "48%";
}
function closeSystempanel() {
    document.getElementById("UNIVERSE_SIDEPANEL").style.width = "0";
    let left_side = document.querySelectorAll(".LeftPanel");
    movePanel(left_side, "6%");
    let right_side = document.querySelector(".StarSystem");
    right_side.style.left = "43%";
    right_side.style.width = "57%";
}

function movePanel(panels, percent) {
    panels.forEach((item) => {
        item.style.left = percent;
    })
}