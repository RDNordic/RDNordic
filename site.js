// Progressive enhancement: flag that JS is active. Scroll-reveal elements are
// only hidden when this class is present (see `.js .reveal` in style.css), so
// with JS disabled or blocked the full page renders normally instead of blank.
// Runs at top level under `defer`, before first paint, to avoid any flash.
document.documentElement.classList.add("js");

document.addEventListener("DOMContentLoaded", function () {
  var navToggle = document.querySelector(".nav-toggle");
  var navLinks = document.querySelector(".nav-links");

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", function () {
      var isOpen = navToggle.classList.toggle("open");
      navLinks.classList.toggle("open", isOpen);
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });
  }

  var revealItems = document.querySelectorAll(".reveal");
  if (!revealItems.length) {
    return;
  }

  if (!("IntersectionObserver" in window)) {
    revealItems.forEach(function (item) {
      item.classList.add("visible");
    });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15 }
  );

  revealItems.forEach(function (item) {
    observer.observe(item);
  });
});
