def calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate):
    # Fonction pour calculer le paiement mensuel d'un prêt.
    # Arguments :
    # - loan_amount : Montant total du prêt (float).
    # - duration_years : Durée du prêt en années (int).
    # - annual_interest_rate : Taux d'intérêt annuel en pourcentage (float).
    # Retourne :
    # - Le paiement mensuel arrondi à 2 décimales (float).
    
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # Convertit le taux d'intérêt annuel en un taux mensuel en divisant par 12.
    # Divise également par 100 pour passer de pourcentage à décimal.

    total_payments = duration_years * 12
    # Calcule le nombre total de paiements mensuels en multipliant la durée en années par 12.

    if monthly_interest_rate > 0:
        # Si le taux d'intérêt mensuel est supérieur à 0 :
        # Utilise la formule standard pour calculer le paiement mensuel d'un prêt avec intérêt :
        # M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                          ((1 + monthly_interest_rate) ** total_payments - 1)
    else:
        # Si le taux d'intérêt est nul :
        # Le paiement mensuel est simplement le montant total du prêt divisé par le nombre total de paiements.
        monthly_payment = loan_amount / total_payments

    return round(monthly_payment, 2)
    # Retourne le paiement mensuel arrondi à 2 décimales pour des raisons de lisibilité et de précision.

def calculate_total_cost(monthly_payment, duration_years):
    # Fonction pour calculer le coût total du prêt.
    # Arguments :
    # - monthly_payment : Paiement mensuel (float).
    # - duration_years : Durée du prêt en années (int).
    # Retourne :
    # - Le coût total du prêt arrondi à 2 décimales (float).

    total_payments = duration_years * 12
    # Calcule le nombre total de paiements mensuels.

    total_cost = monthly_payment * total_payments
    # Multiplie le paiement mensuel par le nombre total de paiements pour obtenir le coût total.

    return round(total_cost, 2)
    # Retourne le coût total arrondi à 2 décimales.
