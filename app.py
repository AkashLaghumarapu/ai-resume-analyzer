import streamlit as st
import pandas as pd
import os
from datetime import datetime

from modules.resume_parser import extract_text_from_pdf
from modules.skill_extractor import extract_skills
from modules.matcher import (
    calculate_similarity,
    calculate_skill_match
)
from modules.resume_sections import extract_resume_sections
from modules.keyword_analyzer import keyword_frequency
from modules.recommendation_engine import generate_recommendations
from modules.report_generator import generate_pdf_report


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# ---------------- MAIN TITLE ----------------

st.title("AI Resume Analyzer")

st.markdown(
    """
    Upload a resume and compare it against a job description
    using NLP and Machine Learning.
    """
)

st.write("---")


# ---------------- SIDEBAR ----------------

st.sidebar.title("Dashboard")

st.sidebar.info(
    """
    AI-powered ATS Resume Analysis System
    """
)


# ---------------- INPUT SECTION ----------------

col1, col2 = st.columns([3, 2])

with col1:

    resume_file = st.file_uploader(
        "Upload Resume PDF",
        type=["pdf"]
    )

    job_description = st.text_area(
        "Paste Job Description",
        height=250
    )

    save_history = st.checkbox(
        "Save Analysis History",
        value=True
    )

with col2:

    st.subheader("Features")

    st.write("✅ Resume ATS Score")
    st.write("✅ Skill Extraction")
    st.write("✅ Missing Skill Detection")
    st.write("✅ Resume Recommendations")
    st.write("✅ PDF Report Download")


# ---------------- MAIN ANALYSIS ----------------

if resume_file is not None and job_description.strip():

    with st.spinner("Analyzing Resume..."):

        # ---------- EXTRACT TEXT ----------

        resume_text = extract_text_from_pdf(
            resume_file
        )

        if not resume_text or len(resume_text.strip()) < 50:

            st.error(
                "Resume text could not be extracted properly."
            )

            st.stop()

        # ---------- NLP ANALYSIS ----------

        resume_sections = extract_resume_sections(
            resume_text
        )

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            job_description
        )

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        matched_skills, missing_skills, skill_match_score = calculate_skill_match(
            resume_skills,
            jd_skills
        )

        # ---------- ATS SCORE ----------

        section_score = 0

        if resume_sections.get("skills"):
            section_score += 10

        if resume_sections.get("projects"):
            section_score += 10

        if resume_sections.get("education"):
            section_score += 10

        if resume_sections.get("experience"):
            section_score += 10

        # ---------- SKILL MATCH PERCENT ----------

        skill_percentage = 0

        if len(jd_skills) > 0:

            skill_percentage = (
                len(matched_skills)
                / len(jd_skills)
            )

        # ---------- FINAL ATS ----------

        ats_score = int(

            (
                similarity_score * 40
            )
            +
            (
                skill_percentage * 50
            )
            +
            section_score

        )

        # ---------- PENALTY ----------

        if len(missing_skills) >= 10:
            ats_score -= 10

        # ---------- LIMIT ----------

        if ats_score > 100:
            ats_score = 100

        if ats_score < 0:
            ats_score = 0

        # ---------- GRADE ----------

        if ats_score >= 90:

            grade = "A+"

        elif ats_score >= 80:

            grade = "A"

        elif ats_score >= 70:

            grade = "B"

        elif ats_score >= 60:

            grade = "C"

        else:

            grade = "D"

        # ---------- RECOMMENDATIONS ----------

        recommendations = generate_recommendations(

            ats_score=ats_score,

            missing_skills=missing_skills,

            resume_sections=resume_sections,

            matched_skills=matched_skills,

            resume_skills=resume_skills,

            jd_skills=jd_skills

        )

        # ---------- KEYWORDS ----------

        keyword_df = keyword_frequency(
            resume_text
        )

        # ---------- RESULTS ----------

        st.success(
            "Resume analysis completed successfully!"
        )

        st.subheader("Resume Analysis")

        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(
                "ATS Score",
                f"{ats_score}/100"
            )

        with c2:

            st.metric(
                "Similarity Score",
                f"{int(similarity_score * 100)}%"
            )

        with c3:

            st.metric(
                "Skill Match",
                f"{int(skill_match_score * 100)}%"
            )

        # ---------- GRADE ----------

        st.success(
            f"Resume Grade: {grade}"
        )

        # ---------- STRENGTH ----------

        if ats_score >= 85:

            st.success(
                "Excellent ATS Resume"
            )

        elif ats_score >= 70:

            st.info(
                "Good Resume"
            )

        elif ats_score >= 50:

            st.warning(
                "Average Resume"
            )

        else:

            st.error(
                "Resume Needs Improvement"
            )

        # ---------- PROGRESS ----------

        st.subheader("ATS Insights")

        p1, p2, p3 = st.columns(3)

        with p1:

            st.progress(
                min(similarity_score, 1.0)
            )

            st.caption(
                "Job Description Similarity"
            )

        with p2:

            st.progress(
                min(skill_match_score, 1.0)
            )

            st.caption(
                "Skill Coverage"
            )

        with p3:

            st.progress(
                min(ats_score / 100, 1.0)
            )

            st.caption(
                "Overall ATS Fit"
            )

        # ---------- SKILLS ----------

        st.subheader("Skills Analysis")

        st.write(
            "**Resume Skills:**",
            ", ".join(sorted(resume_skills))
            if resume_skills
            else "No skills detected"
        )

        st.write(
            "**Job Description Skills:**",
            ", ".join(sorted(jd_skills))
            if jd_skills
            else "No skills detected"
        )

        # ---------- MATCHED ----------

        st.subheader("Matched Skills")

        if matched_skills:

            st.success(
                ", ".join(sorted(matched_skills))
            )

        else:

            st.warning(
                "No matching skills found."
            )

        # ---------- MISSING ----------

        st.subheader("Missing Skills")

        if missing_skills:

            st.error(
                ", ".join(sorted(missing_skills))
            )

        else:

            st.success(
                "No major skills missing."
            )

        # ---------- RECOMMENDATIONS ----------

        with st.expander(
            "AI Recommendations"
        ):

            for rec in recommendations:

                st.write(f"• {rec}")

        # ---------- PDF REPORT ----------

        report_bytes = generate_pdf_report(

            candidate_name="Candidate",

            resume_name=resume_file.name,

            ats_score=ats_score,

            similarity_score=similarity_score,

            skill_match_score=skill_match_score,

            matched_skills=matched_skills,

            missing_skills=missing_skills,

            recommendations=recommendations,

            sections=resume_sections,

            resume_skills=resume_skills,

            jd_skills=jd_skills

        )

        st.download_button(

            label="Download PDF Report",

            data=report_bytes,

            file_name="resume_analysis_report.pdf",

            mime="application/pdf"

        )

        # ---------- SAVE HISTORY ----------

        if save_history:

            os.makedirs(
                "data",
                exist_ok=True
            )

            history_path = os.path.join(
                "data",
                "history.csv"
            )

            record = {

                "timestamp": datetime.now().isoformat(
                    timespec="seconds"
                ),

                "user": "guest",

                "resume_name": resume_file.name,

                "ats_score": ats_score,

                "similarity_score": similarity_score,

                "skill_match_score": skill_match_score

            }

            if os.path.exists(history_path):

                history_df = pd.read_csv(
                    history_path
                )

                history_df = pd.concat(

                    [
                        history_df,
                        pd.DataFrame([record])
                    ],

                    ignore_index=True

                )

            else:

                history_df = pd.DataFrame(
                    [record]
                )

            history_df.to_csv(
                history_path,
                index=False
            )

        # ---------- HISTORY ----------

        if os.path.exists(
            os.path.join(
                "data",
                "history.csv"
            )
        ):

            st.write("---")

            st.subheader(
                "Recent Analysis History"
            )

            history_data = pd.read_csv(
                os.path.join(
                    "data",
                    "history.csv"
                )
            )

            st.dataframe(
                history_data.tail(10)
            )

elif resume_file is not None and not job_description.strip():

    st.warning(
        "Please paste the job description."
    )


# ---------- FOOTER ----------

st.write("---")

st.caption(
    "Built with Python, NLP, Streamlit, and Machine Learning"
)