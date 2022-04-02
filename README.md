# Rantime

Rantime est un outil pour sonder des détails de l'OS Linux utilisé actuellement, et ce pour tous les utilisateurs.
Il est composé de trois sondes :
- Talon (%RAM utilisée) (Python)
- Achilles (%CPU utilisé) (Python)
- Pinky (VSZ allouée) (Bash)
L'outil permet également de détecter une situation de crise, et si la situation le demande, envoyer un mail à l'administrateur.
(Le fichier urgences/mailTemplate.txt est modifiable et permet de donner le récepteur du mail)

Le script Rantime.sh permet de lancer les sondes et de stocker le résultat dans une base SQL : database/logs.db

Le script RantimeRepeat.sh permet de lancer une routine qui exécute Rantime à intervalles réguliers en arrière plan.

Le script RantimeStats.sh permet d'avoir les statistiques actuelles des sondes sous forme de graphique (pour chaque utilisateur)

Le script RantimeWebDisplayer.py permet de générer (et d'afficher) une page web donnant l'ensemble des informations.

# Librairies utilisées

- subprocess (Python)
- os (Python)
- webbrowser (Python)
- datetime (Python)
- sqlite3 (Python)
- pygal (Python)
- smptlib (Python)
- feh (Bash)
