# AI Resume Analyzer

A professional, portfolio-ready resume analysis web app built with Python, Streamlit, NLP, and machine learning.

## Overview
AI Resume Analyzer helps job seekers compare resumes to job descriptions, calculate ATS scores, highlight missing skills, and generate recruiter-ready recommendations.

## Features
- Upload PDF resumes and extract text automatically
- Compare resumes against job descriptions using TF-IDF and cosine similarity
- Generate ATS scores and grading feedback
- Detect missing technical and soft skills
- Recommend resume improvements
- Extract resume sections such as Education, Experience, Projects, and Skills
- Keyword density and top keyword analytics
- Download polished PDF analysis reports
- Save analysis history in CSV
- Authentication with Streamlit Authenticator
- Multi-page Streamlit application with modern dark UI

## Tech Stack
- Python
- Streamlit
- scikit-learn
- spaCy
- pdfplumber
- matplotlib
- pandas
- fpdf
- streamlit-authenticator

## Project Structure
```
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .streamlit/
│   └── config.toml
├── modules/
│   ├── auth.py
│   ├── matcher.py
│   ├── keyword_analyzer.py
│   ├── recommendation_engine.py
│   ├── report_generator.py
│   ├── resume_parser.py
│   ├── resume_sections.py
│   └── skill_extractor.py
├── pages/
│   ├── 1_Resume_Analyzer.py
│   ├── 2_About_Project.py
│   └── 3_How_It_Works.py
├── data/
│   └── history.csv
├── screenshots/
├── sample_resumes/
└── assets/
```

## Installation
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the spaCy English model:
   ```bash
   python -m spacy download en_core_web_sm
   ```

## Run the App
```bash
streamlit run app.py
```

## Login Credentials
- Username: `candidate`
- Password: `password123`

## Deployment
This app is compatible with Streamlit Cloud and other Python web app hosts. Ensure `requirements.txt` is included and the spaCy model is installed on the host.

## Future Improvements
- Add resume version comparison
- Expand sample resume library
- Improve skill extraction with custom named entity recognition
- Add advanced dashboard analytics and charts
- Support DOCX resume uploads
