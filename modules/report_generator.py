from fpdf import FPDF
import unicodedata
import textwrap


# ---------- CLEAN TEXT ----------

def clean_text(text):

    if text is None:
        return ""

    text = str(text)

    text = unicodedata.normalize(
        "NFKD",
        text
    )

    text = (
        text
        .replace("–", "-")
        .replace("—", "-")
        .replace("’", "'")
        .replace("‘", "'")
        .replace("“", '"')
        .replace("”", '"')
    )

    text = text.encode(
        "latin-1",
        "ignore"
    ).decode(
        "latin-1"
    )

    return text


# ---------- SAFE TEXT ----------

def safe_text(text, width=70, max_length=400):

    text = clean_text(text)

    text = text.replace("\n", " ")

    words = text.split()

    cleaned_words = []

    for word in words:

        if len(word) > 25:

            word = word[:25]

        cleaned_words.append(word)

    final_text = " ".join(cleaned_words)

    final_text = final_text[:max_length]

    wrapped = "\n".join(

        textwrap.wrap(
            final_text,
            width=width
        )

    )

    return wrapped


# ---------- PDF REPORT ----------

def generate_pdf_report(

    candidate_name,
    resume_name,
    ats_score,
    similarity_score,
    skill_match_score,
    matched_skills,
    missing_skills,
    recommendations,
    sections,
    resume_skills,
    jd_skills

):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_auto_page_break(
        auto=True,
        margin=15
    )

    # ---------- TITLE ----------

    pdf.set_font(
        "Helvetica",
        "B",
        18
    )

    pdf.cell(
        180,
        12,
        "AI Resume Analyzer Report",
        ln=True,
        align="C"
    )

    pdf.ln(5)

    # ---------- BASIC INFO ----------

    pdf.set_font(
        "Helvetica",
        "",
        12
    )

    basic_info = [

        f"Candidate: {candidate_name}",

        f"Resume File: {resume_name}",

        f"ATS Score: {ats_score}/100",

        f"Similarity Score: {int(similarity_score * 100)}%",

        f"Skill Match Score: {int(skill_match_score * 100)}%"

    ]

    for item in basic_info:

        pdf.multi_cell(
            180,
            8,
            safe_text(item)
        )

    pdf.ln(4)

    # ---------- SECTION FUNCTION ----------

    def add_section(title, content):

        pdf.set_font(
            "Helvetica",
            "B",
            14
        )

        pdf.multi_cell(
            180,
            8,
            safe_text(title)
        )

        pdf.set_font(
            "Helvetica",
            "",
            11
        )

        pdf.multi_cell(
            180,
            6,
            safe_text(content)
        )

        pdf.ln(3)

    # ---------- SKILLS ----------

    add_section(

        "Resume Skills",

        ", ".join(resume_skills)
        if resume_skills
        else "No skills detected"

    )

    add_section(

        "Matched Skills",

        ", ".join(matched_skills)
        if matched_skills
        else "No matched skills"

    )

    add_section(

        "Missing Skills",

        ", ".join(missing_skills)
        if missing_skills
        else "No missing skills"

    )

    # ---------- RECOMMENDATIONS ----------

    recommendations_text = ""

    if recommendations:

        for rec in recommendations:

            recommendations_text += f"- {rec}\n"

    else:

        recommendations_text = "No recommendations available."

    add_section(

        "Recommendations",

        recommendations_text

    )

    # ---------- RESUME SECTIONS ----------

    if sections:

        for section, content in sections.items():

            add_section(

                section.title(),

                content[:250]

            )

    # ---------- JOB DESCRIPTION SKILLS ----------

    add_section(

        "Job Description Skills",

        ", ".join(jd_skills)
        if jd_skills
        else "No JD skills detected"

    )

    # ---------- OUTPUT ----------

    pdf_output = pdf.output(
        dest="S"
    )

    return bytes(pdf_output)