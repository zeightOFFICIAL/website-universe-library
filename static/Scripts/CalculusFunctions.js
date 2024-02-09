var values = new Map();

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

    document.getElementById('result_EV').value = "0";
    document.getElementById('result_EV').disabled = "";

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
    document.getElementById('result_EV').value = escapeVelocity;
    updateValues(escapeVelocity, "green");
}

function calculateFirstCosmicSpeed() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass_FCS').value);
    var radius = parseFloat(document.getElementById('radius_FCS').value);
    const massUnit = document.getElementById('massUnit_FCS').value;
    const radiusUnit = document.getElementById('radiusUnit_FCS').value;

    document.getElementById('result_FCS').value = "0";
    document.getElementById('result_FCS').disabled = "";

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
    document.getElementById('result_FCS').value = firstCosmicSpeed;
    updateValues(firstCosmicSpeed, "green");
}

function calculateSynodicPeriod() {
    var orbitalPeriodA = parseFloat(document.getElementById('orbital_period_A').value);
    var orbitalPeriodB = parseFloat(document.getElementById('orbital_period_B').value);
    const orbitalUnitA = document.getElementById('orbital_unit_A').value;
    const orbitalUnitB = document.getElementById('orbital_unit_B').value;

    document.getElementById('result_synodic').value = "0";
    document.getElementById('result_synodic').disabled = "";

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
    document.getElementById('result_synodic').value = synodicPeriod;
    updateValues(synodicPeriod, "blue");
}

function calculateEarthOrbit() {
    const G = 6.67430e-11;
    const M = 5.972e24;
    const R = 6371000;
    var distance = parseFloat(document.getElementById('distance_EO').value);
    const distanceUnit = document.getElementById('distanceUnit_EO').value;

    document.getElementById('result_EO').value = "0";
    document.getElementById('result_EO').disabled = "";

    if (isNaN(distance) || distance <= 0) {
        return;
    }

    switch (distanceUnit) {
        case 'm':
            break;
        case 'km':
            distance *= 1000;
            break;
        case 'AU':
            distance *= 149597870700; 
            break;
        default:
            alert('Invalid distance unit.');
            return;
    }

    const orbitalPeriod = 2 * Math.PI * Math.sqrt((Math.pow((R + distance), 3))/(G * M)) / 60 / 60;
    document.getElementById('result_EO').value = orbitalPeriod;
    updateValues(orbitalPeriod, "red");
}

function calculateStarLuminosity() {
    const sigma = 5.670374419e-8;
    var radius = parseFloat(document.getElementById('radius_SL').value);
    var temperature = parseFloat(document.getElementById('temperature_SL').value);
    const radiusUnit = document.getElementById('radiusUnit_SL').value;
    const temperatureUnit = document.getElementById('temperatureUnit_SL').value;

    document.getElementById('result_SL').value = "0";
    document.getElementById('result_SL').disabled = "";

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
    document.getElementById('result_SL').value = (luminosity/1000000000);
    updateValues(luminosity/1000000000, "yellow");
}

function calculateRedshift() {
    var initialFreq = parseFloat(document.getElementById('initialFreq').value);
    var finalFreq = parseFloat(document.getElementById('finalFreq').value);
    const initialFreqUnit = document.getElementById('initialFreqUnit').value;
    const finalFreqUnit = document.getElementById('finalFreqUnit').value;

    document.getElementById('resultRedshift').value = "0";
    document.getElementById('resultRedshift').disabled = "";

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
    var last = document.getElementsByClassName("TopLine")[0];
    var inmid = document.getElementsByClassName("MiddleLine")[0];    
    var former = document.getElementsByClassName("BotLine")[0];

    if (!last.innerHTML) {
        last.innerHTML = value;
        last.style.color = coloring;
        last.style.border = "2px solid "+coloring;
        last.style.boxShadow = "0 0 50px "+coloring;
        last.style.display = "block";
    }
    else if (!inmid.innerHTML) {
        var temp = last.innerHTML;
        var tempColor = last.style.color;
        last.innerHTML = value;
        last.style.color = coloring;
        last.style.border = "2px solid "+coloring;
        last.style.boxShadow = "0 0 50px "+coloring;
        last.style.display = "block";

        inmid.innerHTML = temp;
        inmid.style.color = tempColor;
        inmid.style.border = "2px solid "+tempColor;
        inmid.style.boxShadow = "0 0 50px "+tempColor;
        inmid.style.display = "block";
    }
    else {
        var tempTop = last.innerHTML;
        var tempTopColor = last.style.color;
        var temp = inmid.innerHTML;
        var tempColor = inmid.style.color;

        former.innerHTML = temp;
        former.style.color = tempColor;
        former.style.border = "2px solid "+tempColor;
        former.style.boxShadow = "0 0 50px "+tempColor;
        former.style.display = "block";

        inmid.innerHTML = tempTop;
        inmid.style.color = tempTopColor;
        inmid.style.border = "2px solid "+tempTopColor;
        inmid.style.boxShadow = "0 0 50px "+tempTopColor;
        inmid.style.display = "block";

        last.innerHTML = value;
        last.style.color = coloring;
        last.style.border = "2px solid "+coloring;
        last.style.boxShadow = "0 0 50px "+coloring;
        last.style.display = "block";
    }
}

function activateCalc(idToActivate) {
    var arr = document.getElementsByClassName("MainPanel");
    var arr2 = document.getElementsByClassName("LeftPanelItem");
    var arr3 = document.getElementsByClassName("result");

    for (var i = 0; i < arr.length; i++) {
        arr[i].style.display = "none";
    }
    for (var i = 0; i < arr2.length; i++) {
        arr2[i].classList.remove("LeftPanelItemForced");
    }
    for (var i = 0; i < arr2.length; i++) {
        arr3[i].value = "0";
        arr3[i].disabled = "disabled";
        arr3[i].disabled = "";
    }

    document.getElementById(idToActivate).style.display = "block";
    document.getElementById(idToActivate+"_SIDE").classList.add("LeftPanelItemForced");
}

function activateConv(idToActivate) {
    var arr = document.getElementsByClassName("MainPanelConv");
    var arr2 = document.getElementsByClassName("LeftPanelItem");
}

function copyToClipboard(idToCopy) {
    var copyObject = document.getElementById(idToCopy);
    copyObject.select();
    copyObject.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyObject.value);
    copyObject.setSelectionRange(0,0);
    copyObject.value = "Copied!";
    copyObject.disabled = "disabled";
}

function copySideToClipboard(classToCopy) {
    var copyObject = document.getElementsByClassName(classToCopy)[0];
    var text = copyObject.innerHTML;
    var tempElement = document.createElement('input');
    tempElement.value = text;
    tempElement.select();
    tempElement.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(tempElement.value);
}