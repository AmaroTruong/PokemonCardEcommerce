// Wait for the DOM content to be loaded before executing the code
document.addEventListener("DOMContentLoaded", function() {
  // Get references to the elements needed for the dropdown functionality
  const dropdown = document.querySelector(".dropdownSettings");
  const settingsButton = dropdown.querySelector(".dropdown-settings");
  const popover = dropdown.querySelector(".popSettings");
  let isOpen = false; // Variable to track whether the dropdown is currently open or closed

  // Add a click event listener to the settings button within the dropdown
  settingsButton.addEventListener("click", function(event) {
    event.stopPropagation(); // Prevent the click event from propagating to the document
    isOpen = !isOpen; // Toggle the isOpen variable to track the state of the dropdown
    popover.classList.toggle("active", isOpen); // Add or remove the "active" class based on the isOpen state
  });

  // Add a click event listener to the document to handle clicks outside the dropdown
  document.addEventListener("click", function(event) {
    // Check if the click target is not within the dropdown
    if (!dropdown.contains(event.target)) {
      isOpen = false; // Set isOpen to false, indicating that the dropdown is closed
      popover.classList.remove("active"); // Remove the "active" class to hide the dropdown popover
    }
  });
});
