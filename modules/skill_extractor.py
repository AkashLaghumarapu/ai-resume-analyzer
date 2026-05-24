import spacy


# ---------- SKILLS DATABASE ----------

SKILLS = [

    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "django",
    "flask",
    "streamlit",
    "machine learning",
    "deep learning",
    "nlp",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "scikit-learn",
    "data analysis",
    "data science",
    "power bi",
    "tableau",
    "git",
    "github",
    "linux",
    "docker",
    "aws",
    "api",
    "rest api",
    "opencv",
    "computer vision"

]


# ---------- LOAD NLP MODEL ----------

def load_nlp_model():

    try:

        return spacy.load(
            "en_core_web_sm"
        )

    except OSError:

        spacy.cli.download(
            "en_core_web_sm"
        )

        return spacy.load(
            "en_core_web_sm"
        )


# ---------- EXTRACT SKILLS ----------

def extract_skills(text):

    nlp = load_nlp_model()

    text_lower = text.lower()

    doc = nlp(text_lower)

    found_skills = set()

    # ---------- PHRASE MATCHING ----------

    for skill in SKILLS:

        if skill.lower() in text_lower:

            found_skills.add(
                skill.title()
            )

    # ---------- TOKEN MATCHING ----------

    for token in doc:

        token_text = token.text.strip()

        for skill in SKILLS:

            if token_text == skill.lower():

                found_skills.add(
                    skill.title()
                )

    return sorted(
        list(found_skills)
    )