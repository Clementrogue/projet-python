from flask import Flask, render_template, request, jsonify
# Importation des modules nécessaires de Flask pour créer une application web :
# - `Flask` pour créer l'application,
# - `render_template` pour rendre les fichiers HTML,
# - `request` pour gérer les données envoyées par l'utilisateur,
# - `jsonify` pour renvoyer les réponses sous forme de JSON.

from utils import calculate_monthly_payment, calculate_total_cost
# Importation de fonctions utilitaires définies dans un fichier `utils.py` :
# - `calculate_monthly_payment` : pour calculer les paiements mensuels,
# - `calculate_total_cost` : pour calculer le coût total du prêt.

app = Flask(__name__)
# Création de l'application Flask, en passant le nom du module actuel.

@app.route('/')
def home():
    # Définition de la route pour la page d'accueil.
    # Lorsque l'utilisateur accède à "/", la fonction `home` est appelée.
    return render_template('home.html')
    # Rendu du fichier HTML `home.html` situé dans le répertoire `templates`.

@app.route('/calculate', methods=['POST'])
def calculate():
    # Définition d'une route pour le calcul des paiements. 
    # La méthode HTTP `POST` est utilisée, car les données (montant, durée, taux) sont envoyées par un formulaire.

    loan_amount = float(request.form['loan_amount'])
    # Récupération du montant du prêt envoyé via le formulaire HTML et conversion en float.
    
    duration_years = int(request.form['duration'])
    # Récupération de la durée du prêt (en années) envoyée via le formulaire et conversion en entier.
    
    annual_interest_rate = float(request.form['interest_rate'])
    # Récupération du taux d'intérêt annuel envoyé via le formulaire et conversion en float.

    monthly_payment = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
    # Calcul du paiement mensuel en utilisant la fonction utilitaire `calculate_monthly_payment`.
    
    total_cost = calculate_total_cost(monthly_payment, duration_years)
    # Calcul du coût total du prêt (paiement mensuel x nombre de mois) en utilisant `calculate_total_cost`.

    return jsonify({
        'monthly_payment': monthly_payment,
        'total_cost': total_cost
    })
    # Retourne une réponse JSON contenant le paiement mensuel et le coût total.
    # Cette réponse est utilisée pour afficher les résultats à l'utilisateur sans recharger la page.

if __name__ == '__main__':
    # Condition pour s'assurer que le script est exécuté directement et non importé comme module.
    app.run(debug=True)
    # Lancement de l'application Flask en mode debug :
    # - Permet de voir les erreurs en détail,
    # - Recharge automatiquement le serveur si le code est modifié.
