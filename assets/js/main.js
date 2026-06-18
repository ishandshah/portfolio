(function () {
  const root = document.documentElement;
  const normalizedPath = window.location.pathname.replace(/index\.html$/, "");

  if (normalizedPath !== window.location.pathname) {
    window.history.replaceState(null, "", `${normalizedPath}${window.location.search}${window.location.hash}`);
  }

  const savedTheme = localStorage.getItem("theme");
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  if (savedTheme) {
    root.dataset.theme = savedTheme;
  } else if (prefersDark) {
    root.dataset.theme = "dark";
  }

  document.querySelectorAll(".theme-toggle").forEach((button) => {
    button.addEventListener("click", () => {
      const nextTheme = root.dataset.theme === "dark" ? "light" : "dark";
      root.dataset.theme = nextTheme;
      localStorage.setItem("theme", nextTheme);
    });
  });

  const navToggle = document.querySelector(".nav-toggle");
  const navLinks = document.querySelector("#nav-links");

  if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
      const isOpen = navLinks.classList.toggle("is-open");
      navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", () => {
        navLinks.classList.remove("is-open");
        navToggle.setAttribute("aria-expanded", "false");
      });
    });
  }
})();
