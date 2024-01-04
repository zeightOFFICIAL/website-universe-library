var values = [];

function calculateEscapeVelocity() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass').value);
    const massUnit = document.getElementById('massUnit').value;
    var radius = parseFloat(document.getElementById('radius').value);
    const radiusUnit = document.getElementById('radiusUnit').value;

    if (isNaN(mass) || isNaN(radius) || mass < 0 || radius < 0) {
        alert('Please enter valid values for mass and radius.');
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
    document.getElementById('result').value = escapeVelocity.toFixed(10);

    document.getElementById('mass').value = "";
    document.getElementById('radius').value = "";
    values.push(escapeVelocity);
    updateValues();
}

function calculateFirstCosmicSpeed() {
    const G = 6.67430e-11;
    var mass = parseFloat(document.getElementById('mass').value);
    const massUnit = document.getElementById('massUnit').value;
    var radius = parseFloat(document.getElementById('radius').value);
    const radiusUnit = document.getElementById('radiusUnit').value;

    if (isNaN(mass) || isNaN(radius) || mass < 0 || radius < 0) {
        alert('Please enter valid values for mass and radius.');
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
    document.getElementById('result').value = firstCosmicSpeed.toFixed(10);

    document.getElementById('mass').value = "";
    document.getElementById('radius').value = "";
    values.push(firstCosmicSpeed);
    updateValues();
}

function updateValues() {
    if (values.length > 5) {
        values.splice(0, 1);
    }
    var toDiv = document.getElementsByClassName("RightPanel")[0];

    array.reverse().forEach(element => {

    });
}