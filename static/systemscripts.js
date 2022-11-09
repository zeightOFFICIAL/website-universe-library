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

function sunClicked() {
    hideAllInfo();
    document.getElementById("sunInfo").style.display = 'block';
}

function earthClicked() {
    hideAllInfo();
    document.getElementById("earthInfo").style.display = 'block';
}

function marsClicked() {
    hideAllInfo();
    document.getElementById("marsInfo").style.display = 'block';
}

function venusClicked() {
    hideAllInfo();
    document.getElementById("venusInfo").style.display = 'block';
}

function mercuryClicked() {
    hideAllInfo();
    document.getElementById("mercuryInfo").style.display = 'block';
}

function saturnClicked() {
    hideAllInfo();
    document.getElementById("saturnInfo").style.display = "block";
}

function jupiterClicked() {
    hideAllInfo();
    document.getElementById("jupiterInfo").style.display = "block";
}

function neptuneClicked() {
    hideAllInfo();
    document.getElementById("neptuneInfo").style.display = 'block';
}

function uranusClicked() {
    hideAllInfo();
    document.getElementById("uranusInfo").style.display = 'block';
}

function closeInfo() {
    hideAllInfo();
    document.getElementById("systemInfo").style.display = 'block';
}

function moonClicked() {
    hideAllInfo();
    document.getElementById("moonInfo").style.display = 'block';
}

function phobosClicked() {
    hideAllInfo();
    document.getElementById("phobosInfo").style.display = 'block';
}

function hideAllInfo() {
    document.getElementById("systemInfo").style.display = 'none';
    document.getElementById("earthInfo").style.display = 'none';
    document.getElementById("sunInfo").style.display = 'none';
    document.getElementById("marsInfo").style.display = 'none';
    document.getElementById("venusInfo").style.display = 'none';
    document.getElementById("mercuryInfo").style.display = 'none';
    document.getElementById("saturnInfo").style.display = 'none';
    document.getElementById("jupiterInfo").style.display = 'none';
    document.getElementById("neptuneInfo").style.display = 'none';
    document.getElementById("uranusInfo").style.display = 'none';
    document.getElementById("moonInfo").style.display = 'none';
    document.getElementById("phobosInfo").style.display = 'none';
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

function movePanel(percent) {
    let panels = document.querySelectorAll(".left-panel")
    console.log(panels)
    panels.forEach((item) => {
        item.style.left = percent;
        console.log(item);
    })
}