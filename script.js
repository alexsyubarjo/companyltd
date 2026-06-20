(function () {
  "use strict";

  /* ── Scroll to top on load / refresh ─────────── */
  if ("scrollRestoration" in history) {
    history.scrollRestoration = "manual";
  }
  window.scrollTo(0, 0);

  /* ── Page Loader ──────────────────────────────── */
  const loader = document.getElementById("pageLoader");
  if (loader) {
    const minTime = 900; // minimum display time in ms
    const start = Date.now();

    function hideLoader() {
      const elapsed = Date.now() - start;
      const remaining = Math.max(0, minTime - elapsed);
      setTimeout(() => {
        loader.classList.add("hide");
        // Remove from DOM after fade out
        loader.addEventListener("transitionend", () => loader.remove(), { once: true });
      }, remaining);
    }

    if (document.readyState === "complete") {
      hideLoader();
    } else {
      window.addEventListener("load", hideLoader);
    }
  }

  const header = document.getElementById("header");
  const navToggle = document.getElementById("navToggle");
  const mainNav = document.getElementById("mainNav");
  const layananTrigger = document.getElementById("layananTrigger");
  const megaParent = layananTrigger?.closest(".has-mega");
  const yearEl = document.getElementById("year");
  const contactForm = document.getElementById("contactForm");

  if (yearEl) {
    yearEl.textContent = String(new Date().getFullYear());
  }

  /* Sticky header shadow */
  function onScroll() {
    if (header) {
      header.classList.toggle("scrolled", window.scrollY > 10);
    }
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* Mobile nav toggle */
  if (navToggle && mainNav) {
    navToggle.addEventListener("click", () => {
      const open = mainNav.classList.toggle("open");
      navToggle.classList.toggle("open", open);
      navToggle.setAttribute("aria-expanded", String(open));
      document.body.style.overflow = open ? "hidden" : "";
    });

    mainNav.querySelectorAll("a[href^='#']").forEach((link) => {
      link.addEventListener("click", closeMobileNav);
    });
  }

  function closeMobileNav() {
    if (!mainNav || !navToggle) return;
    mainNav.classList.remove("open");
    navToggle.classList.remove("open");
    navToggle.setAttribute("aria-expanded", "false");
    document.body.style.overflow = "";
  }

  /* Mega menu — click toggle */
  if (layananTrigger && megaParent) {
    layananTrigger.addEventListener("click", (e) => {
      e.preventDefault();
      const open = megaParent.classList.toggle("open");
      layananTrigger.setAttribute("aria-expanded", String(open));
    });

    document.addEventListener("click", (e) => {
      if (!megaParent.contains(e.target)) {
        megaParent.classList.remove("open");
        layananTrigger.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* Active nav on scroll */
  const sections = document.querySelectorAll("section[id]");
  const navLinks = document.querySelectorAll(".main-nav .nav-link[href^='#']");

  function setActiveNav() {
    let current = "";
    const offset = 140;

    sections.forEach((section) => {
      const top = section.offsetTop - offset;
      if (window.scrollY >= top) {
        current = section.getAttribute("id") || "";
      }
    });

    navLinks.forEach((link) => {
      const href = link.getAttribute("href");
      link.classList.toggle("active", href === `#${current}`);
    });
  }

  window.addEventListener("scroll", setActiveNav, { passive: true });
  setActiveNav();

  /* Contact form */
  if (contactForm) {
    contactForm.addEventListener("submit", (e) => {
      e.preventDefault();

      const formData = new FormData(contactForm);
      const name = formData.get("name");
      const email = formData.get("email");
      const business = formData.get("business");
      const need = formData.get("need");
      const message = formData.get("message") || "";

      if (!name || !email || !business || !need) {
        alert("Mohon lengkapi semua field yang wajib diisi.");
        return;
      }

      const waText = encodeURIComponent(
        `Halo NexusForge Digital,\n\n` +
          `Nama: ${name}\n` +
          `Email: ${email}\n` +
          `Jenis Bisnis: ${business}\n` +
          `Kebutuhan: ${need}\n` +
          (message ? `Pesan: ${message}\n` : "") +
          `\nSaya ingin konsultasi website dan audit keamanan.`
      );

      window.open(`https://wa.me/6281234567890?text=${waText}`, "_blank", "noopener");

      contactForm.innerHTML =
        `<div class="form-success show">` +
        `<svg width="48" height="48" viewBox="0 0 48 48" aria-hidden="true">` +
        `<circle cx="24" cy="24" r="22" stroke="currentColor" fill="none" stroke-width="2"/>` +
        `<path d="M14 24l8 8 16-16" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round"/>` +
        `</svg>` +
        `<h3>Permintaan Terkirim!</h3>` +
        `<p>Terima kasih, ${name}. Kami akan menghubungi Anda via email atau WhatsApp dalam 1×24 jam kerja.</p>` +
        `</div>`;
    });
  }

  /* Smooth scroll for anchor links */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", (e) => {
      const id = anchor.getAttribute("href");
      if (!id || id === "#") return;

      const target = document.querySelector(id);
      if (!target) return;

      e.preventDefault();
      const top = target.offsetTop - 100;
      window.scrollTo({ top, behavior: "smooth" });
      closeMobileNav();
    });
  });

  /* Resize — close mobile nav on desktop */
  window.addEventListener("resize", () => {
    if (window.innerWidth > 768) {
      closeMobileNav();
      if (megaParent) megaParent.classList.remove("open");
    }
  });
})();
