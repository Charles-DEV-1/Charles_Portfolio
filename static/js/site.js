const navToggle = document.querySelector(".nav-toggle");
const siteNav = document.querySelector(".site-nav");
const navLinks = document.querySelectorAll("[data-nav-link]");
const revealElements = document.querySelectorAll("[data-reveal]");
const contactForm = document.getElementById("contactForm");
const formMessage = document.getElementById("formMessage");
const projectsTrack = document.querySelector("[data-projects-track]");
const prevButton = document.querySelector("[data-carousel-prev]");
const nextButton = document.querySelector("[data-carousel-next]");

if (navToggle && siteNav) {
  navToggle.addEventListener("click", () => {
    const isOpen = siteNav.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      siteNav.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const sections = [...document.querySelectorAll("main section[id]")];

function updateActiveNav() {
  const offset = window.scrollY + 180;
  let currentId = sections[0]?.id;

  sections.forEach((section) => {
    if (offset >= section.offsetTop) {
      currentId = section.id;
    }
  });

  navLinks.forEach((link) => {
    const isActive = link.dataset.navLink === currentId;
    link.classList.toggle("is-active", isActive);
  });
}

window.addEventListener("scroll", updateActiveNav, { passive: true });
window.addEventListener("load", updateActiveNav);

if (revealElements.length) {
  const revealObserver = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) {
          return;
        }

        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    },
    { threshold: 0.16 },
  );

  revealElements.forEach((element) => revealObserver.observe(element));
}

if (projectsTrack && prevButton && nextButton) {
  const getScrollAmount = () => {
    const firstCard = projectsTrack.querySelector(".project-card");
    if (!firstCard) {
      return 320;
    }

    const styles = window.getComputedStyle(projectsTrack);
    const gap = Number.parseFloat(styles.columnGap || styles.gap || "16");
    return firstCard.getBoundingClientRect().width + gap;
  };

  prevButton.addEventListener("click", () => {
    projectsTrack.scrollBy({ left: -getScrollAmount(), behavior: "smooth" });
  });

  nextButton.addEventListener("click", () => {
    projectsTrack.scrollBy({ left: getScrollAmount(), behavior: "smooth" });
  });
}

function showFormMessage(message, type) {
  if (!formMessage) {
    return;
  }

  formMessage.textContent = message;
  formMessage.className = `form-message is-visible is-${type}`;
}

if (contactForm) {
  contactForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const submitButton = contactForm.querySelector(".submit-button");
    const originalLabel = submitButton.textContent;
    const payload = {
      fullName: document.getElementById("fullName").value.trim(),
      email: document.getElementById("email").value.trim(),
      message: document.getElementById("message").value.trim(),
    };

    if (!payload.fullName || !payload.email || !payload.message) {
      showFormMessage("Please fill in all fields before sending.", "error");
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = "Sending...";

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.message || "Something went wrong.");
      }

      contactForm.reset();
      showFormMessage(result.message, "success");
    } catch (error) {
      showFormMessage(error.message || "Unable to send message right now.", "error");
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = originalLabel;
    }
  });
}
