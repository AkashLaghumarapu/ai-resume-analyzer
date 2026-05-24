import pdfplumber
import re
from io import BytesIO

INVALID_RESUME_MESSAGE = "Unable to extract text from the uploaded PDF."

def extract_text_from_pdf(uploaded_file):
    try:
        if hasattr(uploaded_file, "read"):
            data = uploaded_file.read()
            pdf = pdfplumber.open(BytesIO(data))
        else:
            pdf = pdfplumber.open(uploaded_file)

        text = []
        for page in pdf.pages:
            page_text = page.extract_text() or ""
            clean_text = page_text.replace("\xa0", " ")
            text.append(clean_text)
        pdf.close()
        return "\n".join(text).strip()
    except Exception:
        return ""


def sanitize_text(text):
    sanitized = re.sub(r"\s+", " ", text).strip()
    return sanitized
