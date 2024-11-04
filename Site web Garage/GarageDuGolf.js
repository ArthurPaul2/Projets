document.addEventListener('DOMContentLoaded', function () {
    const images = document.querySelectorAll('.fade-in');
    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-visible');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    images.forEach(image => {
        observer.observe(image);
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const options = {
        root: null, // Utilise le viewport comme racine
        rootMargin: "0px",
        threshold: 0.001 // Déclenche lorsque 10% de l'élément est visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("animate");
                observer.unobserve(entry.target); // Stop observing after animation is triggered
            }
        });
    }, options);

    const slideLeftRightElements = document.querySelectorAll(".slide-left-right");
    slideLeftRightElements.forEach(element => {
        observer.observe(element);
    });

    const slideRightLeftElements = document.querySelectorAll(".slide-right-left");
    slideRightLeftElements.forEach(element => {
        observer.observe(element);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const elements = document.querySelectorAll('.slide-left-right, .slide-right-left');

    function checkVisibility() {
        elements.forEach(element => {
            const rect = element.getBoundingClientRect();
            const isVisible = (rect.top >= 0) && (rect.bottom <= window.innerHeight);
            
            if (isVisible) {
                element.classList.add('visible');
            } else {
                element.classList.remove('visible');
            }
        });
    }

    window.addEventListener('scroll', checkVisibility);
    window.addEventListener('resize', checkVisibility);
    checkVisibility(); // Initial check
});

