document.addEventListener("DOMContentLoaded", function () {

  const interests = document.querySelectorAll(".choices > div");
  if (interests.length > 0) {
    interests.forEach(function (interest) {
      interest.onclick = function () {
        interest.classList.toggle("selected");
      };
    });
  }

  const eyeIcon = document.getElementById("eyeIcon");
  const passwordInput = document.getElementById("password");

  if (eyeIcon && passwordInput) {
    eyeIcon.onclick = function () {
      if (passwordInput.value.length > 0) {
        let eye = document.querySelector(".input-group i") || eyeIcon;
        if (passwordInput.type === "password") {
          passwordInput.type = "text";
          eye.className = "fa-regular fa-eye-slash";
        } else {
          passwordInput.type = "password";
          eye.className = "fa-regular fa-eye";
        }
      }
    };
  }

  const container = document.querySelector(".container");
  const box = document.querySelector(".form-container");
  const popupYes = document.querySelector(".popupYes");
  const popupNo = document.querySelector(".popupNo");
  const okBtn = document.getElementById("ok");
  const okYesBtn = document.querySelector(".popupYes button");


  function showPopup(popupElement) {
    if (popupElement) {
      popupElement.classList.add("active");
    }
    if (box) box.style.cssText = "z-index: -2";
    if (container) container.style.cssText = "filter: blur(4px)";
  }


  function hidePopups() {
    if (popupYes) popupYes.classList.remove("active");
    if (popupNo) popupNo.classList.remove("active");
    if (container) container.style.cssText = "";
    if (box) box.style.cssText = "";
  }


  if (okBtn) okBtn.onclick = hidePopups;
  if (okYesBtn) okYesBtn.onclick = hidePopups;


  function validateForm() {

    if (passwordInput && passwordInput.value.trim().length >= 6) {
      return true; 
    }
    return false; 
  }

  const logBtn = document.getElementById("log-btn");
  const signBtn = document.getElementById("sign-btn");


  function handleFormSubmit(e) {
    e.preventDefault();

    const isValid = validateForm();

    if (isValid) {

      showPopup(popupYes);
    } else {

      showPopup(popupNo);
    }
  }

  if (logBtn) logBtn.onclick = handleFormSubmit;
  if (signBtn) signBtn.onclick = handleFormSubmit;
});