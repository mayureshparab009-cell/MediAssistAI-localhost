# MediAssistAI - Smart Medication Tracker & AI Health Companion

[![UN SDG Goal 3](https://img.shields.io/badge/SDG-Goal%203%3A%20Good%20Health%20%26%20Well--Being-emerald?style=for-the-badge)](https://sdgs.un.org/goals/goal3)

MediAssistAI is an AI-powered healthcare assistant application designed to combat medication non-adherence and facilitate symptom and vitals tracking. Built using **React (Vite)** on the frontend and **Flask (Python)** with **SQLite** on the backend, the application serves as a comprehensive tool to help patients, especially those with chronic diseases or elderly individuals, manage their prescriptions, monitor vital signs, and track daily symptoms.

This project is created in alignment with **United Nations Sustainable Development Goal 3 (Good Health and Well-being)**.

---

## 📸 Interface Preview
The user interface features a premium dark-themed **glassmorphic design** utilizing Outfit & Inter typography:
* **Dashboard:** Features dynamic compliance circular gauges, rolling 7-day adherence charts, recent vitals summaries, and today's schedule checklist.
* **Scheduler:** Manage medications, dosage details, custom times, and specific meal instructions.
* **Symptom Diary:** Input physical symptoms, severity ratings (1-10 slider), and monitor severity trends on an SVG coordinates line graph.
* **Vitals Tracker:** Record key health vitals (systolic/diastolic blood pressure, blood glucose levels, and heart pulse rate) and plot custom multi-line SVG charts.
* **AI Medical Companion:** Conversational chat interface to ask queries about drug summaries, side effects, and warning notifications on clinical emergencies.

---

## 🎯 SDG 3 alignment & Problem Statement
* **The Crisis:** Medication non-adherence accounts for 125,000 avoidable deaths yearly and nearly 10% of hospital admissions. Elderly and chronic patients struggle to follow scheduled dosages and keep track of vital indicators.
* **The Solution:** MediAssistAI solves this by introducing a digital interactive checklist, tracking adherence scores, logging vitals history, keeping logs for doctors, and raising medical literacy using natural language chatbots.

---

## 🛠️ Technology Stack
* **Frontend:** React (Vite), Lucide-React, CSS variables and custom typography.
* **Backend:** Flask, Flask-CORS (Python 3).
* **Database:** SQLite (SQLAlchemy ORM).
* **AI Chatbot Engine:** Custom Localized Clinical Regex & Keyword Mapping Engine.

---

## 🚀 Installation & Running

For a detailed setup guide, please consult the [Installation Guide](file:///C:/Users/nares/.gemini/antigravity/scratch/MediAssistAI/INSTALLATION_GUIDE.md).

### Quick Start:

1. **Start Backend Server:**
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
   *Runs on `http://localhost:5000` (auto-seeds mock patient logs).*

2. **Start Frontend Client:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
   *Runs on `http://localhost:5173`.*

---

## 🗂️ Project Directory Structure
```
MediAssistAI/
├── .gitignore
├── README.md
├── INSTALLATION_GUIDE.md
├── PROJECT_REPORT_TEMPLATE.md
├── package.json
├── zip_project.py
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── database.py
│   ├── chatbot.py
│   ├── requirements.txt
│   └── mediassist.db (created automatically on startup)
└── frontend/
    ├── package.json
    ├── vite.config.js
    ├── index.html
    └── src/
        ├── main.jsx
        ├── App.jsx
        ├── index.css
        └── components/
            ├── Dashboard.jsx
            ├── MedicationManager.jsx
            ├── SymptomTracker.jsx
            ├── VitalsTracker.jsx
            ├── AIChatbot.jsx
            └── ReportGenerator.jsx
```


---

## 👥 Team & Submission Details * **Project Name:** MediAssistAI *
**SDG Target:** Goal 3 (Good Health and Well-being) *
**Academic Submission:** B.E COMPUTER SCIENCE AND ENGINEERING *
**Developer:** Mayuresh Parab.
