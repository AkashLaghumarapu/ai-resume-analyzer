from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
    return float(similarity)


def calculate_skill_match(resume_skills, jd_skills):
    resume_set = set([skill.lower() for skill in resume_skills])
    jd_set = set([skill.lower() for skill in jd_skills])
    matched = sorted([skill.title() for skill in resume_set.intersection(jd_set)])
    missing = sorted([skill.title() for skill in jd_set.difference(resume_set)])
    score = 0.0
    if jd_set:
        score = len(matched) / len(jd_set)
    elif resume_set:
        score = 0.5
    return matched, missing, float(score)
