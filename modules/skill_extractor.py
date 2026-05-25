import re


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
    "computer vision",

    # ---------- EXTRA SKILLS ----------

    "spring boot",
    "fastapi",
    "keras",
    "excel",
    "typescript",
    "bootstrap",
    "tailwind",
    "redis",
    "firebase",
    "azure",
    "kubernetes",
    "jira",
    "agile",
    "selenium",
    "cybersecurity",
    "penetration testing",
    "network security"

]


# ---------- EXTRA COMMON VARIATIONS ----------

VARIATIONS = {

    "ml": "Machine Learning",

    "ai": "Artificial Intelligence",

    "js": "JavaScript",

    "reactjs": "React",

    "node": "Nodejs",

    "tf": "Tensorflow"

}


# ---------- EXTRACT SKILLS ----------

def extract_skills(text):

    if not text:

        return []

    text_lower = text.lower()

    found_skills = set()

    # ---------- DIRECT SKILL MATCH ----------

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):

            found_skills.add(
                skill.title()
            )

    # ---------- VARIATION MATCH ----------

    words = text_lower.split()

    for word in words:

        clean_word = word.strip(
            ".,!?():;/"
        )

        if clean_word in VARIATIONS:

            found_skills.add(
                VARIATIONS[clean_word]
            )

    return sorted(
        list(found_skills)
    )