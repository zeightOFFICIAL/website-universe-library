var swiper = new Swiper(".swiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 2,
    autoplay: {
        delay: 7500,
    },
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 2,
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
    spaceBetween: 0,
    loop: true,
});
