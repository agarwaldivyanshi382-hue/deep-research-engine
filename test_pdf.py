from pdf_parser import extract_pdf_text

url = "https://aclanthology.org/P19-1050.pdf"

text = extract_pdf_text(url)

print(text[:2000])