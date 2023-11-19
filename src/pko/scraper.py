import pandas as pd
from io import StringIO
import requests
from bs4 import BeautifulSoup
from utils.utils import complete_schema, get_pdf_content, save_df
from pathlib import Path

def get_content_from_linked_file(url, find_by):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    elem = soup.find(*find_by)
    href = elem.get("href")
    document_url = f"https://www.pkobp.pl{href}"

    return get_pdf_content(document_url)


def scrape():
    current_dir = Path(__file__).resolve().parent
    configs = [
        {
            "url": "https://www.pkobp.pl/oplaty-i-oprocentowanie/oprocentowanie",
            "find_by": [
                "a",
                {
                    "aria-label": "Pobierz lub otwórz plik Tabela 1. Oprocentowanie środków pieniężnych na rachunkach bankowych nieoszczędnościowych na rachunkach powierniczych oraz rachunkach pieniężnych"
                },
            ],
            "schema": "schemas/corporate_schema.csv",
        },
    ]

    for config in configs:
        content = get_content_from_linked_file(config["url"], config["find_by"])
        with open(current_dir / config["schema"], "r") as file:
            schema = file.read()

        filled_schema = complete_schema(schema, content)
        filled_schema = StringIO(filled_schema)
        df = pd.read_csv(filled_schema, sep=";")

        save_df(df)


if __name__ == "__main__":
    scrape()
