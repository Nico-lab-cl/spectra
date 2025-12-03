document.addEventListener('DOMContentLoaded', () => {
    console.log('Spectra Loaded');

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Parallax effect for glowing background
    document.addEventListener('mousemove', (e) => {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;

        const glow = document.querySelector('.background-glow');
        glow.style.transform = `translate(-${x * 20}px, -${y * 20}px) scale(1.1)`;
    });
});
