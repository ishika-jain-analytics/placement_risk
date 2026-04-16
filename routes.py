from flask import Blueprint, render_template, request
from database import db, Prediction
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')


@main.route('/predict', methods=['POST'])
def predict():
    try:
        cgpa = float(request.form['cgpa'])
        internship = int(request.form['internship'])
        course = request.form['course']
        tier = request.form['tier']
        sentiment = request.form['sentiment']

        # 🔥 LOGIC
        score = 0

        if cgpa >= 8.5:
            score += 40
        elif cgpa >= 7:
            score += 25
        else:
            score += 10

        if internship >= 6:
            score += 30
        elif internship >= 3:
            score += 20
        else:
            score += 10

        if tier == "Tier 1":
            score += 20
        elif tier == "Tier 2":
            score += 10
        else:
            score += 5

        if sentiment == "Positive":
            score += 10
        elif sentiment == "Neutral":
            score += 5

        # 🎯 FINAL %
        risk_percent = min(score, 100)

        # 🎯 LABEL
        if risk_percent >= 70:
            risk_label = "Low"
        elif risk_percent >= 40:
            risk_label = "Medium"
        else:
            risk_label = "High"

        # 💰 OUTPUT
        if risk_label == "Low":
            salary = "₹8-12 LPA"
            timeline = "Placement likely within 3-6 months"
            recommendation = "Strong profile. Target top-tier companies."
        elif risk_label == "Medium":
            salary = "₹5-8 LPA"
            timeline = "Placement may take 6-9 months"
            recommendation = "Improve portfolio and networking."
        else:
            salary = "₹3-5 LPA"
            timeline = "Placement may take 9-12 months"
            recommendation = "Focus on skills, internships, and projects."

        # 🗄 SAVE
        prediction = Prediction(
            cgpa=cgpa,
            internship=internship,
            course=course,
            tier=tier,
            sentiment=sentiment,
            risk=risk_label,
            salary=salary,
            timeline=timeline,
            recommendation=recommendation,
            timestamp=datetime.utcnow()
        )

        db.session.add(prediction)
        db.session.commit()

        # 🔥 RESULT OBJECT (FIX)
        result = {
            "risk": risk_label,
            "salary": salary,
            "timeline": timeline,
            "recommendation": recommendation
        }

        # 🔥 FINAL RETURN (FIX)
        return render_template(
            'result.html',
            result=result,
            risk_percent=risk_percent
        )

    except Exception as e:
        return f"Error: {str(e)}"