document.addEventListener('DOMContentLoaded', function () {
    const menuToggle = document.getElementById('menu-toggle');
    const menu = document.getElementById('menu');

    const handleToggleMenu = (event) => {
        if (!menu.contains(event.target) && event.target !== menuToggle) {
            menu.classList.add('hidden');
        }
    };

    menuToggle.addEventListener('click', () => {
        menu.classList.toggle('hidden');
    });

    document.addEventListener('click', handleToggleMenu);
});


function startSlider() {
    setInterval(function () {
        document.querySelector('.slider-nav-next').click();
    }, 5000);
}

document.addEventListener('DOMContentLoaded', startSlider);