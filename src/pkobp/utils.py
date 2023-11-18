import pandas as pd

def transform_table_to_json(filename):
    df = pd.read_csv(filename, sep=';')
    json_list = df.to_dict(orient='records')

    return json_list

def transform_df_to_json(df):
    json_list = df.to_dict(orient='records')
    
    return json_list

# Example Usage
filename = 'retail_schema.csv'  # Replace with your actual file name
with open(filename, 'r') as file:
    text = file.read()

json_data = transform_table_to_json(filename)
print(len(str(json_data).split()))
print(len(text.split()))