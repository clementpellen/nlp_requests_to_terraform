from openai import OpenAI
from dotenv import load_dotenv
import os

def call_openai_api(client, natural_language_query):
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

def ask_request():
    return input("Quelle est la requête que vous souhaitez effectuer ?\n")

def remove_carriage_return(string):
    return string.replace('\n', ' ')


def main():
    load_dotenv()
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    intro = "Ceci est l'introduction"
    natural_query = ask_request()
    prompt = intro + natural_query
    query = call_openai_api(client, prompt)
    print("\nRequête générée :\n", query)
    # if input("\nSouhaitez-vous l'exécuter ?\n") == 'oui':
    #     print("\nRésultat de la requête :\n", execute_query(temp_db, remove_carriage_return(query)))

if __name__ == "__main__":
    main()