function onLoadSolar() {
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('venus-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('mercury-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('earth-spin').style.animationDelay = "-" + randomShift + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('saturn-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('jupiter-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('uranus-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('neptune-spin').style.animationDelay = "-" + randomShift * 1000 + "s";
    randomShift = Math.floor(Math.random() * 100);
    document.getElementById('mars-spin').style.animationDelay = "-" + randomShift + "s";
}

let slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
    showSlides(slideIndex += n);
}

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("allSlide");
    let dots = document.getElementsByClassName("demo");
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
}

var leftSide = document.getElementById("leftSide");

function sunClicked() {
    document.getElementById("systemInfo").style.display = 'none';
    document.getElementById("sunInfo").style.display = 'unset';
}

function closeInfo() {
    document.getElementById("systemInfo").style.display = 'unset';
    document.getElementById("sunInfo").style.display = 'none';
}