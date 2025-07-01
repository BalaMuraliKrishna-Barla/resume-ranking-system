**Appendix G**
**Academic Year 2025-26**
**IV B. Tech I Semester Project work**
**B. Tech Project Proposal**

**Name of the Supervisor:** Mrs. D.Amaravathi, Asst.Professor

**I. Project Group Details:**

| S.No | Batch Code | Register No | Name of the Student | E-Mail Id | Contact Number |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | 22CSEA15 | 22K61A05H5 | Vemulapalli Venkata Sai Vineetha | vineetha.vemulapalli@sasi.ac.in | 9014185433 |
| 2 | 22CSEA15 | 22K61A0582 | Krovvidi Sai Sesha Phani | sai.krovvidi@sasi.ac.in | 9551587927 |
| 3 | 22CSEA15 | 22K61A0511 | Barla Bala Murali Krishna | krishnamurali.barla@sasi.ac.in | 6301155348 |
| 4 | 22CSEA15 | 22K61A05E9 | Seelaboyina Naga Satya Sri | satyasri.seelaboyina@sasi.ac.in | 9704990397 |

**Tentative Title:** AI-Powered Intelligent Resume Ranking and Talent Matching System

**(Specific, clear, and reflects the main theme/problem)**

**Domain / Sub Domain:** Artificial Intelligence / Natural Language Processing (NLP)
**Area of the Project:** Human Resource Technology (HR-Tech) / Recruitment Automation

---

**II. Brief Description of the Project**

**1. Problem Statement:**
In today's competitive job market, recruiters are inundated with hundreds, sometimes thousands, of resumes for a single job opening. Manually screening these documents is an incredibly time-consuming, repetitive, and inefficient process. Traditional Applicant Tracking Systems (ATS) often rely on simple keyword matching (like TF-IDF), which fails to understand the context, semantics, and nuances of a candidate's experience. This leads to two major problems:
1.  **High False Negatives:** Highly qualified candidates are often overlooked because their resumes use different phrasings or synonyms (e.g., "managed a team" vs. "project lead") not explicitly listed in the job description.
2.  **Inherent Bias:** Human screeners and simplistic systems can be susceptible to unconscious biases related to name, gender, or background, hindering diversity and inclusion efforts.
There is a critical need for an intelligent system that can rank resumes not just on keywords, but on the semantic relevance of their content in relation to the job requirements, ensuring a fair and efficient initial screening process.

**2. Objective:**
1.  **To design and develop an advanced NLP pipeline** for parsing resumes from various formats (PDF, DOCX) and extracting structured information, including contact details, work experience, education, and key skills using Named Entity Recognition (NER).
2.  **To implement a semantic matching algorithm** using state-of-the-art sentence-transformer models (e.g., BERT-based) to generate contextual embeddings for both resumes and job descriptions, moving beyond simple keyword analysis.
3.  **To create a multi-faceted scoring system** that intelligently ranks candidates based on a weighted combination of semantic similarity, mandatory skill-set matching, and years of relevant experience.
4.  **To build a dynamic and user-friendly web-based dashboard** for recruiters to upload job descriptions, view a ranked list of applicants, and get explainable insights into why a candidate is ranked highly.
5.  **To evaluate the system's effectiveness** against a baseline keyword-based model, measuring performance in terms of ranking precision, recall, and processing efficiency on a curated dataset.

**3. Scope of the Project:**

**Covered:**
*   Parsing and information extraction from resumes in PDF and DOCX formats.
*   Semantic understanding of job descriptions and resume content.
*   Implementation of a hybrid ranking algorithm combining semantic similarity (via transformer embeddings) and explicit skill matching.
*   Development of a backend API to handle the processing logic.
*   A web interface for recruiters to post a job, view ranked candidates, and see key extracted information (skills, experience).
*   Providing an "explanation" for the ranking (e.g., "High match in leadership skills," "Meets 5/6 required technical skills").

**Excluded:**
*   Full-scale ATS features like interview scheduling, candidate communication, or offer management.
*   Real-time integration with job portals like LinkedIn or Indeed.
*   Multi-language resume parsing (the system will focus on English).
*   Predicting a candidate's future job performance or cultural fit.

**4. Proposed Methodology of Solution:**

Our proposed solution moves beyond the traditional TF-IDF and Cosine Similarity approach to a more robust, context-aware system.

*   **Step 1: Data Collection and Preprocessing:**
    *   **Dataset:** We will start with a publicly available synthetic resume dataset. To enhance realism and robustness, we will augment this by scraping and anonymizing publicly available resumes and job descriptions from various tech domains.
    *   **Resume Parsing:** We will use libraries like `PyMuPDF` for PDFs and `python-docx` for DOCX files to extract raw text. The text will then be cleaned (removing special characters, standardizing formatting) for downstream processing.

*   **Step 2: Information Extraction and Feature Engineering (The NLP Core):**
    *   **Named Entity Recognition (NER):** We will use a pre-trained NER model from `spaCy` to extract structured entities like `PERSON` (name), `EMAIL`, `PHONE`, `GPE` (location), `ORG` (companies), and `DATE` (experience duration).
    *   **Skill Extraction:** We will build a comprehensive skill library (e.g., 'Python', 'Java', 'React', 'AWS', 'Project Management') and use rule-based matching (regex) or `spaCy`'s `PhraseMatcher` to identify and extract a candidate's skills.
    *   **Semantic Embedding:** This is the key innovation. We will use a pre-trained **Sentence-Transformer model** (e.g., `all-MiniLM-L6-v2`) to convert the entire job description and the relevant sections of each resume (like work experience) into high-dimensional vectors (embeddings). These embeddings capture the semantic meaning, not just the words.

*   **Step 3: The Hybrid Ranking Algorithm:**
    1.  **Semantic Score:** Calculate the **Cosine Similarity** between the job description embedding and each resume's embedding. This score (0 to 1) represents the overall contextual fit.
    2.  **Skill Score:** Compare the list of skills required in the job description with the skills extracted from the resume. This can be a simple percentage match (e.g., `(matched_skills / required_skills) * 100`).
    3.  **Experience Score (Optional Extension):** Calculate the years of experience from the extracted `DATE` entities and compare it to the requirement in the job description.
    4.  **Final Weighted Score:** Combine these metrics into a single score:
        `Final Rank = (w1 * Semantic_Score) + (w2 * Skill_Score)`
        The weights (w1, w2) can be adjusted by the recruiter to prioritize contextual fit or hard skills.

*   **Step 4: System Architecture & Implementation:**
    *   **Backend:** A **Flask** application will serve as the API. It will expose endpoints like `/upload_job`, `/upload_resume`, and `/get_ranked_candidates`. The entire NLP pipeline will be integrated here.
    *   **Frontend:** A **React** single-page application will provide the user interface. It will allow recruiters to post job details, upload a batch of resumes, and view a clean, interactive dashboard with the ranked list of candidates.
    *   **Database:** **SQLite** will be used for simplicity to store job descriptions, candidate information, and their calculated scores.

**5. Tools / Technologies to be used:**
*   **Programming Language:** Python
*   **NLP Libraries:** **Sentence-Transformers**, **spaCy**, NLTK, Scikit-learn
*   **File Parsing:** PyMuPDF, python-docx
*   **Backend Framework:** Flask
*   **Frontend Framework:** React.js, HTML5, CSS3, Chart.js (for visualizations)
*   **Database:** SQLite or PostgreSQL (for more robust data handling)
*   **Version Control:** Git & GitHub
*   **Deployment (Optional):** Docker, Heroku/AWS Elastic Beanstalk

**6. Expected Program Outcome:**
*   A fully functional, deployment-ready prototype of an intelligent resume ranking system.
*   A system that demonstrably outperforms traditional keyword-based methods in ranking accuracy and fairness.
*   A research report or paper detailing the effectiveness of the hybrid semantic-and-skill-based ranking methodology.
*   An "explainable AI" component that provides clear, concise reasons for a candidate's ranking, building trust with the user.
*   Valuable analytics for recruiters, such as identifying the overall skill distribution in the applicant pool.

**7. Significance / Societal Relevance:**
This project directly addresses a major bottleneck in the recruitment industry. By automating and enhancing the initial screening process, it:
*   **Combats Unconscious Bias:** The system judges candidates based on skills and experience, not on demographic information, promoting fair hiring practices and workplace diversity.
*   **Increases Efficiency:** It saves countless hours for HR professionals, allowing them to focus on value-added tasks like interviewing and candidate engagement.
*   **Connects Talent with Opportunity:** It helps deserving candidates, whose resumes might be unconventionally formatted, to be discovered by recruiters, bridging the gap between talent and opportunity.
*   **Drives HR Digital Transformation:** It serves as a prime example of applying advanced AI to solve real-world business problems, aligning with Industry 4.0 principles and the modernization of human resource management.

---

**III. Time Line for the Period (Gantt Chart)**

| Activity / Phase | W1-2 | W3-4 | W5-6 | W7-8 | W9-10 | W11-12 | W13-14 | W15-16 | W17-18 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Research & Planning** | | | | | | | | | |
| Literature Survey & Title Confirmation | ████ | | | | | | | | |
| Gap Identification & Methodology Finalization | | ████ | | | | | | | |
| **2. System Design & Setup** | | | | | | | | | |
| System Architecture Design | | | ████ | | | | | | |
| Environment Setup & Tool Installation | | | | ██ | | | | | |
| **3. Core Implementation** | | | | | | | | | |
| Resume Parsing & Preprocessing Module | | | | | ████ | | | | |
| NLP Pipeline (NER, Skill Extraction) | | | | | | ████ | | | |
| Semantic Embedding & Ranking Algorithm | | | | | | | ████ | | |
| **4. Application Development** | | | | | | | | | |
| Backend API (Flask) Development | | | | | | | | ████ | |
| Frontend Dashboard (React) | | | | | | ████ | ████ | | |
| **5. Testing & Evaluation** | | | | | | | | | |
| Integration Testing & Debugging | | | | | | | | | ████ |
| Performance Evaluation & Analysis | | | | | | | | | | ████ |
| **6. Documentation & Publication** | | | | | | | | | |
| Final Report Writing & Documentation | | | | | | | | | | █████ |
| Research Paper Preparation & Submission | | | | | | | | | | | █████ |

---

**IV. Project Classification:**
**Type of the Project:** Application + Research

---

**V. Quality of the project:**

| S.No | Quality Parameter | Description |
| :--- | :--- | :--- |
| 1 | **Ethics & Fairness** | The core design aims to mitigate human bias. Strict data privacy practices will be followed for any real resume data, ensuring anonymization and consent. |
| 2 | **Innovation** | Moves beyond outdated keyword-matching to state-of-the-art semantic analysis using transformer models, which is a significant technological leap. |
| 3 | **Cost-Effectiveness** | The entire technology stack is built on powerful, open-source libraries (Python, Flask, React, spaCy, Sentence-Transformers), making it highly scalable and affordable. |
| 4 | **Application** | Has direct, high-impact applications in corporate HR departments, recruitment agencies, and university career service centers to streamline their hiring processes. |

---

**VI. Project (title)-Program Outcomes (POs) Relationship Matrix (Indicate the relationships by mark “X”)**

| Project Outcomes | PO1 | PO2 | PO3 | PO4 | PO5 | PO6 | PO7 | PO8 | PO9 | PO10 | PO11 | PO12 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :--: | :--: | :--: |
| 1. Develop problem formation and design skills for engineering and real-world problems. | X | X | X | | | | | | | | | |
| 2. Collect and Generate ideas through literature survey on current research areas | | X | | X | | | | | | | | X |
| 3. Import knowledge on software & hardware to meet industry perspective needs and standards. | X | | X | | X | | | | | | | X |
| 4. Create interest to carry out research on innovative ideas as a lifelong learning. | | | | X | | | | X | | | | X |
| 5. Ability to work with team and enrich presentation and communication skills. | | | | | | | | | X | X | X | |
| 6. Create a platform that makes students employable. | | X | X | | X | X | | X | | | | X |

**Program Educational Objectives (PEOs)-Course Outcomes Relationship Matrix (Indicate the relationships by mark “X”)**

| Project Outcomes | PSO1 | PSO2 |
| :--- | :--: | :--: |
| 1. Develop problem formation and design skills for engineering and real-world problems. | X | |
| 2. Collect and Generate ideas through literature survey on current research areas | X | X |
| 3. Import knowledge on software & hardware to meet industry perspective needs and standards. | X | X |
| 4. Create interest to carry out research on innovative ideas as a lifelong learning. | | X |
| 5. Ability to work with team and enrich presentation and communication skills. | | X |
| 6. Create a platform that makes students employable. | X | X |

---

**Signature of the Supervisor**

**DPRC Comment:**

**Signature of DPRC Member1 DPRC Member2 DPRC Member3**
*(Supervisor and DPRC members are requested to review the content and confirm your approval with signatures)*

**Signature of the HOD**

**Tadepalligudem. Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_**