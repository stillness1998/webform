document.getElementById('registerForm').addEventListener('submit', function (e) {
    const emailInput = document.getElementById('email');
    const phoneInput = document.getElementById('phone');
    const passwordInput = document.getElementById('password');
    const phoneValue = phoneInput.value;
    const passwordValue = passwordInput.value;


    const emailPattern = /^[^\s@]+@[^\s@]+.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value)) {
        alert('Please enter a valid email address.');
        e.preventDefault(); 
        return;
    }


    const phonePattern = /^\d{10,15}$/; 
    if (!phonePattern.test(phoneValue)) {
        alert('Phone number must be between 10 and 15 digits.');
        e.preventDefault(); 
        return;
    }


    if (passwordValue.length < 6) { 
        alert('Password must be at least 6 characters long.');
        e.preventDefault(); 
        return;
    }
});