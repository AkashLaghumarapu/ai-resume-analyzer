def generate_recommendations(ats_score, missing_skills, resume_sections, matched_skills, resume_skills, jd_skills):
    recommendations = []

    if missing_skills:
        recommendations.append(
            f"Add the missing skills from the job description: {', '.join(missing_skills)}."
        )

    if not resume_sections.get("Projects"):
        recommendations.append(
            "Add a dedicated Projects section with measurable results to strengthen your profile."
        )

    if not resume_sections.get("Skills") and resume_skills:
        recommendations.append(
            "Create a clear Skills section to improve ATS parseability and recruiter scanning."
        )

    if ats_score < 80:
        recommendations.append(
            "Use quantifiable achievements and action verbs to improve your ATS score and recruiter impact."
        )

    if 80 <= ats_score < 90:
        recommendations.append(
            "Your resume is strong; focus on tailoring experience and keywords for the target job."
        )
    elif ats_score >= 90:
        recommendations.append(
            "Excellent fit — keep refining the resume for clarity and recruiter-friendly formatting."
        )

    if not resume_skills:
        recommendations.append(
            "List your technical and soft skills clearly so the ATS and hiring managers can detect them."
        )

    if not matched_skills and jd_skills:
        recommendations.append(
            "Try matching your resume language to the job description and include relevant terminology."
        )

    if not recommendations:
        recommendations.append(
            "Resume analysis looks healthy. Keep tailoring your resume for each role and continue building new achievements."
        )

    return recommendations
