def compute_final_score(resume_skills, jd_skills, similarity):
    if not jd_skills:
        return 0, "Not Recommended"

    skill_score = (
        len(set(resume_skills) & set(jd_skills)) / len(jd_skills)
    ) * 100

    final_score = round(
        (0.6 * skill_score) + (0.4 * similarity),
        2
    )

    if final_score >= 80:
        recommendation = "Strongly Recommended"
    elif final_score >= 60:
        recommendation = "Recommended"
    elif final_score >= 40:
        recommendation = "Consider with Review"
    else:
        recommendation = "Not Recommended"

    return final_score, recommendation
