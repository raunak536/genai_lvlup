import pymupdf

def parse_pdf(pdf_path):
    text = ""
    doc = pymupdf.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text