from bs4 import BeautifulSoup
import requests
import PyPDF2
import io

def get_retail_offer_pdf_url():
    url = "https://www.pkobp.pl/oplaty-i-oprocentowanie/oprocentowanie"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    elem = soup.find(
        "a",
        {
            "aria-label": "Pobierz lub otwórz plik Cz I. Rachunki bankowe w ofercie dla osób fizycznych"
        },
    )
    href = elem.get("href")

    return f"https://www.pkobp.pl{href}"



def get_corporate_offer_pdf_url():
    url = "https://www.pkobp.pl/oplaty-i-oprocentowanie/oprocentowanie"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    elem = soup.find(
        "a",
        {
            "aria-label": "Pobierz lub otwórz plik Tabela 1. Oprocentowanie środków pieniężnych na rachunkach bankowych nieoszczędnościowych na rachunkach powierniczych oraz rachunkach pieniężnych"
        },
    )
    href = elem.get("href")

    return f"https://www.pkobp.pl{href}"



def get_pdf(url):
    response = requests.get(url)
    if 'application/pdf' in response.headers.get('Content-Type', ''):
        return io.BytesIO(response.content)
    else:
        raise ValueError("URL did not point to a PDF")


def extract_text_from_pdf(pdf_stream):
    reader = PyPDF2.PdfReader(pdf_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Usage
url = get_retail_offer_pdf_url()
pdf_stream = get_pdf(url)
pdf_text = extract_text_from_pdf(pdf_stream)

file_path = "retail_schema.csv"  # Replace with the actual file path
with open(file_path, "r") as file:
    file_text = file.read()


from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
prompt = """Here you have a table,""" +  file_text + """can you fill in the tokens FILL_IN 
            with correct data based on following""" + pdf_text
print(len(prompt.split(" ")))

# response = client.chat.completions.create(
#   model="gpt-4",
#   response_format={ "type": "text" },
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant designed to output semicolon delimited tables."},
#     {"role": "user", "content": prompt},
#   ]
# )
# print(response.choices[0].message.content)







