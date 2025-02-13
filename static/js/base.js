document.addEventListener("DOMContentLoaded", () => {

    const menuLinks = document.querySelectorAll('.menu a');
    const targetValue = document.querySelector('.menu').getAttribute('data-target-value');
    const listCreationModal = document.getElementById("list-creation-modal");

    lucide.createIcons();
    
    menuLinks.forEach(item => {
        if (item.textContent.trim() === targetValue) {
            item.classList.add('active');
        }
    });

    document.querySelectorAll('.toggle-modify-modal').forEach(element => {
        element.addEventListener('click', function () {

            const listId = this.getAttribute('data-list-id');
            console.log(listId);
            document.getElementById('list-id-field').value = listId;
        });
    });

    document.querySelectorAll('.nav-toggle').forEach(element => {
        element.addEventListener('click', function () {
            document.getElementById('actionbar').classList.toggle('expanded');
        });
    });

});