// 1. Animación de aparición (Scroll Reveal)
const observerOptions = {
    threshold: 0.1
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
        }
    });
}, observerOptions);

document.querySelectorAll('section').forEach(section => {
    observer.observe(section);
});

// 2. Efecto de sombra en Navbar al hacer Scroll
window.onscroll = function() {
    const nav = document.querySelector('.navbar');
    if (window.pageYOffset > 100) {
        nav.style.boxShadow = "0 2px 10px rgba(0,0,0,0.3)";
    } else {
        nav.style.boxShadow = "none";
    }
};

// 3. Validación básica del formulario de contacto
const contactForm = document.getElementById('contactForm');
if(contactForm) {
    contactForm.addEventListener('submit', function(e) {
        // Por ahora solo evitamos el recargo, Django manejará esto después
        console.log("Formulario enviado... procesando con Django próximamente.");
    });
}