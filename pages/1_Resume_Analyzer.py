import streamlit as st
from modules.auth import load_authenticator
from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.matcher import calculate_similarity, calculate_skill_match
from modules.resume_sections import extract_resume_sections
from modules.keyword_analyzer import keyword_frequency
from modules.recommendation_engine import generate_recommendations
from modules.report_generator import generate_pdf_report
import pandas as pd
import os
from datetime import datetime

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="wide")

AUTH = load_authenticator()
name, authentication_status, username = AUTH.login("Login", "main")

if authentication_status:
    st.title("Resume Analyzer")
    st.write("Analyze your resume against a job description, identify missing skills, and generate a custom report.")
    st.divider()

    left, right = st.columns([2, 1])
    with left:
        resume_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
        job_description = st.text_area("Job description or role summary", height=250)
        save_history = st.checkbox("Save this analysis for future review", value=True)

    with right:
        st.markdown("## How it works")
        st.markdown("- Upload a PDF resume and paste the target job description.")
        st.markdown("- Resume text is extracted and scored with NLP and ATS logic.")
        st.markdown("- Export a downloadable PDF report with insights and recommendations.")

    if resume_file and job_description.strip():
        text = extract_text_from_pdf(resume_file)
        if not text:
            st.error("Could not extract resume content from the PDF. Please upload a valid file.")
        else:
            sections = extract_resume_sections(text)
            resume_skills = extract_skills(text)
            jd_skills = extract_skills(job_description)
            similarity_score = calculate_similarity(text, job_description)
            matched_skills, missing_skills, skill_match_score = calculate_skill_match(resume_skills, jd_skills)
            ats_score = int((similarity_score * 0.6 + skill_match_score * 0.4) * 100)
            grade = "A+" if ats_score >= 90 else "A" if ats_score >= 80 else "B" if ats_score >= 70 else "C" if ats_score >= 60 else "D"
            recommendations = generate_recommendations(
                ats_score=ats_score,
                missing_skills=missing_skills,
                resume_sections=sections,
                matched_skills=matched_skills,
                resume_skills=resume_skills,
                jd_skills=jd_skills,
            )
            keyword_df = keyword_frequency(text)

            st.metric(label="ATS Score", value=f"{ats_score}/100", delta=f"Grade {grade}")
            st.metric(label="Similarity", value=f"{int(similarity_score * 100)}%")
            st.metric(label="Skill Match", value=f"{int(skill_match_score * 100)}%")
            st.divider()

            st.subheader("Skills Overview")
            st.write("**Detected resume skills:**", ", ".join(resume_skills) if resume_skills else "No skills detected.")
            st.write("**Role keywords:**", ", ".join(jd_skills) if jd_skills else "No job skills extracted.")

            if matched_skills:
                st.success("Matched skills: {}".format(", ".join(matched_skills)))
            if missing_skills:
                st.error("Missing skills: {}".format(", ".join(missing_skills)))

            with st.expander("Top keyword frequency"):
                st.table(keyword_df)

            with st.expander("Resume section preview"):
                for section, content in sections.items():
                    st.markdown(f"#### {section}")
                    st.write(content)

            with st.expander("Recommendations"):
                for rec in recommendations:
                    st.write(f"- {rec}")

            report_bytes = generate_pdf_report(
                candidate_name=username or "Candidate",
                resume_name=resume_file.name,
                ats_score=ats_score,
                similarity_score=similarity_score,
                skill_match_score=skill_match_score,
                matched_skills=matched_skills,
                missing_skills=missing_skills,
                recommendations=recommendations,
                sections=sections,
                resume_skills=resume_skills,
                jd_skills=jd_skills,
            )

            st.download_button(
                label="Download PDF Report",
                data=report_bytes,
                file_name="resume_analysis_report.pdf",
                mime="application/pdf",
            )

            if save_history:
                history_path = os.path.join("data", "history.csv")
                row = {
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "user": username,
                    "resume_name": resume_file.name,
                    "ats_score": ats_score,
                    "similarity_score": round(similarity_score, 3),
                    "skill_match_score": round(skill_match_score, 3),
                    "matched_skills": ";".join(matched_skills),
                    "missing_skills": ";".join(missing_skills),
                }
                history_df = pd.read_csv(history_path) if os.path.exists(history_path) else pd.DataFrame()
                history_df = pd.concat([history_df, pd.DataFrame([row])], ignore_index=True)
                history_df.to_csv(history_path, index=False)

            if os.path.exists(os.path.join("data", "history.csv")):
                st.divider()
                st.subheader("Analysis history")
                history = pd.read_csv(os.path.join("data", "history.csv"))
                st.dataframe(history.tail(10))
    elif resume_file and not job_description.strip():
        st.warning("Please provide a job description for meaningful analysis.")
    else:
        st.info("Upload a resume PDF and paste a job description to begin.")

    AUTH.logout("Logout", "sidebar")
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your credentials to continue.")
