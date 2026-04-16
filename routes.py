from flask import Blueprint, render_template, request, send_file
from model import predict_risk
from database import db, Prediction
from pdf_generator import generate_pdf

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/predict", methods=["POST"])
def predict():
    try:
        data = {
            "cgpa": float(request.form["cgpa"]),
            "internship": int(request.form["internship"]),
            "course": request.form["course"],
            "tier": request.form["tier"],
            "sentiment": request.form["sentiment"]
        }

        result = predict_risk(data)

        # 🔥 dynamic percentage logic
        risk_map = {
            "LOW": 85,
            "MEDIUM": 60,
            "HIGH": 30
        }
        percent = risk_map.get(result["risk"], 50)

        # Save to DB
        record = Prediction(**data, **result)
        db.session.add(record)
        db.session.commit()

        return render_template("result.html",
                               result=result,
                               percent=percent)

    except Exception as e:
        return f"Error: {str(e)}"


@main.route("/download")
def download():
    data = request.args.to_dict()
    file = generate_pdf(data)
    return send_file(file, as_attachment=True)