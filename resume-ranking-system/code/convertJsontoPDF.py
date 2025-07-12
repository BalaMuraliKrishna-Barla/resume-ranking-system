# import json
# from fpdf import FPDF
# import os

# # Load JSON data
# with open("synthetic_resumes.json", "r") as file:
#     resumes = json.load(file)

# # Create output directory
# os.makedirs("pdf_resumes", exist_ok=True)

# # Helper to create PDF
# def create_pdf(resume, index):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     def add_line(text, ln=True):
#         pdf.multi_cell(0, 10, txt=text)

#     add_line(f"Name: {resume['name']}")
#     add_line(f"Email: {resume['email']}")
#     add_line(f"Phone: {resume['phone']}")
#     add_line(f"Address: {resume['address']}")
#     add_line(f"Job Title: {resume['job_title']}")
#     add_line(f"Education: {resume['education']}")
#     add_line("Skills: " + ", ".join(resume['skills']))

#     add_line("Experience:")
#     for exp in resume['experience']:
#         add_line(f"  - Company: {exp['company']}")
#         add_line(f"    Title: {exp['title']}")
#         add_line(f"    Years: {exp['years']}")
#         add_line(f"    Description: {exp['description']}")

#     filename = f"pdf_resumes/resume_{index:04d}.pdf"
#     pdf.output(filename)

# # Generate PDFs
# for i, resume in enumerate(resumes, 1):
#     create_pdf(resume, i)

# print("PDF resumes generated in the 'pdf_resumes' folder.")


import json
from fpdf import FPDF
import os

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Resume", ln=True, align="C")
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 12)

    def section_body(self, text):
        self.multi_cell(0, 8, text)
        self.ln(2)

    def bullet_list(self, items):
        for item in items:
            self.cell(5)
            self.multi_cell(0, 8, f"- {item}")

        self.ln(2)

def create_pdf(resume, index):
    pdf = ResumePDF()
    pdf.add_page()
    pdf.set_font("Arial", "", 12)

    # Personal Info
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 10, resume['name'], ln=True)
    pdf.set_font("Arial", "", 12)
    pdf.cell(0, 8, f"Email: {resume['email']}", ln=True)
    pdf.cell(0, 8, f"Phone: {resume['phone']}", ln=True)
    pdf.multi_cell(0, 8, f"Address: {resume['address']}")
    pdf.ln(4)

    pdf.section_title("Career Summary")
    pdf.section_body(resume['summary'])

    pdf.section_title("Skills")
    pdf.bullet_list(resume['skills'])

    pdf.section_title("Education")
    pdf.section_body(resume['education'])

    if resume.get("certifications"):
        pdf.section_title("Certifications")
        pdf.bullet_list(resume['certifications'])

    pdf.section_title("Professional Experience")
    for exp in resume['experience']:
        title_line = f"{exp['title']} at {exp['company']} ({exp['years']} years)"
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 8, title_line, ln=True)
        pdf.set_font("Arial", "", 12)
        pdf.multi_cell(0, 8, exp['description'])
        pdf.ln(2)

    os.makedirs("pdf_resumes", exist_ok=True)
    filename = f"pdf_resumes/resume_{index:04d}.pdf"
    pdf.output(filename)

# Load resumes from JSON and convert
with open("resumes.json", "r") as file:
    resumes = json.load(file)

for i, resume in enumerate(resumes, 1):
    create_pdf(resume, i)

print("All resumes converted to PDF in the 'pdf_resumes' folder.")
