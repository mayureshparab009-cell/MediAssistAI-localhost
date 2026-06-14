# PROJECT REPORT: MediAssistAI - AI Health & Medication Adherence Assistant
**Academic Submission / Portfolio Project**
**Aligned with United Nations Sustainable Development Goal 3 (Good Health and Well-being)**

---

## 1. Selected SDG and Reason for Selection
* **Selected SDG:** Goal 3: Good Health and Well-being.
* **Core Focus:** Ensuring healthy lives and promoting well-being for all at all ages.
* **Reason for Selection:**
  Medication non-adherence is a major global healthcare concern. Studies indicate that nearly 50% of patients with chronic diseases (such as hypertension, diabetes, and heart failure) fail to take their medications as prescribed. This non-adherence leads to approximately 125,000 avoidable deaths annually in the US alone and accounts for 10% of hospitalizations, placing a severe financial burden of over $100 billion per year on the healthcare system. Additionally, patients struggle to maintain cohesive logs of daily symptoms and vital signs (blood pressure, blood glucose, heart rate), leaving clinical doctors with insufficient data during check-ups. MediAssistAI addresses this gap directly by combining proactive schedule trackers, digital symptom diaries, vitals logging, and automated clinical guidance chatbot interfaces to raise medical adherence and healthcare literacy.

---

## 2. Problem Statement
* **The Core Problem:** Patient non-adherence to drug prescriptions, absence of historical symptom diaries and vitals logs, and low patient comprehension regarding drug side-effects.
* **Context / Scope:** Domestic patient care, particularly among elderly individuals managing multiple prescriptions (polypharmacy) and patients suffering from chronic illnesses.
* **Affected Stakeholders:**
  1. **Patients:** Who experience complications from missed doses.
  2. **Family Caregivers:** Who find it challenging to monitor medication intakes.
  3. **Clinicians:** Who lack reliable, objective patient history charts during consultation.
* **Seriousness of the Issue:** Skipped or incorrect doses trigger disease progression, toxic drug interactions, preventable emergency admissions, and increased mortality.
* **Unresolved Consequence:** Escalating healthcare costs, poor patient outcomes, and clinical inefficiency due to self-reported recall biases.

---

## 3. Objective
To design, implement, and validate a lightweight, locally deployable, intelligent medication scheduler, vitals logger, and symptom log analyzer that provides conversational clinical guidance to patients to boost prescription adherence rates and promote UN SDG 3 health standards.

---

## 4. Proposed Solution
**MediAssistAI** is an integrated health assistant application built using:
1. **React Frontend (Client):** Provides a glassmorphic dashboard showcasing daily dosage checklist, vitals summaries, adherence percentages, and symptom graphs.
2. **Flask Python (REST API Server):** Processes medication CRUD operations, vitals logs, auto-generates daily checklists, computes compliance statistics, and runs an intelligent local NLP chatbot engine.
3. **SQLite Database (Relational Store):** Stores client medication parameters, dosage intakes, vital logs, and symptom diaries.

### Workflow:
* The patient schedules a medication, selecting strength, frequency, start date, and instructions.
* The system auto-generates a checklist for today's required doses.
* Marking a dose as Taken updates compliance statistics.
* The patient logs daily symptoms (headaches, dizziness) with notes and severity ratings.
* The patient records vital logs (systolic/diastolic blood pressure, fasting blood glucose, pulse).
* The chatbot analyzes text queries, answering questions, giving drug summaries, and identifying emergency phrases (e.g. chest pain) to alert the user.

---

## 5. Technology Stack
* **Client Architecture:** React.js, Vite bundler, Outfit & Inter Google fonts, custom CSS design system.
* **Server Architecture:** Flask, Flask-CORS.
* **Database Layer:** SQLite, SQLAlchemy ORM.
* **Intelligent Chatbot Engine:** Python Regex & Natural Language processing dictionary.

---

## 6. Project Features
1. **Interactive Checklist:** A simple, high-contrast dashboard displaying medications scheduled for the current calendar day, marked dynamically.
2. **Compliance Analytics:** Custom mathematical SVG circular gauges representing average adherence, accompanied by rolling 7-day compliance bar charts.
3. **Symptom Severity Diary:** Forms to log symptoms, severities (1-10 slider), and text notes, coupled with automatic SVG line-graph coordinate generation showing symptom trends.
4. **Vitals Tracker:** Interface to input vital signs (blood pressure, blood glucose, heart rate) featuring custom dual-line SVG charts plotting systolic/diastolic blood pressure trends over time.
5. **Local AI Assistant:** Conversational engine responding to greeting, drug summaries (Aspirin, Metformin, Lisinopril), missed dose protocols, and flagging critical emergencies.
6. **Project Report Generator:** Dynamic client-side compiler summarizing student credentials and code statistics, exportable via Markdown download.

---

## 7. System Architecture
```
  [ React Client ]  <==== HTTP REST API ====>  [ Flask Server ]
   (Vite / CSS)                                 (Python / NLP)
         |                                            |
         v                                            v
 [ User Dashboard ]                            [ SQLAlchemy ]
 [ Symptom Charts ]                                   |
 [ Vitals Graphs ]                                    v
 [ Chat interface ]                           [ SQLite Database ]
                                              (mediassist.db)
```

---

## 8. Database Schema
* **Medication Table:**
  - `id` (Integer, Primary Key)
  - `name` (String, Required)
  - `dosage` (String, Required)
  - `frequency` (String, Required)
  - `time` (String, Comma-separated scheduled times)
  - `start_date` (String, YYYY-MM-DD)
  - `end_date` (String, Optional)
  - `instructions` (String)
  - `active` (Boolean)
* **MedicationLog Table:**
  - `id` (Integer, Primary Key)
  - `medication_id` (Integer, Foreign Key)
  - `date` (String, YYYY-MM-DD)
  - `time` (String, HH:MM)
  - `status` (String: Pending / Taken / Missed)
  - `logged_at` (DateTime, Stamp when Taken)
* **SymptomLog Table:**
  - `id` (Integer, Primary Key)
  - `date` (String, YYYY-MM-DD)
  - `symptom` (String, Required)
  - `severity` (Integer, 1 to 10)
  - `notes` (Text)
* **VitalsLog Table:**
  - `id` (Integer, Primary Key)
  - `date` (String, YYYY-MM-DD)
  - `systolic` (Integer, Required)
  - `diastolic` (Integer, Required)
  - `blood_sugar` (Integer, Required)
  - `heart_rate` (Integer, Required)
  - `logged_at` (DateTime)

---

## 9. Future Scope
1. **SMS Notifications:** Twilio API push integrations to alert patients on mobile phones.
2. **Prescription Scanner:** Google Vision OCR to parse prescription sheets and populate the medication scheduler.
3. **Multi-Patient Portals:** Enabling caregivers and clinical physicians to remotely view patient compliance charts.

---

## 10. Conclusion
MediAssistAI serves as an accessible digital intervention to combat medication non-adherence. By organizing scheduling, charting symptom timelines, logging key vitals, and teaching patients through conversational AI, the project delivers a functional, human-centric application that directly aligns with the objectives of UN SDG Goal 3.
