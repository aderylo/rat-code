from pko.scraper import scrape as pko_scrape
from utils.db import Session
from utils.models import DepositLog


if __name__ == "__main__":
    # with Session() as session:
    #     d= DepositLog(id=1, deposit_type='test', over=1, under=1, term=1, currency='test', interest=1, bank='test')
    #     session.add(d)
    #     session.commit()

    pko_scrape()

