# ⚽ Football AI Scouting Platform

An AI-powered web application for analyzing and ranking football players based on performance statistics using Machine Learning.

This platform helps evaluate player performance using key metrics such as goals, assists, passes, and rating to generate an **AI Score** and recommend top-performing players.

---

# 🌐 Live Demo


Frontend
https://football-ai-scouting-platform.vercel.app/

Backend
https://football-ai-scouting-platform.onrender.com/

---

# 📌 Project Overview

The Football AI Scouting Platform is a data-driven system designed to assist football scouts and analysts in evaluating player performance.

The system collects player statistics and applies a scoring algorithm to generate an **AI Score**, allowing users to identify the best players based on performance data.

The application includes:

- Player performance analysis
- AI score prediction
- Top player ranking
- Data visualization dashboard

---

# 🚀 Features

- AI-based player performance analysis
- Player ranking system
- Interactive dashboard
- Real-time AI score calculation
- Player statistics visualization
- Modern responsive UI design
- REST API for player data management

---

# 🧠 AI Model

The AI score is calculated using weighted player statistics.

| Feature | Weight |
|------|------|
| Goals | 35% |
| Assists | 25% |
| Passes | 20% |
| Rating | 20% |

### AI Score Formula


AI Score =
(goals × 0.5 × 0.35) +
(assists × 0.4 × 0.25) +
(passes × 0.15 × 0.20) +
(rating × 1.5 × 0.20)


This formula helps evaluate a player's overall performance based on attacking contribution and playmaking ability.

---

# 🏗 System Architecture


Frontend (HTML, CSS, JavaScript)
↓
FastAPI Backend (Python)
↓
AI Scoring Model
↓
SQLite Database


---

# 🛠 Technologies Used

## Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js
- Responsive UI Design

## Backend

- Python
- FastAPI
- Uvicorn
- REST API

## Database

- SQLite

## Deployment

- Vercel (Frontend)
- Render (Backend)

---

# 📂 Project Structure


football-ai-scouting-platform
│
├── backend
│ ├── main.py
│ ├── ai_model.py
│ ├── crud.py
│ ├── database.py
│ ├── models.py
│ └── schemas.py
│
├── database
│ └── players.db
│
├── dataset
│ └── players_sample.csv
│
├── frontend
│ ├── index.html
│ ├── dashboard.html
│ ├── app.js
│ └── style.css
│
├── requirements.txt
└── README.md


---

# ⚙ Installation

Clone the repository


git clone https://github.com/yourusername/football-ai-scouting-platform.git


Enter project directory


cd football-ai-scouting-platform


Install dependencies


pip install -r requirements.txt


---

# ▶ Running the Backend

Navigate to the backend folder


cd backend


Run FastAPI server


uvicorn main:app --reload


Server will start at


http://127.0.0.1:8000


API documentation available at


http://127.0.0.1:8000/docs


---

# 🌐 Running the Frontend

Open the file


frontend/index.html


in your browser.

Make sure the API endpoint in `app.js` is configured correctly:


const API_BASE = "http://127.0.0.1:8000
"


For deployed version:


const API_BASE = "https://football-api.onrender.com
"


---

# 📊 Example Output

The system provides:

- AI Score calculation
- Top recommended players
- Player ranking chart
- Performance analytics

---

# 👨‍💻 Author

Student Project  
Artificial Intelligence / Data Mining Course

---

# 📜 License

This project is for educational purposes.
