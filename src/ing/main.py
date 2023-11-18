import requests
from bs4 import BeautifulSoup
from scraper import fetch_content_generic



configs = [
    {
        "url" : "https://www.ing.pl/indywidualni/tabele-i-regulaminy/oprocentowanie/rachunki-oszczednosciowe-lokaty",
        "schema" : "schemas/retail_schema.csv", 
    }
] 


for config in configs:
    content = fetch_content_generic(config["url"])
    print(content.text.strip("\n "))


