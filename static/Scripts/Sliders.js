let slideIndex = 1

function onLoadAny() {
    objClicked("SYSTEM_INFO")
}

function showSlides(index, name) {
    let index;
    let slides = document.getElementsByClassName(name);
    if (index > slides.length) { slideIndex = 1 }
    if (index < 1) { slideIndex = slides.length }
    for (index = 0; index < slides.length; index++) {
        slides[index].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

function plusSlides(n, name) {
    showSlides(slideIndex += n, name);
}
function currentSlide(n, name) {
    showSlides(n, name);
}