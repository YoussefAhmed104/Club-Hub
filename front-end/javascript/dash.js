const header = document.getElementById("header");

window.addEventListener("scroll", function () {
  if (window.scrollY > 20) {
    header.classList.add("scroll");
  } else {
    header.classList.remove("scroll");
  }
});

let burger = document.getElementById("headBurger");
let side_bar = document.getElementById("sideBar");
burger.addEventListener("click", function () {
  side_bar.classList.toggle("open");
});

const logo = document.querySelector(".stemVct");
logo.addEventListener("click", function () {
  window.open("https://www.stemegypt.net/", "_blank");
});

const join = document.querySelector(".joinOrCreate");
join.addEventListener("click", function () {
  join.classList.toggle("active");
});

/* const titles = document.querySelectorAll(".side-bar > div");

titles.forEach((title) => {
  title.addEventListener("click", function (event) {
    event.preventDefault();
    titles.forEach((item) => item.classList.remove("active"));
    title.classList.add("active");
  });
}); */

/* pages  */
const about = document.getElementById("about");
about.addEventListener("click", function () {
  if (window.location.pathname.includes("about.html")) {
    location.reload();
  } else {
    window.location.href = "main pages/about.html";
  }
});
