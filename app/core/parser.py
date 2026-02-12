import pdfplumber
import docx
import io

def extract_text(file):
    content = file.file.read()
    file.file.seek(0)

    if file.filename.lower().endswith(".pdf"):
        text = ""
        with pdfplumber.open(io.BytesIO(content)) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    elif file.filename.lower().endswith(".docx"):
        document = docx.Document(io.BytesIO(content))
        return "\n".join(p.text for p in document.paragraphs)

    else:
        return content.decode("utf-8", errors="ignore")
