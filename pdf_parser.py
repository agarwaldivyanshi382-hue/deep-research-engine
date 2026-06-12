import fitz
import requests


def extract_pdf_text(url):

    response = requests.get(url)

    with open(
        "temp.pdf",
        "wb"
    ) as f:

        f.write(
            response.content
        )

    pdf = fitz.open(
        "temp.pdf"
    )

    text = ""

    for page in pdf:

        text += page.get_text()

    return text