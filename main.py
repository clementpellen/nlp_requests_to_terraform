from openai_api import call_openai_api


############################################
# VARIABLES
############################################

intro = "Ceci est l'introduction"

natural_query = ""


############################################
# FUNCTIONS
############################################

def ask_request():
    return input("Quelle est la requête que vous souhaitez effectuer ?\n")

def remove_carriage_return(string):
    return string.replace('\n', ' ')


############################################
# MAIN
############################################

def main():
    global natural_query

    natural_query = natural_query if natural_query != "" else ask_request()

    prompt = intro + natural_query
    query = call_openai_api(prompt)
    print("\nRequête générée :\n", query)


    # Code d'exécution de la requête Terraform
    # if input("\nSouhaitez-vous l'exécuter ?\n") == 'oui':
    #     print("\nRésultat de la requête :\n", execute_query(temp_db, remove_carriage_return(query)))



if __name__ == "__main__":
    main()