document.addEventListener("DOMContentLoaded", () => {
    const menuLinks = document.querySelectorAll('.menu a');
    const targetValue = document.querySelector('.menu').getAttribute('data-target-value');

    menuLinks.forEach(item => {
        if (item.textContent.trim() === targetValue) {
            item.classList.add('active');
        }
    });

    let listCreationModal = document.getElementById("list-creation-modal");

    function minimizeModal() {
        listCreationModal.classList.toggle('minimized');
    }

});