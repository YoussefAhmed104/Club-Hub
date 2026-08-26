let eyeIcon = document.getElementById("eyeIcon");
let password = document.getElementById("password");
eyeIcon.onclick = function () {
  let eye = document.querySelector(".input-group i");
  if (password.type == "password") {
    password.type = "text";
    eye.className = "fa-regular fa-eye-slash";
  } else {
    password.type = "password";
    eye.className = "fa-regular fa-eye";
  }
};

let container = document.querySelector(".container");
let box = document.querySelector(".form-container");

let signBtn = document.getElementById("log-btn");
let popup = document.querySelector(".popupYes");
signBtn.onclick = function () {
  popup.classList.add("active");
  box.style.cssText = "z-index: -2";
  container.style.cssText = "filter: blur(4px)";
};
