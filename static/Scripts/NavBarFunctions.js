function navPanelEnter() {
    var nav = document.getElementById("NAV_PANEL");
    var btn = document.getElementsByClassName("CenterNavButton")[0];
    var btn2 = document.getElementsByClassName("LeftCloseNavButton")[0];
    var btn3 = document.getElementsByClassName("RightCloseNavButton")[0];
    var btn4 = document.getElementsByClassName("LeftFarNavButton")[0];
    var btn5 = document.getElementsByClassName("RightFarNavButton")[0];
    var other = document.getElementById("LOWER_PART");

    other.style.filter = "brightness(30%)";

    nav.style.height = "25%";
    nav.style.filter = "brightness(50%)";
    nav.style.boxShadow = "0 0 25vmin yellow";

    btn.style.top = "0%";
    btn.style.animation = "spin 1s";

    btn2.style.top = "0";
    btn2.style.left = "28%";
    btn2.style.width = "15%";

    btn3.style.top = "0";
    btn3.style.left = "57%";
    btn3.style.width = "15%";

    btn4.style.top = "0";
    btn4.style.left = "13%";
    btn4.style.width = "15%";

    btn5.style.top = "0";
    btn5.style.left = "72%";
    btn5.style.width = "15%";
}

function navPanelLeave() {
    var nav = document.getElementById("NAV_PANEL");
    var btn = document.getElementsByClassName("CenterNavButton")[0];
    var btn2 = document.getElementsByClassName("LeftCloseNavButton")[0];
    var btn3 = document.getElementsByClassName("RightCloseNavButton")[0];
    var btn4 = document.getElementsByClassName("LeftFarNavButton")[0];
    var btn5 = document.getElementsByClassName("RightFarNavButton")[0];
    var other = document.getElementById("LOWER_PART");

    other.style.filter = "brightness(100%)";

    nav.style.height = "4%";
    nav.style.filter = "brightness(100%)";
    nav.style.boxShadow = "0 0 5vmin white";

    btn.style.top = "-100%";
    btn.style.animation = "spin-back 1s"

    btn2.style.top = "-100%";
    btn2.style.left = "50%";
    btn2.style.width = "0";

    btn3.style.top = "-100%";
    btn3.style.left = "50%";
    btn3.style.width = "0";

    btn4.style.top = "-100%";
    btn4.style.left = "50%";
    btn4.style.width = "0";

    btn5.style.top = "-100%";
    btn5.style.left = "50%";
    btn5.style.width = "0";
}

function onMainButtonEnter() {
    var btn = document.getElementsByClassName("CenterNavButton")[0];

    btn.style.animation =  "spin-main .75s"
}