import subprocess, string, random, re, datetime
import sqlite3

# On lit le fichier results.txt, et on gère son contenu
fic = open("sondes/result.txt", "r")
laDate = fic.readline()
talon = eval(fic.readline())
achil = eval(fic.readline())
pinky = eval(fic.readline())
fic.close()
print(laDate)
# On réunit tout en un seul dictionaire
dicoLog = {}
for key in talon:
	if (key in achil) and (key in pinky):
		dicoLog[key] = [talon[key],achil[key],pinky[key]]
# Connexion à la base SQL
connection = sqlite3.connect("database/logs.db")
cursor = connection.cursor()
# On crée nos deux tables si elles n'existent pas
command = """CREATE TABLE IF NOT EXISTS
logs(id_logs VARCHAR(10) PRIMARY KEY, user VARCHAR(20), ram FLOAT, cpu FLOATT, vsz INTEGER)
"""
cursor.execute(command)
command = """CREATE TABLE IF NOT EXISTS
dates(id_logs VARCHAR(10) PRIMARY KEY, date_log DATETIME)
"""
cursor.execute(command)
# On génère un identifiant de log et on vérifie si il est unique
idLog = ''.join(random.choice(string.digits) for _ in range(10))
# On enregistre les valeurs 
cursor.execute("INSERT INTO dates VALUES(?, ?)", (idLog, laDate,))
for keys in dicoLog:
	cursor.execute("INSERT INTO logs VALUES(?, ?, ?, ?, ?)",(idLog, key, round(dicoLog[key][0],2), round(dicoLog[key][1],2), dicoLog[key][2]))
# On commit les résultats une première fois
connection.commit()
# On récupère tous les identifiants différents
cursor.execute("SELECT * FROM dates")
identifiants = cursor.fetchall()
# Pour chaque ligne, on regarde si la date est trop vieille
# (Si elle date de + de 30 secondes)
for row in identifiants:
	print(row)
	# On sépare la date en une liste pour avoir chaque valeur
	listdate = row[1].replace("/", " ").replace(":", " ").replace("\n", " ").split()
	# On trouve l'ancienneté en secondes du log
	diffTemps = datetime.datetime.now() - datetime.datetime(int(listdate[0]), int(listdate[1]), int(listdate[2]), int(listdate[3]), int(listdate[4]), int(listdate[5]))
	anciennete = diffTemps.total_seconds()
	# Si c'est plus vieux que 30 secondes (pour les tests), on supprime
	if(anciennete > 300):
		idASupprimer = row[0]
		commande = "DELETE FROM dates WHERE id_logs ='" + idASupprimer + "';"
		cursor.execute(commande)
		commande = "DELETE FROM logs WHERE id_logs ='" + idASupprimer + "';"
		cursor.execute(commande)
		connection.commit()
		print("Supprimé la case " + idASupprimer + " car trop vieux.")
	else:
		print(anciennete)
