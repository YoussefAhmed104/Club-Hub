const scrollContainer = document.querySelector('.scroll');
const navLinks = document.querySelectorAll('.scroll ul li a');
const indicator = document.querySelector('.nav-indicator');

function updateIndicator(element) {
  const linkRect = element.getBoundingClientRect();
  const containerRect = scrollContainer.getBoundingClientRect();

  indicator.style.width = `${linkRect.width}px`;
  indicator.style.left = `${linkRect.left - containerRect.left}px`;
}

function setActiveTab() {
  const currentPath = window.location.pathname;

  navLinks.forEach((link) => {
    if (link.getAttribute('href') && currentPath.includes(link.getAttribute('href').replace('./', ''))) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  const activeLink = document.querySelector('.scroll ul li a.active') || navLinks[0];
  if (activeLink) {
    activeLink.classList.add('active');
    updateIndicator(activeLink);
  }
}

navLinks.forEach((link) => {
  link.addEventListener('click', function (e) {
    const targetHref = this.getAttribute('href');

    if (targetHref && targetHref !== '#') {
      e.preventDefault();

      navLinks.forEach((l) => l.classList.remove('active'));
      this.classList.add('active');
      updateIndicator(this);

      setTimeout(() => {
        window.location.href = targetHref;
      }, 700);
    }
  });
});

window.addEventListener('DOMContentLoaded', setActiveTab);
window.addEventListener('resize', () => {
  const activeLink = document.querySelector('.scroll ul li a.active');
  if (activeLink) updateIndicator(activeLink);
});