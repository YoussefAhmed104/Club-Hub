let eyeIcon = document.getElementById("eyeIcon");
let password = document.getElementById("password");
eyeIcon.onclick = function () {
  if (password.value.length > 0) {
    let eye = document.querySelector(".input-group i");
    if (password.type == "password") {
      password.type = "text";
      eye.className = "fa-regular fa-eye-slash";
    } else {
      password.type = "password";
      eye.className = "fa-regular fa-eye";
    }
  }
};

let container = document.querySelector(".container");
let box = document.querySelector(".form-container");

let logBtn = document.getElementById("log-btn");
let popupYes = document.querySelector(".popupYes");
let popupNo = document.querySelector(".popupNo");
logBtn.onclick = function (e) {
  e.preventDefault();
  popupNo.classList.add("active");
  box.style.cssText = "z-index: -2";
  container.style.cssText = "filter: blur(4px)";
};
/* signBtn.onclick = function () {
  popupYes.classList.add("active");
  box.style.cssText = "z-index: -2";
  container.style.cssText = "filter: blur(4px)";
}; */
