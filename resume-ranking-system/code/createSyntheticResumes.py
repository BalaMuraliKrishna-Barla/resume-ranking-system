# import random
# from faker import Faker
# import json

# fake = Faker()
# Faker.seed(42)
# random.seed(42)

# # Sample job titles, skills, and education levels
# job_titles = [
#     "Software Engineer", "Data Analyst", "Project Manager", "Marketing Specialist", 
#     "Sales Executive", "Human Resources Manager", "UX Designer", "Product Manager"
# ]

# skills_pool = [
#     "Python", "SQL", "Java", "Excel", "Leadership", "Project Management", 
#     "Communication", "Data Visualization", "Machine Learning", "SEO", "AWS"
# ]

# education_levels = [
#     "Bachelor of Science in Computer Science",
#     "Master of Business Administration",
#     "Bachelor of Arts in Marketing",
#     "PhD in Data Science",
#     "Associate Degree in Graphic Design"
# ]

# # Function to generate a single resume
# def generate_resume():
#     name = fake.name()
#     email = fake.email()
#     phone = fake.phone_number()
#     address = fake.address().replace("\n", ", ")
#     job_title = random.choice(job_titles)
#     skills = random.sample(skills_pool, k=random.randint(4, 7))
#     education = random.choice(education_levels)
#     experience_years = random.randint(1, 15)
#     experience = [{
#         "company": fake.company(),
#         "title": job_title,
#         "years": experience_years,
#         "description": fake.paragraph(nb_sentences=3)
#     } for _ in range(random.randint(1, 3))]

#     return {
#         "name": name,
#         "email": email,
#         "phone": phone,
#         "address": address,
#         "job_title": job_title,
#         "skills": skills,
#         "education": education,
#         "experience": experience
#     }

# # Generate 1000 resumes
# resumes = [generate_resume() for _ in range(10)]

# # Optional: Save to JSON
# with open("synthetic_resumes.json", "w") as f:
#     json.dump(resumes, f, indent=2)

# print("Generated 1000 synthetic resumes and saved to 'synthetic_resumes.json'")



import random
from faker import Faker
import json

from numpy import number

fake = Faker()
Faker.seed(42)
random.seed(42)

job_titles = [
    "Software Engineer", "Data Analyst", "Project Manager", "Marketing Specialist", 
    "Sales Executive", "Human Resources Manager", "UX Designer", "Product Manager"
]

skills_pool = [
    "Python", "SQL", "Java", "C++", "Excel", "Leadership", "Project Management", 
    "Communication", "Data Visualization", "Machine Learning", "SEO", "AWS", "Docker", "React", "Agile"
]

education_levels = [
    "Bachelor of Science in Computer Science",
    "Master of Business Administration",
    "Bachelor of Arts in Marketing",
    "PhD in Data Science",
    "Bachelor of Engineering in Information Technology",
    "Master of Science in Human Resource Management"
]

certifications = [
    "AWS Certified Solutions Architect",
    "PMP - Project Management Professional",
    "Google Data Analytics Certificate",
    "Certified Scrum Master (CSM)",
    "Adobe Certified Expert (ACE)"
]

def generate_resume():
    name = fake.name()
    email = fake.email()
    phone = fake.phone_number()
    address = fake.address().replace("\n", ", ")
    job_title = random.choice(job_titles)
    skills = random.sample(skills_pool, k=random.randint(6, 10))
    education = random.choice(education_levels)
    certs = random.sample(certifications, k=random.randint(0, 2))
    summary = fake.paragraph(nb_sentences=3)

    experience = []
    for _ in range(random.randint(2, 4)):
        years = random.randint(1, 5)
        exp = {
            "company": fake.company(),
            "title": random.choice(job_titles),
            "years": years,
            "description": "\n".join(fake.paragraphs(nb=2))
        }
        experience.append(exp)

    return {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "job_title": job_title,
        "summary": summary,
        "skills": skills,
        "education": education,
        "certifications": certs,
        "experience": experience
    }

# Generate 1000 rich resumes
number_of_resumes = 10
resumes = [generate_resume() for _ in range(number_of_resumes)]

with open("resumes.json", "w") as f:
    json.dump(resumes, f, indent=2)

print(f"Generated {number_of_resumes} rich synthetic resumes and saved to 'synthetic_resumes.json'")
