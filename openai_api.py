from openai import OpenAI
from dotenv import load_dotenv
from cryptography.fernet import Fernet
import os

def call_openai_api(natural_language_query):
    load_dotenv()
    key = os.getenv("MY_KEY")
    cipher_suite = Fernet(key)
    client = OpenAI(api_key=cipher_suite.decrypt(os.getenv("OPENAI_API_KEY")).decode("utf-8"))

    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": natural_language_query,
                }
            ],
            model="gpt-3.5-turbo",
            temperature=0.1,
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)