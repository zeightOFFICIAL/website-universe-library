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

    document.getElementById('mass_EV').value = "0";
    document.getElementById('radius_EV').value = "0";

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
    values.push(escapeVelocity);
    updateValues();
}

function calculateFirstCosmicSpeed() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass_FCS').value);
    const massUnit = document.getElementById('massUnit_FCS').value;
    var radius = parseFloat(document.getElementById('radius_FCS').value);
    const radiusUnit = document.getElementById('radiusUnit_FCS').value;

    document.getElementById('mass_FCS').value = "0";
    document.getElementById('radius_FCS').value = "0";

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
    values.push(firstCosmicSpeed);
    updateValues();
}

function calculateSynodicPeriod() {
    var orbitalPeriodA = parseFloat(document.getElementById('orbital_period_A').value);
    const orbitalUnitA = document.getElementById('orbital_unit_A').value;
    var orbitalPeriodB = parseFloat(document.getElementById('orbital_period_B').value);
    const orbitalUnitB = document.getElementById('orbital_unit_B').value;

    document.getElementById('orbital_period_A').value = "0";
    document.getElementById('orbital_period_B').value = "0";

    if (isNaN(orbitalPeriodA) || isNaN(orbitalPeriodB) || orbitalPeriodA <= 0 || orbitalPeriodB <= 0) {
        document.getElementById('result_synodic').value = "0";
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
    values.push(escapeVelocity);
    updateValues();
}

function calculateKeplersThirdLaw() {
    const earthOrbitalPeriod = 1;
    const earthAverageDistance = 1; 

    var orbitalPeriod = parseFloat(document.getElementById('orbital_period').value);
    var averageDistance = parseFloat(document.getElementById('average_distance').value);

    document.getElementById('orbital_period').value = "0";
    document.getElementById('average_distance').value = "0";

    if (isNaN(orbitalPeriod) || isNaN(averageDistance) || orbitalPeriod <= 0 || averageDistance <= 0) {
        document.getElementById('result_keplers').value = "0";
        return;
    }

    const keplersThirdLaw = Math.sqrt((orbitalPeriod ** 2) * (averageDistance ** 3) / (earthOrbitalPeriod ** 2 * earthAverageDistance ** 3));
    document.getElementById('result_keplers').value = keplersThirdLaw.toFixed(10);
}

function calculateStarLuminosity() {
    const sigma = 5.670374419e-8;
    var radius = parseFloat(document.getElementById('radius_SL').value);
    const radiusUnit = document.getElementById('radiusUnit_SL').value;
    var temperature = parseFloat(document.getElementById('temperature_SL').value);
    const temperatureUnit = document.getElementById('temperatureUnit_SL').value;

    document.getElementById('radius_SL').value = "0";
    document.getElementById('temperature_SL').value = "0";

    if (isNaN(radius) || isNaN(temperature) || radius <= 0 || temperature <= 0) {
        document.getElementById('result_SL').value = "0";
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
            temperature = (temperature + 459.67) * (5/9);
            break;
        default:
            alert('Invalid temperature unit.');
            return;
    }

    const luminosity = 4 * Math.PI * Math.pow(radius, 2) * sigma * Math.pow(temperature, 4);
    document.getElementById('result_SL').value = luminosity.toExponential(2);
    values.push(luminosity);
    updateValues();
}

function calculateRedshift() {
    var initialFreq = parseFloat(document.getElementById('initialFreq').value);
    const initialFreqUnit = document.getElementById('initialFreqUnit').value;
    var finalFreq = parseFloat(document.getElementById('finalFreq').value);
    const finalFreqUnit = document.getElementById('finalFreqUnit').value;

    document.getElementById('initialFreq').value = "0";
    document.getElementById('finalFreq').value = "0";

    if (isNaN(initialFreq) || isNaN(finalFreq) || initialFreq <= 0 || finalFreq <= 0) {
        document.getElementById('resultRedshift').value = "0";
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
    values.push(redshift);
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