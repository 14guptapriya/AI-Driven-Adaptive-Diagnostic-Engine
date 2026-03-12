from fastapi import FastAPI
from database import questions_collection, sessions_collection
from adaptive_engine import update_ability
from models import AnswerSubmission
from bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from ai_plan import generate_study_plan
import uuid

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start-session")
def start_session():

    session = {
        "session_id": str(uuid.uuid4()),
        "ability_score": 0.5,
        "answered": [],
        "correct": 0,
        "topics_wrong": []
    }

    sessions_collection.insert_one(session)

    return {
        "session_id": session["session_id"],
        "ability_score": 0.5
    }


@app.get("/next-question")
def next_question(session_id: str):

    session = sessions_collection.find_one({"session_id": session_id})

    ability = session["ability_score"]
    answered = session["answered"]

    # STOP AFTER 10 QUESTIONS
    if len(answered) >= 10:

        try:
             plan = generate_study_plan(session["topics_wrong"], ability)
        except:
            plan = "Revise weak topics and practice more questions."

        return {
            "test_complete": True,
            "ability_score": ability,
            "questions_attempted": len(answered),
            "study_plan": plan
        }

    questions = list(
        questions_collection.find(
            {"_id": {"$nin": [ObjectId(q) for q in answered]}}
        )
    )

    q = min(questions, key=lambda x: abs(x["difficulty"] - ability))

    return {
        "question_id": str(q["_id"]),
        "question": q["question"],
        "options": q["options"],
        "q_no": len(answered) + 1,
        "total_questions": 10
    }


@app.post("/submit-answer")
def submit_answer(data:AnswerSubmission):

    session = sessions_collection.find_one({"session_id":data.session_id})

    if not session:
        return {"error":"Invalid session"}

    question = questions_collection.find_one({"_id":ObjectId(data.question_id)})

    if not question:
        return {"error":"Question not found"}

    correct = data.answer == question["correct_answer"]

    ability = update_ability(session["ability_score"],correct)

    update_data = {
        "$set":{"ability_score":ability},
        "$push":{"answered":data.question_id}
    }

    if correct:
        update_data["$inc"] = {"correct":1}
    else:
        update_data["$push"]["topics_wrong"] = question["topic"]

    sessions_collection.update_one(
        {"session_id":data.session_id},
        update_data
    )

    return {
        "correct":correct,
        "ability":ability
    }