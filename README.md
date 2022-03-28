# Rantime

Rantime est un outil pour sonder des détails de l'OS Linux utilisé actuellement, et ce pour tous les utilisateurs.
Il est compoés de trois sondes :
- Talon (%RAM utilisée) (Python)
- Achilles (%CPU utilisé) (Python)
- Pinky (VSZ allouée) (Bash)

Le script Rantime.sh permet de lancer les sondes et de stocker le résultat dans une base SQL : database/logs.db
Le script RantimeRepeat.sh permet de lancer une routine qui exécute Rantime à intervalles réguliers

# À faire
1. Rantime.sh devra supprimer les valeurs trop vieilles de la base SQL.
2. Créer des scripts pour sauvegarder/restaurer la base SQL.
