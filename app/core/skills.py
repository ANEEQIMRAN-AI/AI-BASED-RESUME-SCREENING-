import spacy
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

SKILL_LIST = [
    "python", "java", "fastapi", "flask",
    "machine learning", "deep learning",
    "react", "node.js", "docker", "kubernetes",
    "sql", "postgresql", "mongodb",
    "git", "aws", "tensorflow", "pytorch"
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
matcher.add("SKILLS", [nlp(skill) for skill in SKILL_LIST])

def extract_skills(text: str):
    doc = nlp(text)
    matches = matcher(doc)
    return sorted(
        set(doc[start:end].text.lower() for _, start, end in matches)
    )
