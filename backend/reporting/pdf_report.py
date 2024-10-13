from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from backend.reporting.visualization import generate_vulnerability_charts

def generate_pdf_report(findings, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Security Scan Report")

    text_object = c.beginText(100, 700)
    text_object.setFont("Helvetica", 10)
    
    for finding in findings:
        text_object.textLine(finding)
    
    c.drawText(text_object)
    generate_vulnerability_charts(findings)
    c.drawImage('vulnerability_chart.png', 100, 400, width=400, height=200)

    c.save()
