import pymupdf

def parse_pdf(pdf_path):
    text = ""
    doc = pymupdf.open(pdf_path)
    text_with_metadata = []
    for page_num, page in enumerate(doc):
        text_with_metadata.append([page_num+1, page.get_text()])
    return text_with_metadata