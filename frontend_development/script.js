// Toggle the left menu collapse/expand state
function toggleMenu() {
    const leftMenu = document.getElementById('leftMenu');
    const isCollapsed = leftMenu.classList.toggle('collapsed');

    // Smoothly transition the width
    leftMenu.style.transition = 'width 0.3s ease';
    if (isCollapsed) {
        leftMenu.style.width = '5%';
    } else {
        leftMenu.style.width = '20%';
    }
}

// Adjust the page width based on screen size
function adjustPageWidth() {
    const width = window.innerWidth;

    if (width <= 600) {
        document.body.style.width = '50%';
    } else if (width <= 700) {
        document.body.style.width = '75%';
    } else if (width <= 767) {
        document.body.style.width = '80%';
    } else if (width <= 1600) {
        document.body.style.width = '90%';
    } else {
        document.body.style.width = '100%';
    }
}

// Event listeners for page load and resizing
window.addEventListener('resize', adjustPageWidth);
window.addEventListener('load', adjustPageWidth);
