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
showSlides(slideIndex, "sunSlide");
showSlides(slideIndex, "earthSlide");
showSlides(slideIndex, "marsSlide");
showSlides(slideIndex, "venusSlide");
showSlides(slideIndex, "mercurySlide");
showSlides(slideIndex, "saturnSlide");
showSlides(slideIndex, "jupiterSlide");
showSlides(slideIndex, "neptuneSlide");
showSlides(slideIndex, "uranusSlide");
showSlides(slideIndex, "moonSlide");
showSlides(slideIndex, "phobosSlide");
showSlides(slideIndex, "asteroidSlide");

function plusSlides(n, name) {
    showSlides(slideIndex += n, name);
}

function currentSlide(n, name) {
    showSlides(slideIndex = n, name);
}

function showSlides(n, name) {
    let i;
    let slides = document.getElementsByClassName(name);
    if (n > slides.length) { slideIndex = 1 }
    if (n < 1) { slideIndex = slides.length }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slides[slideIndex - 1].style.display = "block";
}

function objClicked(revealName) {
    hideAllInfo();
    document.getElementById(revealName).style.display = 'block';
}

function hideAllInfo() {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.display = 'none';
    })
}

function openSidepanel() {
    document.getElementById("solarSidepanel").style.width = "17%";
    movePanel("18%");
    document.querySelector(".star-system").style.left = "48%";
    document.querySelector(".star-system").style.width = "52%";
}
function closeSidepanel() {
    document.getElementById("solarSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "41%";
    document.querySelector(".star-system").style.width = "59%";
}
function openSystempanel() {
    document.getElementById("starSidepanel").style.width = "17%";
    movePanel("18%");
    document.querySelector(".star-system").style.left = "48%";
    document.querySelector(".star-system").style.width = "52%";
}
function closeSystempanel() {
    document.getElementById("starSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "41%";
    document.querySelector(".star-system").style.width = "59%";
}

function movePanel(percent) {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.left = percent;
    })
}
