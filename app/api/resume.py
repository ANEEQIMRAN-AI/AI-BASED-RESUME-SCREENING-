from fastapi import APIRouter, UploadFile, Form
from typing import List

from app.core.parser import extract_text
from app.core.skills import extract_skills
from app.core.similarity import semantic_similarity
from app.core.scoring import compute_final_score

router = APIRouter()

@router.post("/analyze-multiple")
async def analyze_multiple_resumes(
    resumes: List[UploadFile],
    job_description: str = Form(...)
):
    jd_skills = extract_skills(job_description)
    results = []

    for resume in resumes:
        resume_text = extract_text(resume)
        resume_skills = extract_skills(resume_text)

        similarity = semantic_similarity(resume_text, job_description)
        final_score, recommendation = compute_final_score(
            resume_skills, jd_skills, similarity
        )

        results.append({
            "candidate_name": resume.filename,
            "resume_skills": resume_skills,
            "matched_skills": list(set(resume_skills) & set(jd_skills)),
            "missing_skills": list(set(jd_skills) - set(resume_skills)),
            "semantic_similarity": similarity,
            "final_match_percentage": final_score,
            "recommendation": recommendation
        })

    ranked_results = sorted(
        results,
        key=lambda x: x["final_match_percentage"],
        reverse=True
    )

    return {
        "total_candidates": len(resumes),
        "job_description_skills": jd_skills,
        "ranked_candidates": ranked_results
    }
