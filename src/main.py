from pko.scraper import scrape as pko_scrape
from ing.scraper import scrape as ing_scrape
from utils.db import Session
from utils.models import DepositLog


if __name__ == "__main__":
    pko_scrape()
    ing_scrape()

