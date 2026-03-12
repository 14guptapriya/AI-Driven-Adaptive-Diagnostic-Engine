# AI Driven Adaptive Diagnostic Engine

## Overview

This project is an **AI-driven adaptive diagnostic test system** that dynamically adjusts question difficulty based on the student's performance.
The system estimates the learner’s ability score and selects the most appropriate next question.

At the end of the test, the system generates a **personalized AI study plan** based on the student’s weak topics.

---

# Features

* Adaptive question selection based on ability score
* Ability score updated after every answer
* Difficulty-based question matching
* Weak topic tracking
* AI-generated study plan
* REST API built with FastAPI
* MongoDB database for storing questions and sessions
* Simple frontend using HTML, CSS, and JavaScript

---

# Project Structure

```
AI-Driven-Adaptive-Diagnostic-Engine
│
├── backend
│   ├── main.py
│   ├── adaptive_engine.py
│   ├── database.py
│   ├── models.py
│   ├── ai_plan.py
│   └── requirements.txt
│
├── frontend
│   ├── index.html
│   ├── result.html
│   ├── script.js
│   └── style.css
│
└── README.md
```

---

# How to Run the Project

## 1. Clone the repository

```
git clone https://github.com/14guptapriya/AI-Driven-Adaptive-Diagnostic-Engine.git
cd AI Driven Adaptive Diagnostic Engine 
```

---

## 2. Install dependencies

Create a virtual environment:

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install required packages:

```
pip install -r requirements.txt
```

---

## 3. Set API Key

Create an environment variable for the Groq API:

Windows:

```
set GROQ_API_KEY=your_api_key
```

Mac/Linux:

```
export GROQ_API_KEY=your_api_key
```

---

## 4. Run the backend server

```
uvicorn main:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

---

## 5. Run the frontend

Navigate to the frontend folder and start a simple server:

```
cd frontend
live-server
```

Or simply open `index.html` in a browser.

---

# Adaptive Algorithm Logic

The adaptive engine estimates the student's **ability score** (range: 0–1).

### Initial Ability

The test begins with a default ability score:

```
ability = 0.5
```

### After Each Question

The ability score is updated using the following logic:

* If the student answers correctly → ability increases
* If incorrect → ability decreases

Example update logic:

```
new_ability = old_ability + 0.05   (correct)
new_ability = old_ability - 0.05   (incorrect)
```

### Question Selection

For the next question, the system selects the question whose **difficulty level is closest to the student's ability score**.

```
min(|question_difficulty - ability|)
```

This ensures the test continuously adapts to the learner’s skill level.

### Test Completion

The test ends after:

```
10 questions
```

Then the system:

1. Calculates the final ability score
2. Identifies weak topics
3. Generates an AI-based study plan

---

# AI Study Plan Generation

The project uses **Groq API with the Llama model** to generate personalized study recommendations.

Inputs to the AI model:

* Student ability score
* Topics answered incorrectly

The AI returns:

* Ability level
* Topics to revise
* Suggested practice strategy

---

# AI Log

During development, AI tools such as **ChatGPT** were used to accelerate development.

### How AI Helped

* Designing the FastAPI backend structure
* Debugging API errors
* Generating frontend UI improvements
* Creating prompts for AI-based study plan generation
* Structuring the adaptive question selection logic

### Challenges AI Couldn't Fully Solve

* Debugging real-time API errors (rate limits, environment variables)
* Integrating frontend with backend endpoints
* Handling session logic and database updates correctly
* Designing a clean adaptive algorithm without overfitting

Manual debugging and testing were required to resolve these issues.

---

# API Documentation

## Start Test Session

```
POST /start-session
```

Creates a new test session.

Response:

```
{
  "session_id": "uuid",
  "ability_score": 0.5
}
```

---

## Get Next Question

```
GET /next-question
```

Query parameter:

```
session_id
```

Response:

```
{
  "question_id": "...",
  "question": "...",
  "options": ["A","B","C","D"],
  "q_no": 3
}
```

If test completes:

```
{
  "test_complete": true,
  "ability_score": 0.72,
  "questions_attempted": 10,
  "study_plan": "AI generated plan"
}
```

---

## Submit Answer

```
POST /submit-answer
```

Request body:

```
{
  "session_id": "...",
  "question_id": "...",
  "answer": "A"
}
```

Response:

```
{
  "correct": true,
  "ability": 0.65
}
```

---

# Future Improvements

* Implement Item Response Theory (IRT) based ability estimation
* Add visual analytics dashboard
* Track ability progression graph
* Add user login and test history
* Improve AI study recommendations

---

# Technologies Used

Backend:

* FastAPI
* Python

Database:

* MongoDB

Frontend:

* HTML
* CSS
* JavaScript

AI Integration:

* Groq API
* Llama Model

---

