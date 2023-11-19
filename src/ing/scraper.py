import pandas as pd
from io import StringIO
import requests
from bs4 import BeautifulSoup
from utils.utils import complete_schema, save_df
from pathlib import Path

def get_content_from_html(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find(id="outlet-content")

    return element.text


def scrape():
    current_dir = Path(__file__).resolve().parent
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
        content = get_content_from_html(config["url"])
        with open(current_dir / config["schema"], "r") as file:
            schema = file.read()

        filled_schema = complete_schema(schema, content)
        filled_schema = StringIO(filled_schema)
        df = pd.read_csv(filled_schema, sep=";")
        df["bank"] = "ING"
        save_df(df)


if __name__ == "__main__":
    scrape()
