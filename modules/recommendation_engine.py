def generate_recommendations(

    ats_score,
    missing_skills,
    resume_sections,
    matched_skills,
    resume_skills,
    jd_skills

):

    recommendations = []

    # ---------- SCORE ----------

    if ats_score < 50:

        recommendations.append(
            "Resume is poorly aligned with the job description."
        )

    elif ats_score < 70:

        recommendations.append(
            "Resume partially matches the job description."
        )

    else:

        recommendations.append(
            "Resume is well aligned with the job description."
        )

    # ---------- MISSING SKILLS ----------

    if missing_skills:

        recommendations.append(

            "Add missing skills: "
            +
            ", ".join(missing_skills[:5])

        )

    # ---------- SECTIONS ----------

    required_sections = [

        "skills",
        "projects",
        "education",
        "experience"

    ]

    for section in required_sections:

        if not resume_sections.get(section):

            recommendations.append(

                f"Add {section} section to improve ATS score."

            )

    # ---------- MATCH QUALITY ----------

    if len(matched_skills) >= 5:

        recommendations.append(
            "Strong skill match with job description."
        )

    elif len(matched_skills) >= 2:

        recommendations.append(
            "Moderate skill match detected."
        )

    else:

        recommendations.append(
            "Very few relevant skills detected."
        )

    return recommendations