from fastapi import FastAPI, File, UploadFile
from PyPDF2 import PdfReader
import spacy
import os

app = FastAPI()

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...)):
    # Save uploaded file temporarily
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as f:
        f.write(await file.read())

    # Extract text from PDF
    extracted_text = extract_text_from_pdf(temp_file_path)

    # Run NLP Analysis
    analysis = run_nlp_analysis(extracted_text)

    # Clean up the temporary file
    os.remove(temp_file_path)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text,
        "analysis": analysis
    }

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def run_nlp_analysis(text):
    """Perform NLP analysis on the text."""
    doc = nlp(text)

    # Named Entity Recognition (NER)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Extract Keywords (Noun Chunks)
    keywords = list(set(chunk.text for chunk in doc.noun_chunks))

    # Summarize Sections
    summary = generate_summary(text)

    return {
        "entities": entities,
        "keywords": keywords,
        "summary": summary
    }

def generate_summary(text):
    """Generate a simple summary based on sections."""
    lines = text.split("\n")
    summary = {}

    for line in lines:
        line = line.strip()
        if line.startswith("1."):
            summary["Purpose"] = line
        elif line.startswith("2."):
            summary["Obligations"] = line
        elif line.startswith("3."):
            summary["Confidentiality"] = line
        elif line.startswith("4."):
            summary["Term and Termination"] = line
        elif line.startswith("5."):
            summary["Governing Law"] = line

    return summary
