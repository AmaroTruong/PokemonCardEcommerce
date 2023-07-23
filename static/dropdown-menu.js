// This event listener waits for the DOM (Document Object Model) to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
    // Get the DOM element with the class "dropdown"
    var dropdown = document.querySelector(".dropdown");

    // Get the DOM element with the class "dropdown-btn" inside the "dropdown" element
    var dropdownBtn = dropdown.querySelector(".dropdown-btn");

    // Get the DOM element with the class "popovermenu" inside the "dropdown" element
    var popovermenu = dropdown.querySelector(".popovermenu");

    // This event listener is triggered when the "dropdownBtn" is clicked
    dropdownBtn.addEventListener("click", function (event) {
        // Stop the click event from propagating to other elements
        event.stopPropagation();

        // Toggle the class "show" on the "dropdown" element
        // This will add the class if it's not present, and remove it if it's already present
        // The "show" class is likely used to control the visibility of the dropdown menu
        dropdown.classList.toggle("show");
    });

    // This event listener is triggered when any part of the document is clicked
    document.addEventListener("click", function (event) {
        // Check if the clicked element is outside the "dropdown" element and if the "show" class is present
        if (!dropdown.contains(event.target) && dropdown.classList.contains("show")) {
            // If the clicked element is outside and the "show" class is present, remove the "show" class
            // This is used to hide the dropdown menu when clicking outside of it
            dropdown.classList.remove("show");
        }
    });
});
