document.addEventListener("DOMContentLoaded", function () {
    var loginContainer = document.querySelector(".login");
    var loginBtn = loginContainer.querySelector(".login-btn");
    var loginPopup = loginContainer.querySelector(".login-popup");
  
    loginBtn.addEventListener("click", function (event) {
      event.stopPropagation();
      var isLoginPopupOpen = loginPopup.style.display === "block";
      loginPopup.style.display = isLoginPopupOpen ? "none" : "block";
    });
  
    document.addEventListener("click", function (event) {
      if (!loginContainer.contains(event.target)) {
        loginPopup.style.display = "none";
      }
    });
  });