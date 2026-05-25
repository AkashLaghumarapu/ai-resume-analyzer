from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------- SIMILARITY ----------

def calculate_similarity(

    resume_text,
    job_description

):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    vectors = vectorizer.fit_transform(

        [
            resume_text,
            job_description
        ]

    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(
        float(similarity),
        2
    )


# ---------- SKILL MATCH ----------

def calculate_skill_match(

    resume_skills,
    jd_skills

):

    resume_set = set(

        skill.lower()
        for skill in resume_skills

    )

    jd_set = set(

        skill.lower()
        for skill in jd_skills

    )

    matched = sorted(

        list(
            resume_set & jd_set
        )

    )

    missing = sorted(

        list(
            jd_set - resume_set
        )

    )

    if len(jd_set) == 0:

        score = 0

    else:

        score = len(
            matched
        ) / len(jd_set)

    return (

        [skill.title() for skill in matched],

        [skill.title() for skill in missing],

        round(score, 2)

    )