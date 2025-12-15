// Light/Dark theme toggler shared across pages
(function () {
  const STORAGE_KEY = "sc-theme";
  const root = document.documentElement;

  const getPreferredTheme = () => {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored === "light" || stored === "dark") return stored;
    return window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark";
  };

  const updateToggleUI = (theme) => {
    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      const icon = button.querySelector("[data-theme-icon]");
      const label = button.querySelector("[data-theme-label]");
      if (icon) icon.textContent = theme === "light" ? "🌞" : "🌙";
      if (label) label.textContent = theme === "light" ? "Light" : "Dark";
      button.setAttribute("aria-pressed", theme === "light");
      button.setAttribute("data-theme-state", theme);
    });
  };

  const applyTheme = (theme) => {
    const nextTheme = theme === "light" ? "light" : "dark";
    root.setAttribute("data-theme", nextTheme);
    try {
      localStorage.setItem(STORAGE_KEY, nextTheme);
    } catch (err) {
      // ignore storage errors (private browsing, etc.)
    }
    updateToggleUI(nextTheme);
  };

  const toggleTheme = () => {
    const current = root.getAttribute("data-theme") === "light" ? "light" : "dark";
    applyTheme(current === "light" ? "dark" : "light");
  };

  const init = () => {
    applyTheme(getPreferredTheme());

    document.querySelectorAll("[data-theme-toggle]").forEach((button) => {
      button.addEventListener("click", toggleTheme);
    });

    // If user hasn't set a preference, follow system changes
    const mediaQuery = window.matchMedia("(prefers-color-scheme: light)");
    mediaQuery.addEventListener("change", (event) => {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored !== "light" && stored !== "dark") {
        applyTheme(event.matches ? "light" : "dark");
      }
    });
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Expose minimal API for debugging
  window.scTheme = { applyTheme, toggleTheme };
})();

