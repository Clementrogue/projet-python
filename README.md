Flask App - Modèle de Projet DevOps

Ce dépôt sert de modèle pour un projet DevOps simple basé sur Flask. L'application propose des fonctionnalités de calcul de base (addition et soustraction) et inclut tous les fichiers nécessaires pour configurer un environnement local, exécuter des tests, et déployer sur un service cloud en suivant les meilleures pratiques DevOps.
Structure du Projet

DEVOPS-PROJECT/
├── app.py
├── utils.py
├── test.py
├── requirements.txt
├── Makefile
├── templates/
│   └── home.html
├── .env
├── .gitignore

Description des Fichiers

    app.py : Fichier principal de l'application Flask. Configure les routes et les connecte aux fonctions définies dans utils.py pour fournir des points de terminaison API.

    utils.py : Contient les fonctions utilitaires pour les opérations principales (addition, soustraction). Ce fichier centralise la logique de l'application.

    test.py : Fichier de tests unitaires, contenant les tests des fonctions définies dans utils.py afin de garantir le bon fonctionnement de l'application.

    requirements.txt : Liste des dépendances Python nécessaires au fonctionnement de l'application. Ce fichier est utilisé pour installer les bibliothèques requises dans l'environnement.

    Makefile : Fichier Make qui simplifie la gestion du projet avec des commandes comme :
        make init : Installer les dépendances.
        make run : Lancer l'application Flask.
        make test : Exécuter les tests unitaires.

    templates/home.html : Modèle HTML pour l'interface utilisateur de l'application. Ce fichier inclut des champs d'entrée et des boutons pour interagir avec les opérations du calculateur.

    .env : Fichier de configuration pour les variables d'environnement. Il est utilisé pour stocker des informations sensibles (comme des clés API, identifiants de base de données ou paramètres spécifiques à l'environnement). ⚠️ Ce fichier ne doit pas être versionné dans Git.

    .gitignore : Liste des fichiers et dossiers à ignorer par Git, comme .env, les fichiers compilés Python (__pycache__), et les caches locaux.

Guide de Démarrage

    Cloner le Dépôt :

git clone <repository-url>
cd DEVOPS-PROJECT

Configurer l'Environnement :

    Créez et activez un environnement virtuel (recommandé pour gérer les dépendances).
    Installez les dépendances :

    make init

Lancer l'Application :

    Exécutez l'application Flask en local :

    make run

Exécuter les Tests :

    Vérifiez la fonctionnalité en exécutant les tests unitaires :

        make test

Configuration Supplémentaire
Variables d'Environnement :

    Utilisez le fichier .env pour configurer les paramètres spécifiques à votre environnement ou pour stocker des informations sensibles.
    Assurez-vous que ce fichier est inclus dans .gitignore pour éviter de le versionner.

Instructions de Déploiement

Pour le déploiement, configurez des pipelines CI/CD adaptés à votre plateforme préférée (par exemple, GitHub Actions, Azure Pipelines). Ce modèle est compatible avec les plateformes de déploiement cloud comme AWS, Azure ou Heroku pour une évolutivité facile.

    Utilisez pipeline.yaml comme modèle pour créer un pipeline de construction et de déploiement, notamment sur Azure.

Points Forts de ce Modèle

    Structure claire et modulaire.
    Intégration facile avec des outils CI/CD.
    Conformité aux bonnes pratiques de gestion d'environnements sécurisés.
