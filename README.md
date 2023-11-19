# supervisionhack-23

## Extensible deposit and savings interest rate offer monitoring 

We have provided several examples for a few deposit providers of how to setup the scraping & parsing pipeline. Generally, introducing new data source requires only one time creation of data schema and choosing corresponding data fetching method (pdf or html). 


## Prerequisites

Not much is needed other than a few dependencies:
```
pip install -r requirements.txt
```

And .env file populated with following keys:
```
OPENAI_API_KEY=<your_openai_key>
PGUSER=<postgresql_username>
PGPASSWORD=postgresql_password
```


## Running 
Once everything is set up, simply execute:
```
python src/main.py 
```

## Extensibility

Our solution is designed in such a way that with minimal coding knowledge one can introduce new 
data sources to be monitored. Simply copy one of the folders (`ing` if data is contained on a website, if it is in a pdf then `pko`) and change create data schemas using the provided notebook! And that is all! 