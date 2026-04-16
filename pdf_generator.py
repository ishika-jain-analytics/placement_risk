from flask import make_response
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import io


def generate_pdf(data):
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Placement Risk Report", styles['Title']))
    content.append(Spacer(1, 20))

    # Section 1
    content.append(Paragraph("Section 1: User Input", styles['Heading2']))
    content.append(Paragraph(f"CGPA: {data.get('cgpa')}", styles['Normal']))
    content.append(Paragraph(f"Internship Months: {data.get('internship')}", styles['Normal']))
    content.append(Paragraph(f"Course: {data.get('course')}", styles['Normal']))
    content.append(Paragraph(f"Tier: {data.get('tier')}", styles['Normal']))
    content.append(Paragraph(f"Market Sentiment: {data.get('sentiment')}", styles['Normal']))

    content.append(Spacer(1, 15))

    # Section 2
    content.append(Paragraph("Section 2: Prediction Result", styles['Heading2']))
    content.append(Paragraph(f"Risk: {data.get('risk')}", styles['Normal']))
    content.append(Paragraph(f"Salary: {data.get('salary')}", styles['Normal']))
    content.append(Paragraph(f"Timeline: {data.get('timeline')}", styles['Normal']))

    content.append(Spacer(1, 15))

    # Section 3
    content.append(Paragraph("Section 3: AI Insights", styles['Heading2']))
    content.append(Paragraph(f"Recommendation: {data.get('recommendation')}", styles['Normal']))

    doc.build(content)

    buffer.seek(0)

    response = make_response(buffer.getvalue())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=placement_report.pdf'

    return response