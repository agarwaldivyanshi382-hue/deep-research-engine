import requests
from bs4 import BeautifulSoup
from pdf_parser import extract_pdf_text


def fetch_content(url):

    try:

        # PDF handling
        if ".pdf" in url.lower():

            return extract_pdf_text(url)

        # Normal webpage handling
        response = requests.get(
            url,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return text[:3000]

    except Exception as e:

        print(e)

        return ""