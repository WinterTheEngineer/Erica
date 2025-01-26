document.addEventListener("DOMContentLoaded", () => {
    const menu = document.querySelector('.actionbar');

    const menuLinks = document.querySelectorAll('.menu a');
    const targetValue = document.querySelector('.menu').getAttribute('data-target-value');
    const listCreationModal = document.getElementById("list-creation-modal");

    lucide.createIcons();
    
    menuLinks.forEach(item => {
        if (item.textContent.trim() === targetValue) {
            item.classList.add('active');
        }
    });

    document.querySelectorAll('.nav-toggle').forEach(toggler => {
        toggler.addEventListener('click', () => {
            menu.classList.toggle('expanded');
        });
    });

    document.querySelectorAll('.toggle-modal').forEach(element => {
        element.addEventListener('click', () => {
            listCreationModal.classList.toggle('minimized');
        });
    });

});