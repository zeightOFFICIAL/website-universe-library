var values = [];
var selection = false;

function changeSelection() {
    var btn = document.getElementById("BUTTON_CALC");
    var btn2 = document.getElementById("BUTTON_CONV");
    var pnl = document.getElementById("LOWER_PART_CALC");
    var pnl2 = document.getElementById("LOWER_PART_CONV");

    if (selection === false) {
        selection = true;

        btn.style.backgroundColor = "white";
        btn.style.color = "white";
        btn.style.pointerEvents = "none";
        pnl.style.display = "block";

        btn2.style.backgroundColor = "black";
        btn2.style.color = "white";
        btn2.style.pointerEvents = "all";
        pnl2.style.display = "none";
    }
    else {
        selection = false;

        btn2.style.backgroundColor = "white";
        btn2.style.color = "white";
        btn2.style.pointerEvents = "none"; 
        pnl.style.display = "block";

        btn.style.backgroundColor = "black";
        btn.style.color = "white";
        btn.style.pointerEvents = "all";
        pnl.style.display = "none";
    }
}

function calculateEscapeVelocity() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass_EV').value);
    const massUnit = document.getElementById('massUnit_EV').value;
    var radius = parseFloat(document.getElementById('radius_EV').value);
    const radiusUnit = document.getElementById('radiusUnit_EV').value;

    if (isNaN(mass) || isNaN(radius) || mass <= 0 || radius <= 0) {
        document.getElementById('result_EV').value = "0";
        return;
    }

    switch (massUnit) {
        case 'kg':
            break;
        case 't':
            mass *= 1000;
            break;
        case 'M☉':
            mass *= 1.989e30;
            break;
        case 'M⊕':
            mass *= 5.972e24;
            break;
        default:
            alert('Invalid mass unit.');
            return;
    }

    switch (radiusUnit) {
        case 'm':
            break;
        case 'km':
            radius *= 1000;
            break;
        case 'R☉':
            radius *= 6.9634e8;
            break;
        case 'R⊕':
            radius *= 6.371e6;
            break;
        default:
            alert('Invalid radius unit.');
            return;
    }

    const escapeVelocity = Math.sqrt(2 * G * mass / radius);
    document.getElementById('result_EV').value = escapeVelocity.toFixed(10);

    document.getElementById('mass_EV').value = "0";
    document.getElementById('radius_EV').value = "0";
    values.push(escapeVelocity);
    updateValues();
}

function calculateFirstCosmicSpeed() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass_FCS').value);
    const massUnit = document.getElementById('massUnit_FCS').value;
    var radius = parseFloat(document.getElementById('radius_FCS').value);
    const radiusUnit = document.getElementById('radiusUnit_FCS').value;

    if (isNaN(mass) || isNaN(radius) || mass <= 0 || radius <= 0) {
        document.getElementById('result_FCS').value = "0";
        return;
    }

    switch (massUnit) {
        case 'kg':
            break;
        case 't':
            mass *= 1000;
            break;
        case 'M☉':
            mass *= 1.989e30;
            break;
        case 'M⊕':
            mass *= 5.972e24;
            break;
        default:
            alert('Invalid mass unit.');
            return;
    }

    switch (radiusUnit) {
        case 'm':
            break;
        case 'km':
            radius *= 1000;
            break;
        case 'R☉':
            radius *= 6.9634e8;
            break;
        case 'R⊕':
            radius *= 6.371e6;
            break;
        default:
            alert('Invalid radius unit.');
            return;
    }

    const firstCosmicSpeed = Math.sqrt(G * mass / radius);
    document.getElementById('result_FCS').value = firstCosmicSpeed.toFixed(10);
    document.getElementById('mass_FCS').value = "0";
    document.getElementById('radius_FCS').value = "0";
    values.push(firstCosmicSpeed);
    updateValues();
}

function updateValues() {
    
}

function activateCalc(idToActivate) {
    var arr = document.getElementsByClassName("MainPanel");
    for (var i = 0; i < arr.length; i++) {
        arr[i].style.display="none";
    }
    document.getElementById(idToActivate).style.display = "block";
}