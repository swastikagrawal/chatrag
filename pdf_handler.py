import os
from pypdf import PdfReader
from config import PDF_FOLDER, CHUNK_SIZE, CHUNK_OVERLAP


def get_pdf_list():
    pdf_files = []
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            path = os.path.join(PDF_FOLDER, file)
            try:
                reader = PdfReader(path)
                if reader.is_encrypted:
                    continue
                pdf_files.append(file)
            except:
                continue
    return pdf_files


def extract_text(pdf_file):
    path = os.path.join(PDF_FOLDER, pdf_file)
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted
    return text


def chunk_text(text):
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = words[i:i + CHUNK_SIZE]
        chunks.append(" ".join(chunk))
        i += CHUNK_SIZE - CHUNK_OVERLAP
    return chunks


def load_pdf(pdf_file):
    text = extract_text(pdf_file)
    chunks = chunk_text(text)
    return chunks


def load_all_pdfs(pdf_files):
    all_chunks = []
    all_sources = []
    for file in pdf_files:
        text = extract_text(file)
        chunks = chunk_text(text)
        for chunk in chunks:
            all_chunks.append(chunk)
            all_sources.append(file)
    return all_chunks, all_sources