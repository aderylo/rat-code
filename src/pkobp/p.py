import pandas as pd
from io import StringIO


data = """
deposit_type;over;under;term;details;interest
Rachunki oszczędnościowo-rozliczeniowe, z wyjątkiem wymienionego w pkt 2;NA;NA;NA;NA;FILL_IN
Rachunek oszczędnościowo–rozliczeniowy PKO Konto Dziecka oraz PKO Konto dla Młodych (poniżej 18 roku życia);0;2500;NA;NA;FILL_IN
"""

# Use StringIO to convert the string data into a file-like object
string_data = StringIO(data)

# Create the DataFrame
df = pd.read_csv(string_data, sep=';')


from utils import transform_df_to_json

json_data = transform_df_to_json(df)
print(json_data)


print(df.head())
