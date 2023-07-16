document.addEventListener("DOMContentLoaded", function () {
  var loginContainer = document.querySelector(".login");
  var loginBtn = loginContainer.querySelector(".login-btn");
  var loginPopup = loginContainer.querySelector(".login-popup");
  var createAccountLink = loginContainer.querySelector("#create-account-link");
  var createAccountPopup = loginContainer.querySelector(".create-account-popup");
  var loginLink = loginContainer.querySelector("#login-link");

  loginBtn.addEventListener("click", function (event) {
    event.stopPropagation();
    var isLoginPopupOpen = loginPopup.style.display === "block";
    loginPopup.style.display = isLoginPopupOpen ? "none" : "block";
    createAccountPopup.style.display = "none";
  });

  document.addEventListener("click", function (event) {
    if (!loginContainer.contains(event.target)) {
      loginPopup.style.display = "none";
      createAccountPopup.style.display = "none";
    }
  });


  document.getElementById("recoverPassword").addEventListener("click", openResetPopup);

  function openResetPopup() {
    document.querySelector(".login-popup").style.display = "none";
    document.querySelector(".create-account-popup").style.display = "none";
  
    document.querySelector("#reset-popup").style.display = "block";
  }
  
  createAccountLink.addEventListener("click", function() {
    loginPopup.style.display = "none";
    createAccountPopup.style.display = "block";
  });

  document.getElementById("login-link").addEventListener("click", openLoginPopup);

  createAccountPopup.querySelector("button[type='submit']").addEventListener("click", function() {
    createAccountPopup.style.display = "none";
    loginPopup.style.display = "block";
  });

  document.querySelector(".login-form").addEventListener("submit", function(event) {
    event.preventDefault();
   
    if (response.status === 200) {
      window.location.href = "/catalogueLogged";
    } else if (response.status === 401) {
      response.text().then(function(errorMessage) {
        showAlert(errorMessage);
      });
    }
  });

  function openLoginPopup() {
    document.querySelector(".create-account-popup").style.display = "none";
  
    document.querySelector(".login-popup").style.display = "block";
  }
  
  function showAlert(message) {
    alert(message);
  }

  loginLink.addEventListener("click", function() {
    loginPopup.style.display = "block";
    createAccountPopup.style.display = "none";
  });

  loginBtn.addEventListener("click", function () {
    loginPopup.style.display = "block";
    createAccountPopup.style.display = "none";
  });
});

