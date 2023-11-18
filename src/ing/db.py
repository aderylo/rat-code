import json
import os

def add_record_to_db(record, filename='db.json'):
    """
    Adds a new record to the JSON file.
    """
    try:
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file)  # Create an empty list in the file

        with open(filename, 'r+') as file:
            data = json.load(file)
            data.append(record)
            file.seek(0)  # Go to the beginning of the file
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"An error occurred: {e}")


def add_df_to_db(df, filename='db.json'):
    json_list = df.to_dict(orient='records')
    add_record_to_db(json_list, filename)


def get_all_records_from_db(filename='db.json'):
    """
    Retrieves all records from the JSON file.
    """
    try:
        if not os.path.exists(filename):
            return []  # Return an empty list if the file does not exist

        with open(filename, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    # Usage
    new_record = {"name": "John Doe", "age": 30}
    add_record_to_db(new_record)
    add_record_to_db(new_record)


    all_records = get_all_records_from_db()
    print(all_records)
