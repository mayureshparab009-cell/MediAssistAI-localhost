# Installation and Setup Guide - MediAssistAI

This guide provides step-by-step instructions to configure, install, and run the **MediAssistAI** application on a local development machine.

---

## Prerequisites
Ensure the following tools are installed on your machine:
1. **Node.js** (v18 or higher) & **npm** (v9 or higher)
2. **Python** (v3.9 or higher) & **pip**
3. **Git** (optional, for version control)

---

## Folder Structure Overview
The project is split into two main sections:
* `backend/`: Flask web API server, SQLAlchemy database management, SQLite database, and local AI chatbot engine.
* `frontend/`: React client using Vite, Outfit typography, and a custom glassmorphism design system.

---

## Step 1: Clone or Extract the Project
If you have downloaded the zip archive, extract the files to a directory of your choice (e.g., `C:\Projects\MediAssistAI`).

---

## Step 2: Setup Backend (Flask + SQLite)

1. Open a terminal and navigate to the backend folder:
   ```bash
   cd backend
   ```

2. Create a virtual environment (recommended):
   * **Windows (PowerShell/CMD):**
     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```
   * **macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask application:
   ```bash
   python app.py
   ```
   * The backend server will initialize the SQLite database automatically (`backend/mediassist.db`) and seed it with dummy patient logs.
   * The server runs on **`http://localhost:5000`**. Keep this terminal open.

---

## Step 3: Setup Frontend (React + Vite)

1. Open a **second terminal** and navigate to the frontend folder:
   ```bash
   cd frontend
   ```

2. Install the frontend dependencies:
   ```bash
   npm install
   ```

3. Run the Vite development server:
   ```bash
   npm run dev
   ```
   * The React interface will build and launch on **`http://localhost:5173`**.
   * Open this URL in your web browser.

---

## Step 4: Verification Checklist

1. **Dashboard Loading:** The circular adherence ring should load, displaying a score based on mock seed database records.
2. **Medication Logs:** Today's medication checklist should display (Aspirin, Metformin). Check "Taken" on a dose and verify the adherence score updates instantly.
3. **Adding a Medication:** Go to the "Schedule" tab, click "Add Medication", fill out the form, and save. Check that it is added to the active schedule.
4. **Symptom Tracker:** Go to the "Symptom Diary" tab, slide the severity rating to 7, write a note, and submit. Ensure the severity chart plots the new coordinate.
5. **AI Assistant:** Go to the "AI Assistant" tab, click a suggested question like "What if I miss a dose?" and verify the assistant responds with structured guidance.

---

## Troubleshooting

* **Frontend displays "Backend Server Offline" banner:**
  Ensure the Flask application is running successfully on port 5000. If port 5000 is occupied, you can change the port in `backend/app.py` and modify the proxy port in `frontend/vite.config.js` to match.
* **Database errors on startup:**
  If you face SQLite schema lockups, delete `backend/mediassist.db` and run `python app.py` again. The backend will regenerate a clean database and re-seed it automatically.
