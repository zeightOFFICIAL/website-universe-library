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
        onHoverEnterAddClass(idToHover, "HoveredObjectForced");
    }
}

function onHoverEnterAddClass(id, className) {
    document.getElementById(id).classList.toggle(className);
}

function onHoverLeaveRemoveClass(id, className) {
    document.getElementById(id).classList.toggle(className);
}

function onHoverSidepanelTitle(id, color) {
    let object = document.getElementById(id);
    object.style.color = color;
    object.style.textShadow = `${color} .5vmin .5vmin 1vmin`;
    object.style.paddingLeft = "1.5%";
    object.style.fontSize = "4.5vmin";
    let idObjToHover = id.split("_")[0] + "_OBJ";
    onHoverEnterAddClass(idObjToHover, "HoveredObject");
}

function onHoverSidepanelTitleLeave(id) {
    let object = document.getElementById(id);
    object.style.color = "#aaa";
    object.style.textShadow = `#000 0 0 0`;
    object.style.paddingLeft = "0%";
    object.style.fontSize = "3.5vmin";
    let idObjToHover = id.split("_")[0] + "_OBJ";
    onHoverLeaveRemoveClass(idObjToHover, "HoveredObject");
}

function hideAllObjects() {
    let allAudio = document.querySelectorAll(".Audio");
    allAudio.forEach((audio) => {
        audio.pause();
    })
    let allVideo = document.querySelectorAll('iframe');
    allVideo.forEach((video) => {
        var temp = video.src;
        video.src = temp; 
    })
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
    if (document.getElementById("STAR_SIDEPANEL") == null) {
        return;
    }
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
    if (document.getElementById("UNIVERSE_SIDEPANEL") == null) {
        return;
    }
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