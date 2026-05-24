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


# ---------- EXTRACT SKILLS ----------

def extract_skills(text):

    if text is None:

        return []

    text_lower = text.lower()

    found_skills = set()

    # ---------- DIRECT SKILL MATCH ----------

    for skill in SKILLS:

        if skill.lower() in text_lower:

            found_skills.add(
                skill.title()
            )

    # ---------- EXTRA COMMON VARIATIONS ----------

    variations = {

        "ml": "Machine Learning",

        "ai": "Artificial Intelligence",

        "js": "JavaScript",

        "node": "Nodejs",

        "reactjs": "React",

        "tf": "Tensorflow"

    }

    words = text_lower.split()

    for word in words:

        if word in variations:

            found_skills.add(
                variations[word]
            )

    return sorted(
        list(found_skills)
    )