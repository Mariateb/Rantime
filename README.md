# Rantime

Rantime est un outil pour sonder des détails de l'OS Linux utilisé actuellement, et ce pour tous les utilisateurs.
Il est compoés de trois sondes :
- Talon (%RAM utilisée) (Python)
- Achilles (%CPU utilisé) (Python)
- Pinky (VSZ allouée) (Bash)

Le script Rantime.sh permet de lancer les sondes et de stocker le résultat dans une base SQL : database/logs.db

Le script RantimeRepeat.sh permet de lancer une routine qui exécute Rantime à intervalles réguliers

# Librairies utilisées

1. subprocess (Python)
2. sqlite3 (Python)

# À faire

Étape 2 :
1. Rantime.sh devra supprimer les valeurs trop vieilles de la base SQL.
2. Créer des scripts pour sauvegarder/restaurer la base SQL.
Étape 3 :
3. Script qui affiche la base SQL sous forme de graphes. (Option : Couleur) (pygal)
4. Script qui détecte une situation de crise.
5. Script d'envoi par e-mail. (Option : Fichier template) (smtplib)
Étape 4 :
6. Interface Web pour visualiser les graphes.
