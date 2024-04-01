# nlp_requests_to_terraform
Ceci est le dépôt de NLP Requests To Terraform

## Commandes

### Création d'un environnement virtuel
```bash
python -m venv venv
```

### Activation de l'environnement virtuel 

Windows :
```powershell
.\venv\Scripts\Activate
```

Linux :
```bash
source venv/bin/activate
```

### Installation des dépendances
```cmd
pip install -r requirements.txt
```

### Exécution du script
```cmd
python main.py
```


## Développement des requêtes

➡️ Main.py

```python
############################################
# VARIABLES
############################################

intro = "Définir le contexte de la requête ici (languages, besoins ...)"

natural_query = "Définir la requête spécifique ici"
```


## Développement de code

➡️ Créer un fichier *file.py* 

➡️ Importer le fichier dans *main.py*
### Exemple :
```python
from openai_api import call_openai_api
```
