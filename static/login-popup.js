// Wait for the DOM content to be loaded before executing the code
document.addEventListener("DOMContentLoaded", function () {
  // Get the required elements from the DOM
  var loginContainer = document.querySelector(".login");
  var loginBtn = loginContainer.querySelector(".login-btn");
  var loginPopup = loginContainer.querySelector(".login-popup");
  var createAccountLink = loginContainer.querySelector("#create-account-link");
  var createAccountPopup = loginContainer.querySelector(".create-account-popup");
  var loginLink = loginContainer.querySelector("#login-link");

  // Toggle loginPopup visibility when loginBtn is clicked
  loginBtn.addEventListener("click", function (event) {
    event.stopPropagation();
    var isLoginPopupOpen = loginPopup.style.display === "block";
    loginPopup.style.display = isLoginPopupOpen ? "none" : "block";
    createAccountPopup.style.display = "none";
  });

  // Hide loginPopup and createAccountPopup when clicking outside the loginContainer
  document.addEventListener("click", function (event) {
    if (!loginContainer.contains(event.target)) {
      loginPopup.style.display = "none";
      createAccountPopup.style.display = "none";
    }
  });

  // Attach event listener to the "Recover Password" link to open the reset popup
  document.getElementById("recoverPassword").addEventListener("click", openResetPopup);

  function openResetPopup() {
    loginPopup.style.display = "none";
    createAccountPopup.style.display = "none";
    document.querySelector("#reset-popup").style.display = "block";
  }

  // Show the createAccountPopup when the "Create Account" link is clicked
  createAccountLink.addEventListener("click", function () {
    loginPopup.style.display = "none";
    createAccountPopup.style.display = "block";
  });

  // Attach event listener to the "Login" link to open the login popup
  document.getElementById("login-link").addEventListener("click", openLoginPopup);

  // Submit the create account form and show loginPopup after successful submission
  createAccountPopup.querySelector("button[type='submit']").addEventListener("click", function () {
    createAccountPopup.style.display = "none";
    loginPopup.style.display = "block";
  });

  // Handle login form submission
  document.querySelector(".login-form").addEventListener("submit", function (event) {
    event.preventDefault();
   
    // Check the response status and redirect to the appropriate page or show an alert
    if (response.status === 200) {
      window.location.href = "/catalogueLogged";
    } else if (response.status === 401) {
      response.text().then(function (errorMessage) {
        showAlert(errorMessage);
      });
    }
  });

  // Function to open the login popup
  function openLoginPopup() {
    document.querySelector(".create-account-popup").style.display = "none";
    document.querySelector(".login-popup").style.display = "block";
  }

  // Function to show an alert with a given message
  function showAlert(message) {
    alert(message);
  }

  // Show the loginPopup and hide createAccountPopup when "Login" link is clicked
  loginLink.addEventListener("click", function () {
    loginPopup.style.display = "block";
    createAccountPopup.style.display = "none";
  });

  // Show the loginPopup and hide createAccountPopup when loginBtn is clicked
  loginBtn.addEventListener("click", function () {
    loginPopup.style.display = "block";
    createAccountPopup.style.display = "none";
  });
});

