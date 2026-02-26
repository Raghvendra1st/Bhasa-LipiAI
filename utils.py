import os
from PyPDF2 import PdfReader
import docx
from deep_translator import GoogleTranslator

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    elif ext == '.pdf':
        reader = PdfReader(file_path)
        text = ''
        for page in reader.pages:
            text += page.extract_text() + '\n'
        return text
    elif ext == '.docx':
        doc = docx.Document(file_path)
        return '\n'.join([para.text for para in doc.paragraphs])
    else:
        return "Unsupported file format"

def translate_text(text, target_lang='hi'):
    return GoogleTranslator(source='en', target=target_lang).translate(text)
