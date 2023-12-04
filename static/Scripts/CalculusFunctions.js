function calculateEscapeVelocity() {
    const G = 6.67430e-11; // Gravitational constant
    const mass = parseFloat(document.getElementById('mass').value);
    const radius = parseFloat(document.getElementById('radius').value);

    if (isNaN(mass) || isNaN(radius)) {
        alert('Please enter valid values for mass and radius.');
        return;
    }

    const escapeVelocity = Math.sqrt(2 * G * mass / radius);
    document.getElementById('result').value = escapeVelocity.toFixed(2);
}