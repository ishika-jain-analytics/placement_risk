from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(data):
    filename = "placement_report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(300, 750, "AI Placement Risk Report")

    # Section 1: User Input
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 710, "Section 1: User Input")
    c.setFont("Helvetica", 12)
    c.drawString(120, 690, f"CGPA: {data.get('cgpa')}")
    c.drawString(120, 670, f"Internship Months: {data.get('internship')}")
    c.drawString(120, 650, f"Course: {data.get('course')}")
    c.drawString(120, 630, f"Tier: {data.get('tier')}")
    c.drawString(120, 610, f"Market Sentiment: {data.get('sentiment')}")

    # Section 2: Prediction Result
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 580, "Section 2: Prediction Result")
    c.setFont("Helvetica", 12)
    c.drawString(120, 560, f"Risk: {data.get('risk')}")
    c.drawString(120, 540, f"Salary: {data.get('salary')}")
    c.drawString(120, 520, f"Timeline: {data.get('timeline')}")

    # Section 3: AI Insights
    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, 490, "Section 3: AI Insights")
    c.setFont("Helvetica", 12)
    c.drawString(120, 470, f"Recommendation: {data.get('recommendation')}")

    c.save()
    return filename
