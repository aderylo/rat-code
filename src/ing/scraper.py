import pandas as pd
from io import StringIO
import requests
from bs4 import BeautifulSoup
from utils import complete_schema
from db import add_df_to_db


def fetch_content_generic(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find(id="outlet-content")

    return element.text


def scrape():
    configs = [
        {
            "url": "https://www.ing.pl/indywidualni/tabele-i-regulaminy/oprocentowanie/rachunki-oszczednosciowe-lokaty",
            "schema": "schemas/retail_schema.csv",
        },
        {
            "url": "https://www.ing.pl/dokumenty-fis-i-korporacji/oprocentowanie",
            "schema": "schemas/corporate_schema.csv",
        },
        {
            "url": "https://www.ing.pl/male-firmy/tabele-i-regulaminy/oprocentowanie-mf#oprocentowanie=2",
            "schema": "schemas/enterprise_schema.csv",
        },
    ]

    for config in configs:
        content = fetch_content_generic(config["url"])
        with open(config["schema"], "r") as file:
            schema = file.read()

        filled_schema = complete_schema(schema, content)
        filled_schema = StringIO(filled_schema)
        df = pd.read_csv(filled_schema, sep=";")

        add_df_to_db(df)


if __name__ == "__main__":
    scrape()
