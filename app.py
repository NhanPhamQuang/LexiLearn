from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"

# 10 questions
questions = [
    {"question": "She _____ to school every day.",
     "options": ["go", "goes", "went", "gone"],
     "answer": "goes"},

    {"question": "They have been friends _____ 2010.",
     "options": ["since", "for", "from", "at"],
     "answer": "since"},

    {"question": "If I _____ rich, I would travel the world.",
     "options": ["am", "was", "were", "be"],
     "answer": "were"},

    {"question": "He is looking forward to _____ you.",
     "options": ["see", "seeing", "saw", "seen"],
     "answer": "seeing"},

    {"question": "There isn't _____ milk left.",
     "options": ["many", "much", "few", "several"],
     "answer": "much"},

    {"question": "She speaks English _____ than her sister.",
     "options": ["good", "well", "better", "best"],
     "answer": "better"},

    {"question": "I forgot _____ the door.",
     "options": ["lock", "to lock", "locking", "locked"],
     "answer": "to lock"},

    {"question": "This is the _____ movie I've seen.",
     "options": ["more interesting", "most interesting", "interesting", "very interesting"],
     "answer": "most interesting"},

    {"question": "He asked me where I _____ from.",
     "options": ["am", "was", "were", "be"],
     "answer": "was"},

    {"question": "Neither Tom nor Jerry _____ at home.",
     "options": ["is", "are", "were", "be"],
     "answer": "is"},
]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/start", methods=["POST"])
def start():
    session["score"] = 0
    session["current"] = 0
    session["quiz"] = random.sample(questions, 5)
    return redirect("/quiz")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        selected = request.form.get("answer")
        current_q = session["quiz"][session["current"]]
        if selected == current_q["answer"]:
            session["score"] += 1
        session["current"] += 1

    if session["current"] >= 5:
        return redirect("/result")

    question = session["quiz"][session["current"]]
    return render_template("quiz.html", question=question)

@app.route("/result")
def result():
    score = session.get("score", 0)
    return render_template("result.html", score=score)

if __name__ == "__main__":
    app.run(debug=True)
