let slideIndex = 1

function showSlides(index, name) {
    let i;
    let slides = document.querySelectorAll("#" + name);
    if (index > slides.length) { slideIndex = 1 }
    if (index < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

function plusSlides(n, name) {
    showSlides(slideIndex += n, name);
}
function currentSlide(n, name) {
    showSlides(n, name);
}