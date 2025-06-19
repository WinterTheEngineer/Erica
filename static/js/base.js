document.addEventListener("DOMContentLoaded", () => {

    const menuLinks = document.querySelectorAll('.menu a');
    const targetValue = document.querySelector('.menu').getAttribute('data-target-value');
    const listCreationModal = document.getElementById("list-creation-modal");

    lucide.createIcons();
    
    menuLinks.forEach(item => {
        if (item.textContent.trim() === targetValue) {
            item.classList.add('active');
        }

        item.addEventListener('click', function (event) {
            if (item.classList.contains('active')) {
                console.log("This is the active link.");
            } else {
                document.querySelector('.menu li a.active').classList.remove('active')
                item.classList.add('active')
            }
        });
    });

    document.querySelectorAll('.toggle-modify-modal').forEach(element => {
        element.addEventListener('click', function () {

            const listId = this.getAttribute('data-list-id');
            console.log(listId);
            document.getElementById('list-id-field').value = listId;
        });
    });

    document.querySelectorAll('.toggle-list-modal').forEach(element => {
        element.addEventListener('click', function () {
            listCreationModal.classList.toggle('expanded');
        });
    });

    document.querySelectorAll('.toggle-dropdown').forEach(element => {
        element.addEventListener('click', function () {
            const listMenuId = this.getAttribute('data-list-id');
            document.getElementById(`menu-${listMenuId}`).classList.toggle('expanded');
            document.getElementById(`list-${listMenuId}`).classList.toggle('menu-toggled');
        });
    });
    
    // // Close menu when clicking outside
    // document.addEventListener('click', function (event) {
    //     document.querySelectorAll('.card-menu.expanded').forEach(menu => {
    //         const toggleButton = document.querySelector(`.toggle-card-menu[data-list-id="${menu.id.replace('menu-', '')}"]`);
            
    //         // Check if the click was outside both the menu and its toggle button
    //         if (!menu.contains(event.target) && !toggleButton.contains(event.target)) {
    //             menu.classList.toggle('expanded');
    //         }
    //     });
    // });

    document.querySelectorAll('.nav-toggle').forEach(element => {
        element.addEventListener('click', function () {
            document.getElementById('actionbar').classList.toggle('expanded');
        });
    });

});