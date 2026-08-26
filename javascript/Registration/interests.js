let interests = document.querySelectorAll(".choices > div");

interests.forEach(function (interest) {
  interest.onclick = function () {
    interest.classList.toggle("selected");
  };
});
