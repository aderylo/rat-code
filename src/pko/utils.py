from dotenv import load_dotenv
from openai import OpenAI
import requests
import io
import PyPDF2

load_dotenv()
client = OpenAI()


def complete_schema(schema: str, content: str):
    prompt = (
        "Here you have a table,"
        + schema
        + """can you fill in the tokens FILL_IN
            with correct data based on following"""
        + content
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "text"},
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output semicolon delimited tables.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content


def extract_text_from_pdf(pdf_stream):
    reader = PyPDF2.PdfReader(pdf_stream)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


def get_pdf_content(url):
    response = requests.get(url)
    if "application/pdf" in response.headers.get("Content-Type", ""):
        return extract_text_from_pdf(io.BytesIO(response.content))
    else:
        raise ValueError("URL did not point to a PDF")
