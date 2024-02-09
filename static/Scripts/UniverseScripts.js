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
