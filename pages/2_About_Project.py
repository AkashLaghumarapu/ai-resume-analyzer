import streamlit as st

st.set_page_config(page_title="About Project", page_icon="📚", layout="wide")

st.title("About AI Resume Analyzer")
st.write("AI Resume Analyzer is a portfolio-ready application designed for job seekers and recruiters looking to assess resume fit quickly.")

st.markdown("### Core capabilities")
st.markdown("- Intelligent resume parsing from PDF files.")
st.markdown("- Job description matching powered by TF-IDF and cosine similarity.")
st.markdown("- ATS scoring and missing skill detection.")
st.markdown("- Custom recommendation generation and PDF report export.")

st.markdown("### Built with")
st.markdown("- Python")
st.markdown("- Streamlit")
st.markdown("- spaCy for NLP")
st.markdown("- scikit-learn for resume matching")
st.markdown("- pdfplumber for PDF extraction")
st.markdown("- pandas for data workflows")
st.markdown("- fpdf for report generation")

st.markdown("### Why this project is portfolio-ready")
st.write(
    "This app combines clean UX, modular Python architecture, and real-world resume analytics to showcase data and product design skills. "
    "It is ideal for recruiters and internship hiring because it demonstrates both technical and user-focused development." 
)
