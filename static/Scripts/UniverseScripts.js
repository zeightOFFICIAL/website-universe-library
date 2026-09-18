var swiper = new Swiper(".swiper", {
    effect: "cards",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 2,
    cardsEffect: {
        perSlideOffset: 45,
        perSlideRotate: 14,
        rotate: true,
        modifier: 1,
        slideShadows: false
    },
    keyboard: {
        enabled: true,
        pageUpDown: true
    },
    mousewheel: {
        thresholdDelta: 35,
        thresholdTime: 0,
        sensitivity: 200
    },
    pagination: {
        el: ".swiper-pagination",
        clickable: true,
        dynamicBullets: true,
        dynamicMainBullets: 10
    },
});


function setMainView(view) {
    const isGalaxy = view === "galaxy";
    document.body.classList.toggle("ViewGalaxy", isGalaxy);
    document.getElementById("GALAXY_VIEW").setAttribute("aria-hidden", String(!isGalaxy));
    document.querySelectorAll(".ViewSwitchButton").forEach((button) => {
        button.classList.toggle("ViewSwitchActive", button.dataset.view === view);
    });
    if (isGalaxy) {
        swiper.keyboard.disable();
        swiper.mousewheel.disable();
    } else {
        swiper.keyboard.enable();
        swiper.mousewheel.enable();
    }
    try {
        localStorage.setItem("mainView", view);
    } catch (e) {}
    document.dispatchEvent(new CustomEvent("mainview", { detail: view }));
}

document.querySelectorAll(".ViewSwitchButton").forEach((button) => {
    button.addEventListener("click", () => setMainView(button.dataset.view));
});

let savedView = "cards";
try {
    savedView = localStorage.getItem("mainView") || "cards";
} catch (e) {}
setMainView(savedView);
