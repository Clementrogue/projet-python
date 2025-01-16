import unittest
from utils import calculate_monthly_payment, calculate_total_cost
# Importation de la bibliothèque `unittest` pour écrire et exécuter des tests unitaires.
# Les fonctions `calculate_monthly_payment` et `calculate_total_cost` sont importées depuis `utils.py`.

class TestLoanCalculatorUtils(unittest.TestCase):
    # Définition d'une classe de test qui hérite de `unittest.TestCase`.
    # Cette classe regroupe tous les tests relatifs aux fonctions du calculateur de prêt.

    def test_calculate_monthly_payment_with_interest(self):
        # Test pour vérifier que le calcul du paiement mensuel est correct lorsqu'un taux d'intérêt est appliqué.
        loan_amount = 10000  # Montant du prêt
        duration_years = 5   # Durée du prêt en années
        annual_interest_rate = 5  # Taux d'intérêt annuel en pourcentage
        expected_payment = 188.71  # Résultat attendu du paiement mensuel
        
        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        # Appel de la fonction pour calculer le paiement mensuel.
        
        self.assertAlmostEqual(result, expected_payment, places=2)
        # Vérifie que le résultat calculé est presque égal au résultat attendu avec une précision de 2 décimales.

    def test_calculate_monthly_payment_no_interest(self):
        # Test pour vérifier le calcul du paiement mensuel sans taux d'intérêt (taux = 0).
        loan_amount = 10000  # Montant du prêt
        duration_years = 5   # Durée du prêt en années
        annual_interest_rate = 0  # Taux d'intérêt annuel en pourcentage
        expected_payment = 166.67  # Résultat attendu du paiement mensuel
        
        result = calculate_monthly_payment(loan_amount, duration_years, annual_interest_rate)
        # Appel de la fonction pour calculer le paiement mensuel sans intérêt.
        
        self.assertAlmostEqual(result, expected_payment, places=2)
        # Vérifie que le résultat calculé est presque égal au résultat attendu avec une précision de 2 décimales.

    def test_calculate_total_cost(self):
        # Test pour vérifier que le calcul du coût total du prêt est correct.
        monthly_payment = 188.71  # Paiement mensuel
        duration_years = 5        # Durée du prêt en années
        expected_total_cost = 11322.6  # Résultat attendu du coût total (paiement x durée)
        
        result = calculate_total_cost(monthly_payment, duration_years)
        # Appel de la fonction pour calculer le coût total du prêt.
        
        self.assertAlmostEqual(result, expected_total_cost, places=2)
        # Vérifie que le résultat calculé est presque égal au résultat attendu avec une précision de 2 décimales.

if __name__ == '__main__':
    unittest.main()
    # Point d'entrée pour exécuter les tests lorsque le script est exécuté directement.
