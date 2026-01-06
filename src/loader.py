from pypdf import PdfReader
import pandas as pd

def load_document(path):
    if path.endswith(".pdf"):
        reader = PdfReader(path)
        return "\n".join(page.extract_text() for page in reader.pages)
    elif path.endswith(".txt"):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    elif path.endswith(".csv"):
        df = pd.read_csv(path)
        return df.to_string()
    else:
        raise ValueError("Unsupported file type")
