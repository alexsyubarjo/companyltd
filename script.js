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
        `Hello alexsyubarjoltd,\n\n` +
          `Nama: ${name}\n` +
          `Email: ${email}\n` +
          `Jenis Bisnis: ${business}\n` +
          `Kebutuhan: ${need}\n` +
          (message ? `Pesan: ${message}\n` : "") +
          `\nSaya ingin konsultasi website dan audit keamanan.`
      );

      window.open(`https://wa.me/6287805718296?text=${waText}`, "_blank", "noopener");

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

  /* ══════════════════════════════════════════════════════════
     ANIMATIONS — Scroll Reveal, Counters, Marquee, Tilt
     ══════════════════════════════════════════════════════════ */

  /* ── 1. Add reveal classes to elements ─────────── */
  function setupRevealClasses() {
    // Section headers
    document.querySelectorAll(".section-header").forEach((el) => {
      el.classList.add("reveal");
    });

    // Hero elements
    const heroCopy = document.querySelector(".hero-copy");
    const heroVisual = document.querySelector(".hero-visual");
    if (heroCopy) heroCopy.classList.add("reveal", "reveal-left");
    if (heroVisual) heroVisual.classList.add("reveal", "reveal-right");

    // Grids with staggered children
    const staggerGrids = [
      { selector: ".problem-grid", childSelector: ".problem-card" },
      { selector: ".pillar-grid", childSelector: ".pillar-card" },
      { selector: ".service-grid", childSelector: ".service-card" },
      { selector: ".pricing-grid", childSelector: ".pricing-card" },
      { selector: ".case-grid", childSelector: ".case-card" },
      { selector: ".process-track", childSelector: ".process-step" },
    ];

    staggerGrids.forEach(({ selector, childSelector }) => {
      const grid = document.querySelector(selector);
      if (grid) {
        grid.classList.add("reveal-stagger");
        grid.querySelectorAll(childSelector).forEach((child) => {
          child.classList.add("reveal");
        });
      }
    });

    // Audit section
    const auditCopy = document.querySelector(".audit-copy");
    const auditReport = document.querySelector(".audit-report");
    if (auditCopy) auditCopy.classList.add("reveal", "reveal-left");
    if (auditReport) auditReport.classList.add("reveal", "reveal-right");

    // CTA section
    const ctaCopy = document.querySelector(".cta-copy");
    const ctaForm = document.querySelector(".contact-form");
    if (ctaCopy) ctaCopy.classList.add("reveal", "reveal-left");
    if (ctaForm) ctaForm.classList.add("reveal", "reveal-right");

    // FAQ items
    document.querySelectorAll(".faq-item").forEach((item) => {
      item.classList.add("reveal");
    });

    // Social proof
    const socialProof = document.querySelector(".social-proof");
    if (socialProof) socialProof.classList.add("reveal");

    // Trust badges
    const trustBadges = document.querySelector(".trust-badges");
    if (trustBadges) {
      trustBadges.querySelectorAll(".badge").forEach((badge) => {
        badge.classList.add("reveal");
      });
      trustBadges.classList.add("reveal-stagger");
    }
  }

  /* ── 2. IntersectionObserver for scroll reveal ─── */
  function initScrollReveal() {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (prefersReducedMotion) {
      // Immediately show everything
      document.querySelectorAll(".reveal").forEach((el) => {
        el.classList.add("visible");
      });
      return;
    }

    const observerOptions = {
      root: null,
      rootMargin: "0px 0px -60px 0px",
      threshold: 0.1,
    };

    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          revealObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);

    document.querySelectorAll(".reveal").forEach((el) => {
      revealObserver.observe(el);
    });
  }

  /* ── 3. Animated counter for case metrics ──────── */
  function initCounterAnimation() {
    const caseMetrics = document.querySelectorAll(".case-metric");
    if (!caseMetrics.length) return;

    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            animateCounter(entry.target);
            counterObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    caseMetrics.forEach((metric) => {
      // Store original text
      metric.dataset.target = metric.textContent.trim();
      counterObserver.observe(metric);
    });
  }

  function animateCounter(el) {
    const text = el.dataset.target;
    const duration = 1500;
    const start = performance.now();

    // Extract number and prefix/suffix
    const match = text.match(/^([^\d-]*)(-?\d+(?:\.\d+)?)(.*)/);
    if (!match) return;

    const prefix = match[1];
    const targetNum = parseFloat(match[2]);
    const suffix = match[3];
    const isFloat = text.includes(".");

    function update(now) {
      const elapsed = now - start;
      const progress = Math.min(elapsed / duration, 1);
      // Ease out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = targetNum * eased;

      if (isFloat) {
        el.textContent = prefix + current.toFixed(1) + suffix;
      } else {
        el.textContent = prefix + Math.round(current) + suffix;
      }

      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.textContent = text;
      }
    }

    el.textContent = prefix + "0" + suffix;
    requestAnimationFrame(update);
  }

  /* ── 4. Logo strip marquee ─────────────────────── */
  function initLogoMarquee() {
    const logoStrip = document.querySelector(".logo-strip");
    if (!logoStrip) return;

    // Get all existing children
    const items = Array.from(logoStrip.children);
    if (!items.length) return;

    // Create inner wrapper for marquee
    const inner = document.createElement("div");
    inner.className = "logo-strip-inner";

    // Move original items into inner
    items.forEach((item) => inner.appendChild(item));

    // Duplicate items for seamless loop
    items.forEach((item) => {
      const clone = item.cloneNode(true);
      inner.appendChild(clone);
    });

    logoStrip.appendChild(inner);
  }

  /* ── 5. Subtle tilt effect on cards ────────────── */
  function initTiltEffect() {
    const tiltCards = document.querySelectorAll(
      ".service-card, .pillar-card, .pricing-card, .case-card"
    );

    tiltCards.forEach((card) => {
      card.addEventListener("mousemove", (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        const rotateX = ((y - centerY) / centerY) * -3;
        const rotateY = ((x - centerX) / centerX) * 3;

        card.style.transform = `perspective(800px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-6px)`;
      });

      card.addEventListener("mouseleave", () => {
        card.style.transform = "";
      });
    });
  }

  /* ── 6. Parallax on hero glow ──────────────────── */
  function initParallax() {
    const heroGlow = document.querySelector(".hero-glow");
    if (!heroGlow) return;

    window.addEventListener("mousemove", (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 20;
      const y = (e.clientY / window.innerHeight - 0.5) * 20;
      heroGlow.style.transform = `translate(${x}px, ${y}px)`;
    }, { passive: true });
  }

  /* ── Initialize all animations ─────────────────── */
  function initAnimations() {
    setupRevealClasses();
    initScrollReveal();
    initCounterAnimation();
    initLogoMarquee();
    initTiltEffect();
    initParallax();
  }

  // Run after DOM is ready and loader is done
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => {
      // Slight delay to let the loader finish
      setTimeout(initAnimations, 100);
    });
  } else {
    setTimeout(initAnimations, 100);
  }
})();

