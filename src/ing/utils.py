from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()


def complete_schema(schema: str, content: str):
    prompt = (
        "Here you have a table,"
        + schema
        + """can you fill in the tokens FILL_IN
            with correct data based on following"""
        + content
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "text"},
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output semicolon delimited tables.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content
