document.addEventListener("DOMContentLoaded", function () {
    var dropdown = document.querySelector(".dropdown");
    var dropdownBtn = dropdown.querySelector(".dropdown-btn");
    var popovermenu = dropdown.querySelector(".popovermenu");

    dropdownBtn.addEventListener("click", function (event) {
      event.stopPropagation();
      dropdown.classList.toggle("show");
    });

    document.addEventListener("click", function (event) {
      if (!dropdown.contains(event.target) && dropdown.classList.contains("show")) {
        dropdown.classList.remove("show");
      }
    });
});