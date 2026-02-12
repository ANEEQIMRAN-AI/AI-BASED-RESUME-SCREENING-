# AI-Based Resume Screening System


An intelligent system to **automatically analyze resumes** and match them with job descriptions. The system extracts skills, education, and experience from resumes, calculates a match percentage, and provides a recommendation. Multiple resumes can be analyzed and ranked.

---

## 🚀 Features

- Upload resumes in **PDF, DOCX, or TXT** format.
- Paste or input **Job Description (JD)**.
- Extract **skills, education, and experience** from resumes.
- Compare resumes with JD:
  - **Skills Match**
  - **Experience Match**
  - **Education Match**
  - **Semantic similarity**
- Compute **weighted score** and **recommendation**:
  - Strongly Recommended
  - Recommended
  - Consider with Review
  - Not Recommended
- **Multiple resume analysis** and ranking.
- **React frontend** with clean UI.

---

## 🗂️ Folder Structure

```
AI-Resume-Screening/
│
├─ backend/
│   ├─ app/
│   │   ├─ main.py                # Entry point of FastAPI app
│   │   ├─ api/
│   │   │   └─ resume.py          # Resume endpoints
│   │   ├─ core/
│   │   │   ├─ parser.py          # Text extraction & entity parsing
│   │   │   ├─ skills.py          # NLP skill extraction
│   │   │   └─ utils.py           # Helper functions
│   │   └─ models/                # Optional Pydantic models
│   ├─ requirements.txt           # Python dependencies
│   └─ venv/                      # Virtual environment
│
├─ frontend/
│   ├─ src/
│   │   ├─ App.js                  # React main component
│   │   ├─ App.css                 # Styles
│   │   ├─ api.js                  # API calls to backend
│   │   └─ assets/                 # Logo and images
│   └─ package.json
│
└─ README.md
```

---

## 🛠️ Technologies Used

- **Backend**:
  - FastAPI (API server)
  - Uvicorn (ASGI server)
  - PyPDF2 (PDF parsing)
  - python-docx (DOCX parsing)
  - SpaCy (NLP for skill extraction)
  - Python Regex (`re`) for parsing patterns
- **Frontend**:
  - React.js
  - HTML, CSS, JavaScript
- **Other Tools**:
  - VS Code / PyCharm (development)
  - Git & GitHub (version control)

---

## ⚙️ Installation & Setup

### Backend

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-resume-screening.git
cd ai-resume-screening/backend
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows:
```bash
venv\Scripts\activate
```
- macOS/Linux:
```bash
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Download SpaCy English model:

```bash
python -m spacy download en_core_web_sm
```

6. Start the backend server:

```bash
uvicorn app.main:app --reload
```

The backend runs at: `http://127.0.0.1:8000`

---

### Frontend

1. Navigate to the frontend folder:

```bash
cd ../frontend
```

2. Install npm dependencies:

```bash
npm install
```

3. Start the React app:

```bash
npm start
```

The frontend runs at: `http://localhost:3000`

---

## 📄 API Endpoints

### 1. Analyze Multiple Resumes

**POST** `/api/analyze-multiple`

**Form Data:**

- `resumes` – Multiple resume files (PDF, DOCX, TXT)
- `job_description` – Job Description text

**Response Example:**

```json
[
  {
    "candidate_name": "John Doe",
    "matched_skills": ["Python", "FastAPI"],
    "missing_skills": ["Docker"],
    "semantic_similarity": 78.5,
    "recommendation": "Strongly Recommended"
  },
  {
    "candidate_name": "Jane Smith",
    "matched_skills": ["Java", "SQL"],
    "missing_skills": ["AWS", "Docker"],
    "semantic_similarity": 65.3,
    "recommendation": "Recommended"
  }
]
```

---

## 🧠 How It Works

1. **Resume Upload** → Backend extracts text using PyPDF2 / python-docx.
2. **Text Parsing** → Extract skills, education, experience.
3. **Job Description Parsing** → Extract required skills.
4. **Comparison**:
   - Skills matched vs JD
   - Education match
   - Experience calculation
5. **Weighted Scoring**:
   - Skills: 50%
   - Experience: 30%
   - Education: 20%
6. **Semantic Similarity** → Measures how close the resume text is to JD text.
7. **Final Match & Recommendation** → Combined score → Returns JSON.
8. **Ranking** → Multiple resumes sorted by `final_match_percentage`.

---

## 🏆 Future Improvements

- Use **BERT or OpenAI embeddings** for advanced semantic similarity.
- Store resumes and results in **database**.
- Add **user authentication** and **admin dashboard**.
- Enable **resume history tracking** for multiple job postings.

---

## 👨‍💻 Author

**Aneeq Imran**  
- GitHub: https://github.com/ANEEQIMRAN-AI

- LinkedIn: https://linkedin.com/in/aneeq-imran-977077340

---

```

