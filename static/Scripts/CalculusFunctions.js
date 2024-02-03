var values = new Map();
var selection = false;


function buttonClicked(id) {
    var btn = document.getElementById("BUTTON_CALC");
    var btn2 = document.getElementById("BUTTON_CONV");
    var pnl = document.getElementById("LOWER_PART_CALC");
    var pnl2 = document.getElementById("LOWER_PART_CONV");

    if (id==="BUTTON_CALC") {
        pnl.style.display = "block";
        pnl2.style.display = "none";
        btn.style.boxShadow = "0 0 45px red";
        btn2.style.boxShadow = "0 0 0";
    }
    if (id==="BUTTON_CONV") {
        pnl.style.display = "none";
        pnl2.style.display = "block";
        btn.style.boxShadow = "0 0 0";
        btn2.style.boxShadow = "0 0 45px orangered";
    }
}

function calculateEscapeVelocity() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass_EV').value);
    var radius = parseFloat(document.getElementById('radius_EV').value);
    const massUnit = document.getElementById('massUnit_EV').value;
    const radiusUnit = document.getElementById('radiusUnit_EV').value;

    document.getElementById('mass_EV').value = "0";
    document.getElementById('radius_EV').value = "0";
    document.getElementById('result_EV').value = "0";

    if (isNaN(mass) || isNaN(radius) || mass <= 0 || radius <= 0) {
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
    updateValues(escapeVelocity, "green");
}

function calculateFirstCosmicSpeed() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass_FCS').value);
    var radius = parseFloat(document.getElementById('radius_FCS').value);
    const massUnit = document.getElementById('massUnit_FCS').value;
    const radiusUnit = document.getElementById('radiusUnit_FCS').value;

    document.getElementById('mass_FCS').value = "0";
    document.getElementById('radius_FCS').value = "0";
    document.getElementById('result_FCS').value = "0";

    if (isNaN(mass) || isNaN(radius) || mass <= 0 || radius <= 0) {
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
    updateValues(firstCosmicSpeed, "green");
}

function calculateSynodicPeriod() {
    var orbitalPeriodA = parseFloat(document.getElementById('orbital_period_A').value);
    var orbitalPeriodB = parseFloat(document.getElementById('orbital_period_B').value);
    const orbitalUnitA = document.getElementById('orbital_unit_A').value;
    const orbitalUnitB = document.getElementById('orbital_unit_B').value;

    document.getElementById('orbital_period_A').value = "0";
    document.getElementById('orbital_period_B').value = "0";
    document.getElementById('result_synodic').value = "0";

    if (isNaN(orbitalPeriodA) || isNaN(orbitalPeriodB) || orbitalPeriodA <= 0 || orbitalPeriodB <= 0) {
        return;
    }

    switch (orbitalUnitA) {
        case 'days':
            break;
        case 'months':
            orbitalPeriodA *= 30;
            break;
        case 'years':
            orbitalPeriodA *= 365;
            break;
        default:
            alert('Invalid orbital unit for Object A.');
            return;
    }

    switch (orbitalUnitB) {
        case 'days':
            break;
        case 'months':
            orbitalPeriodB *= 30;
            break;
        case 'years':
            orbitalPeriodB *= 365;
            break;
        default:
            alert('Invalid orbital unit for Object B.');
            return;
    }

    const synodicPeriod = Math.abs((orbitalPeriodA * orbitalPeriodB) / (orbitalPeriodA - orbitalPeriodB));
    document.getElementById('result_synodic').value = synodicPeriod.toFixed(10);
    updateValues(synodicPeriod, "blue");
}

function calculateSemiMajorAxis() {
    const G = 6.67430e-11;
    var period = parseFloat(document.getElementById('period_KTL').value);
    var mass = parseFloat(document.getElementById('mass_KTL').value);
    const periodUnit = document.getElementById('periodUnit_KTL').value;    
    const massUnit = document.getElementById('massUnit_KTL').value;

    document.getElementById('period_KTL').value = "0";
    document.getElementById('mass_KTL').value = "0";

    if (isNaN(period) || isNaN(mass) || period <= 0 || mass <= 0) {
        document.getElementById('result_KTL').value = "0";
        return;
    }

    switch (periodUnit) {
        case 'years':
            period *= 1;
            break;
        case 'days':
            period /= 365;
            break;
        case 'months':
            period /= 12;
            break;
        default:
            alert('Invalid period unit.');
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
    const distance = Math.cbrt(((period * period * G * mass) / (4 * Math.PI * Math.PI)));
    
    document.getElementById('result_KTL').value = distance.toFixed(10);
    updateValues(distance, "red");
}

function calculateStarLuminosity() {
    const sigma = 5.670374419e-8;
    var radius = parseFloat(document.getElementById('radius_SL').value);
    var temperature = parseFloat(document.getElementById('temperature_SL').value);
    const radiusUnit = document.getElementById('radiusUnit_SL').value;
    const temperatureUnit = document.getElementById('temperatureUnit_SL').value;

    document.getElementById('radius_SL').value = "0";
    document.getElementById('temperature_SL').value = "0";
    document.getElementById('result_SL').value = "0";

    if (isNaN(radius) || isNaN(temperature) || radius <= 0 || temperature <= 0) {
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

    switch (temperatureUnit) {
        case 'K':
            break;
        case '°C':
            temperature += 273.15;
            break;
        case '°F':
            temperature = (temperature + 459.67) * (5 / 9);
            break;
        default:
            alert('Invalid temperature unit.');
            return;
    }

    const luminosity = 4 * Math.PI * Math.pow(radius, 2) * sigma * Math.pow(temperature, 4);
    document.getElementById('result_SL').value = luminosity.toExponential(2);
    updateValues(luminosity, "yellow");
}

function calculateRedshift() {
    var initialFreq = parseFloat(document.getElementById('initialFreq').value);
    var finalFreq = parseFloat(document.getElementById('finalFreq').value);
    const initialFreqUnit = document.getElementById('initialFreqUnit').value;
    const finalFreqUnit = document.getElementById('finalFreqUnit').value;

    document.getElementById('initialFreq').value = "0";
    document.getElementById('finalFreq').value = "0";
    document.getElementById('resultRedshift').value = "0";

    if (isNaN(initialFreq) || isNaN(finalFreq) || initialFreq <= 0 || finalFreq <= 0) {
        return;
    }

    switch (initialFreqUnit) {
        case 'kHz':
            initialFreq *= 1e3;
            break;
        case 'MHz':
            initialFreq *= 1e6;
            break;
        case 'GHz':
            initialFreq *= 1e9;
            break;
        default:
            break;
    }

    switch (finalFreqUnit) {
        case 'kHz':
            finalFreq *= 1e3;
            break;
        case 'MHz':
            finalFreq *= 1e6;
            break;
        case 'GHz':
            finalFreq *= 1e9;
            break;
        default:
            break;
    }

    const redshift = (finalFreq - initialFreq) / initialFreq;
    document.getElementById('resultRedshift').value = redshift.toFixed(10);
    updateValues(redshift, "yellow");
}

function updateValues(value, coloring) {
    var lastLine = document.getElementsByClassName("TopLine")[0];
    var middleLine = document.getElementsByClassName("MiddleLine")[0];
    var formerLine = document.getElementsByClassName("BotLine")[0];
    
    if (!middleLine.innerHTML) {
        middleLine.innerHTML = value;
        middleLine.style.color = coloring;
    }
}

function activateCalc(idToActivate) {
    var arr = document.getElementsByClassName("MainPanel");
    var arr2 = document.getElementsByClassName("LeftPanelItem");
    for (var i = 0; i < arr.length; i++) {
        arr[i].style.display = "none";
    }
    for (var i = 0; i < arr2.length; i++) {
        arr2[i].classList.remove("LeftPanelItemForced");
    }
    document.getElementById(idToActivate).style.display = "block";
    document.getElementById(idToActivate+"_SIDE").classList.add("LeftPanelItemForced");
}