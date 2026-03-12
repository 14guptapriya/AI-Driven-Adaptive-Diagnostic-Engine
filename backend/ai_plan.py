from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_study_plan(topics_wrong, ability):

    prompt = f"""
You are an AI tutor for an adaptive diagnostic test system.

Ability score (0 to 1): {ability}

Weak topics:
{topics_wrong}

Tasks:
1. Determine ability level (Beginner, Intermediate, Advanced)
2. Suggest topics to revise
3. Give short practice advice

Keep response concise (max 6 lines).
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role":"user","content":prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content