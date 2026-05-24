import streamlit as st

st.set_page_config(page_title="How It Works", page_icon="⚙️", layout="wide")

st.title("How AI Resume Analyzer Works")

st.markdown("### 1. Upload and extract")
st.write("Users upload a PDF resume. The app extracts text from the PDF and prepares it for analysis.")

st.markdown("### 2. Skill extraction")
st.write("The resume and job description are scanned for technical and soft skills using NLP token matching.")

st.markdown("### 3. Resume matching")
st.write("TF-IDF vectorization and cosine similarity measure how closely the resume aligns with the job description.")

st.markdown("### 4. ATS scoring")
st.write("A combined score uses both similarity and skill coverage to simulate ATS readiness.")

st.markdown("### 5. Recommendations")
st.write("The app generates actionable recommendations and highlights missing skills for stronger resume targeting.")

st.markdown("### 6. Reporting")
st.write("A downloadable PDF report summarizes resume strengths, weak spots, and optimization opportunities.")
