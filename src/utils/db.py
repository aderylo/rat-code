from sqlalchemy import URL, create_engine
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from utils.models import Base, DepositLog

connection_string = URL.create(
  'postgresql',
  username='a.derylo2',
  password='Q7enkV3absfr',
  host='ep-snowy-pond-99254375-pooler.eu-central-1.aws.neon.tech', 
  database='depo',
)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


if __name__ == "__main__":
  with Session() as session:
     DepositLog(id=1, deposit_type='test', over=1, under=1, term=1, currency='test', interest=1, bank='test')