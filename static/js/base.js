document.addEventListener("DOMContentLoaded", () => {
    const menu = document.querySelector('.actionbar');
    const menuToggler = document.getElementById('nav-toggle');

    const menuLinks = document.querySelectorAll('.menu a');
    const targetValue = document.querySelector('.menu').getAttribute('data-target-value');
    let listCreationModal = document.getElementById("list-creation-modal");

    lucide.createIcons();
    
    menuLinks.forEach(item => {
        if (item.textContent.trim() === targetValue) {
            item.classList.add('active');
        }
    });
    
    menuToggler.addEventListener('click', () => {
        menu.classList.toggle('expanded');
    })


});