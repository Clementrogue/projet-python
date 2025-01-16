# Crée et configure l'environnement virtuel
init:
	python3 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

# Lance l'application
run: init
	. venv/bin/activate && python app.py

# Exécute les tests unitaires
test: init
	. venv/bin/activate && python -m unittest discover -s tests -p "*.py"

# Supprime l'environnement virtuel et nettoie les fichiers temporaires
clean:
	rm -rf venv
	find . -type d -name "__pycache__" -exec rm -r {} +

# Variables Makefile pour plus de flexibilité
VENV = venv
REQUIREMENTS = requirements.txt

init_with_vars:
	python3 -m venv $(VENV)
	. $(VENV)/bin/activate && pip install -r $(REQUIREMENTS)
