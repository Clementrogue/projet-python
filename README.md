# Application Flask - Modèle de Projet DevOps

Ce dépôt sert de modèle pour un projet DevOps simple construit avec Flask. L'application inclut un calculateur de prêt permettant de calculer les mensualités et le coût total d'un emprunt. Ce projet est conçu pour suivre les meilleures pratiques DevOps, avec des configurations pour un déploiement local, des tests unitaires et des pipelines d'intégration et de déploiement continus (CI/CD).

---

## Structure du Projet

```
clementrogue-projet-python/
├── README.md                   # Documentation du projet
├── Dockerfile                  # Configuration Docker pour la conteneurisation
├── Makefile                    # Commandes pour configurer, exécuter et tester le projet
├── app.py                      # Fichier principal de l'application Flask
├── pipeline.yaml               # Exemple de configuration pour pipeline CI/CD
├── requirements.txt            # Liste des dépendances Python
├── test.py                     # Tests unitaires pour les fonctions utilitaires
├── utils.py                    # Logique principale pour les calculs de prêt
├── Template/                   # Modèles HTML pour l'interface utilisateur
│   ├── home.html               # Interface utilisateur du calculateur de prêt
│   └── test                    # Fichier placeholder pour ressources supplémentaires
└── .github/
    └── workflows/              # Workflows GitHub Actions pour CI/CD
        ├── main_projet.yml     # Workflow pour le déploiement Azure (projet spécifique)
        ├── main_py.yml         # Workflow pour le déploiement Azure (Python spécifique)
        ├── makefile.yml        # Workflow basé sur Makefile pour la construction et les tests
        └── test                # Placeholder pour workflows supplémentaires
```

---

## Fonctionnalités

- **Calculateur de Prêt** : Une application web simple permettant de calculer les mensualités et le coût total d'un prêt en fonction du montant, du taux d'intérêt et de la durée.
- **Structure Modulaire** : Une organisation claire pour faciliter l'extension et la maintenance du projet.
- **Intégration CI/CD** : Workflows GitHub Actions fournis pour automatiser les tests et le déploiement.
- **Support Docker** : Fichier Docker prêt à l'emploi pour la conteneurisation.
- **Configuration Environnementale** : Utilisation de fichiers `.env` pour des configurations spécifiques et sécurisées.

---

## Instructions d’Installation

### 1. Cloner le Dépôt

```bash
git clone <repository-url>
cd clementrogue-projet-python
```

### 2. Créer et Activer un Environnement Virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Sous Windows, utilisez `venv\Scripts\activate`
```

### 3. Installer les Dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer l’Application

```bash
make run
```

Accédez à l'application à l'adresse suivante : `http://127.0.0.1:5000`.

### 5. Exécuter les Tests Unitaires

```bash
make test
```

---

## Déploiement

Le projet est pré-configuré pour être déployé sur Azure Web Apps via GitHub Actions.

1. Remplacez les variables placeholder dans les fichiers `.github/workflows/*.yml` avec les détails de votre application Azure Web App.
2. Poussez vos modifications sur la branche `main` pour déclencher les pipelines CI/CD.

---

## Contribuer

1. Forkez le dépôt.
2. Créez une nouvelle branche : `git checkout -b nom-fonctionnalité`.
3. Faites vos modifications et commitez-les : `git commit -m 'Ajout d'une nouvelle fonctionnalité'`.
4. Poussez votre branche : `git push origin nom-fonctionnalité`.
5. Ouvrez une Pull Request.

---

## Licence

Ce projet est sous licence [MIT](LICENSE).
