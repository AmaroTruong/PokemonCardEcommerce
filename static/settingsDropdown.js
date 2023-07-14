document.addEventListener("DOMContentLoaded", function() {
    const dropdown = document.querySelector(".dropdownSettings");
    const settingsButton = dropdown.querySelector(".dropdown-settings");
    const popover = dropdown.querySelector(".popSettings");
    let isOpen = false;
  
    settingsButton.addEventListener("click", function(event) {
      event.stopPropagation();
      isOpen = !isOpen;
      popover.classList.toggle("active", isOpen);
    });
  
    document.addEventListener("click", function(event) {
      if (!dropdown.contains(event.target)) {
        isOpen = false;
        popover.classList.remove("active");
      }
    });
  });