let slideIndex = 1;
showSlides(slideIndex, 'alphaSlide');
showSlides(slideIndex, 'proxSlide');

function onLoadTrebia() {
    objClicked('systemInfo');
}

function plusSlides(n, name) {
    showSlides(slideIndex += n, name);
}
function currentSlide(n, name) {
    showSlides(n, name);
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
    document.getElementById(revealName).style.textIndent = '0';
    document.getElementById(revealName).style.top = '0';
}

function hideAllInfo() {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.textIndent = '-1000em';
        item.style.top = '200vh';
        item.scrollTop = '0';
    })
}

function openSidepanel() {
    document.getElementById("solarSidepanel").style.width = "16%";
    movePanel("20%");
    document.querySelector(".star-system").style.left = "57%";
    document.querySelector(".star-system").style.width = "40%";
}
function closeSidepanel() {
    document.getElementById("solarSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "46%";
    document.querySelector(".star-system").style.width = "54%";
}
function openSystempanel() {
    document.getElementById("starSidepanel").style.width = "16%";
    movePanel("20%");
    document.querySelector(".star-system").style.left = "57%";
    document.querySelector(".star-system").style.width = "40%";
}
function closeSystempanel() {
    document.getElementById("starSidepanel").style.width = "0";
    movePanel("10%");
    document.querySelector(".star-system").style.left = "46%";
    document.querySelector(".star-system").style.width = "54%";
}

function movePanel(percent) {
    let panels = document.querySelectorAll(".left-panel")
    panels.forEach((item) => {
        item.style.left = percent;
    })
}
