(function () {
  'use strict';
  const root = document.documentElement;
  const normalizedPath = location.pathname.replace(/index\.html$/, '');
  if (normalizedPath !== location.pathname) history.replaceState(null, '', normalizedPath + location.search + location.hash);
  let savedTheme;
  try { savedTheme = localStorage.getItem('theme'); } catch (_) { /* Storage can be unavailable in privacy modes. */ }
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  root.dataset.theme = ['light', 'dark'].includes(savedTheme) ? savedTheme : (media.matches ? 'dark' : 'light');
  function updateThemeButtons() {
    document.querySelectorAll('.theme-toggle').forEach(button => {
      button.setAttribute('aria-label', 'Switch to ' + (root.dataset.theme === 'dark' ? 'light' : 'dark') + ' theme');
      button.setAttribute('aria-pressed', String(root.dataset.theme === 'dark'));
    });
  }
  updateThemeButtons();
  document.querySelectorAll('.theme-toggle').forEach(button => button.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('theme', root.dataset.theme); } catch (_) { /* Theme still works without storage. */ }
    updateThemeButtons();
  }));
  const navToggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('#nav-links');
  function closeNav(returnFocus) {
    if (!navLinks || !navToggle) return;
    navLinks.classList.remove('is-open'); navToggle.setAttribute('aria-expanded', 'false');
    if (returnFocus) navToggle.focus();
  }
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => navToggle.setAttribute('aria-expanded', String(navLinks.classList.toggle('is-open'))));
    navLinks.querySelectorAll('a').forEach(link => link.addEventListener('click', () => closeNav(false)));
    document.addEventListener('keydown', event => { if (event.key === 'Escape' && navLinks.classList.contains('is-open')) closeNav(true); });
    document.addEventListener('click', event => { if (!event.target.closest('.nav')) closeNav(false); });
    window.matchMedia('(min-width: 981px)').addEventListener('change', () => closeNav(false));
  }
  document.querySelectorAll('[data-filter-group]').forEach(group => {
    const controls = group.querySelector('.filter-controls');
    const buttons = [...group.querySelectorAll('[data-filter]')];
    const items = [...group.querySelectorAll('[data-filter-item]')];
    const status = group.querySelector('.filter-status');
    controls.hidden = false;
    function apply(value) {
      let count = 0;
      items.forEach(item => { item.hidden = value !== 'All' && item.dataset.filterItem !== value; if (!item.hidden) count++; });
      buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.filter === value)));
      status.textContent = count + ' article' + (count === 1 ? '' : 's') + (value === 'All' ? ' · all publishers' : ' · ' + value);
    }
    buttons.forEach(button => button.addEventListener('click', () => apply(button.dataset.filter)));
    apply('All');
    // Deep links must still reveal an article hidden by the current filter.
    window.addEventListener('hashchange', () => { if (items.some(item => '#' + item.id === location.hash && item.hidden)) apply('All'); });
  });
  document.querySelectorAll('[data-print]').forEach(button => button.addEventListener('click', () => window.print()));
})();
