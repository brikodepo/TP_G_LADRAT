# Script de Détection de Vulnérabilités Path Traversal

Ce script permet de tester les vulnérabilités de type "Path Traversal" sur un serveur web cible. Il tente d'accéder à des fichiers sensibles en utilisant des chemins spécifiques pour identifier des failles potentielles.

## Fonctionnalités

- Test de plusieurs chemins potentiellement vulnérables.
- Génération automatique d'un rapport détaillant les vulnérabilités détectées.
- Journalisation des résultats dans un fichier de rapport horodaté.

## Pré-requis

- Python 3.x
- Bibliothèque `requests` (peut être installée avec `pip install requests`)

## Installation

1. Clonez ou téléchargez ce dépôt.
2. Assurez-vous d'avoir Python installé sur votre système.
3. Installez les dépendances avec la commande suivante :

   ```bash
   pip install -r requirements.txt
