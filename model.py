def predict_risk(data):
    cgpa = data.get("cgpa", 0)
    internship = data.get("internship", 0)

    if cgpa < 6.5 and internship == 0:
        risk = "High"
        timeline = "Placement may take 12+ months"
        salary = "₹3-5 LPA"
        recommendation = "Focus on skill-building and certifications."
    elif cgpa > 8 and internship > 3:
        risk = "Low"
        timeline = "Placement likely within 3-6 months"
        salary = "₹8-12 LPA"
        recommendation = "Strong profile. Target top-tier companies."
    else:
        risk = "Medium"
        timeline = "Placement may take 6-9 months"
        salary = "₹5-8 LPA"
        recommendation = "Improve portfolio and networking."

    return {
        "risk": risk,
        "timeline": timeline,
        "salary": salary,
        "recommendation": recommendation
    }
