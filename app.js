const dayData = {
  1: {
    title: "Controlled Environment Agriculture Discovery Day",
    intro: "Welcome to Day 1 of AIFS Summer Camp. Choose the learning resource you want to open.",
    workshopDescription:
      "Interactive facility exploration where students observe plant growth systems, ask questions, and identify key components used in indoor farming.",
    materialFile: "slides/day1-in-class.pdf",
    workshopFile: "slides/day1-workshop/"
  },

  2: {
    title: "Sensors and IoT Systems in Greenhouse",
    intro: "Welcome to Day 2 of AIFS Summer Camp. Choose the learning resource you want to open.",

    materialDescription:
      "Two lecture modules are provided: one on greenhouse sensors and IoT systems, and one on AI/ML connections in controlled environment agriculture.",

    workshopDescription:
      "Hands-on sensor data collection with Arduino and Raspberry Pi, including sensor connection, data display, and basic interpretation.",

    materialFiles: [
      {
        label: "📡 IoT Lecture",
        file: "slides/day2-iot.html"
      },
      {
        label: "🤖 AI/ML Lecture",
        file: "slides/day2-ai-ml-lecture.html"
      }
    ],

    workshopFile: "slides/day2-workshop.html"
  },

  3: {
    title: "Imaging Systems in Greenhouse",
    intro: "Welcome to Day 3 of AIFS Summer Camp. Choose the learning resource you want to open.",
    materialDescription:
      "Introduction to imaging systems, machine vision, and how image analysis can be used to monitor plant growth, detect stress, and support automated farming.",
    workshopDescription:
      "Hands-on Raspberry Pi camera activity where students capture plant images and explore basic image-based plant monitoring.",
    materialFile: "slides/day3-in-class.html",
    workshopFile: "slides/day3-workshop.html"
  },

  4: {
    title: "Artificial Lighting and Imaging in the CEA",
    intro: "Welcome to Day 4 of AIFS Summer Camp. Choose the learning resource you want to open.",
    materialDescription:
      "Introduction to plant-lighting concepts, including daily light integral, photosynthetic photon flux density, light-use efficiency, and lighting applications in computer vision.",
    workshopDescription:
      "Hands-on computer vision image training with experimental data for controlled environment agriculture applications.",
    materialFile: "slides/day4-in-class.html",
    workshopFile: "slides/day4-workshop.html"
  }
};

function getQueryValue(key) {
  const params = new URLSearchParams(window.location.search);
  return params.get(key);
}

function setupDayPage() {
  const day = getQueryValue("day");
  const data = dayData[day];

  if (!data) return;

  document.title = `AIFS Summer Camp - Day ${day}`;
  document.getElementById("day-heading").textContent = `Day ${day}`;
  document.getElementById("day-title").textContent = data.title;
  document.getElementById("day-intro").textContent = data.intro;

  const materialButtons = document.getElementById("material-buttons");
  const materialLink = document.getElementById("material-link");
  const workshopLink = document.getElementById("workshop-link");

  const materialDescriptionRow = document.getElementById("material-description-row");
  const materialDescription = document.getElementById("material-description");
  const workshopDescription = document.getElementById("workshop-description");

  workshopLink.href = data.workshopFile;
  workshopDescription.textContent = data.workshopDescription;

  /*
    Day 1: hide in-class material.
    Days 2–4: show in-class material.
  */
  if (String(day) === "1") {
    materialLink.style.display = "none";

    if (materialDescriptionRow) {
      materialDescriptionRow.style.display = "none";
    }

    return;
  }

  /*
    If this day has multiple lecture files, create multiple buttons.
    Example: Day 2 has IoT Lecture and AI/ML Lecture.
  */
  if (data.materialFiles && data.materialFiles.length > 0) {
    materialLink.style.display = "none";

    data.materialFiles.forEach((item) => {
      const newButton = document.createElement("a");
      newButton.className = "nav-button material";
      newButton.href = item.file;
      newButton.textContent = item.label;

      materialButtons.insertBefore(newButton, workshopLink);
    });

    if (materialDescriptionRow) {
      materialDescriptionRow.style.display = "list-item";
    }

    materialDescription.textContent = data.materialDescription;

    return;
  }

  /*
    Default case: one in-class material button.
  */
  materialLink.style.display = "inline-flex";
  materialLink.href = data.materialFile;

  if (materialDescriptionRow) {
    materialDescriptionRow.style.display = "list-item";
  }

  materialDescription.textContent = data.materialDescription;
}

function setupViewerPage() {
  const day = getQueryValue("day");
  const type = getQueryValue("type");
  const data = dayData[day];

  if (!data) return;

  let filePath = "";
  let label = "";

  if (type === "material") {
    filePath = data.materialFile;
    label = "In-Class Material";
  } else if (type === "workshop") {
    filePath = data.workshopFile;
    label = "Workshop";
  } else {
    return;
  }

  document.title = `Day ${day} - ${label}`;
  document.getElementById("viewer-title").textContent =
    `Day ${day}: ${label} - ${data.title}`;

  document.getElementById("pdf-frame").src = filePath;
  document.getElementById("back-to-day").href = `day.html?day=${day}`;
}

if (document.getElementById("day-heading")) {
  setupDayPage();
}

if (document.getElementById("pdf-frame")) {
  setupViewerPage();
}