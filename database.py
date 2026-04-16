from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# ✅ FIRST define db
db = SQLAlchemy()

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    cgpa = db.Column(db.Float)
    internship = db.Column(db.Integer)
    course = db.Column(db.String(50))
    tier = db.Column(db.String(20))
    sentiment = db.Column(db.String(20))

    risk = db.Column(db.String(20))
    salary = db.Column(db.String(50))
    timeline = db.Column(db.String(50))
    recommendation = db.Column(db.Text)

    # ✅ FIXED timestamp
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)