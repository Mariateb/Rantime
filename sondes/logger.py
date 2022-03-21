import subprocess
import sqlite3
import string
import random

# On lit le fichier results.txt, et on gère son contenu
fic = open("sondes/result.txt", "r")
date = fic.readline()
talon = eval(fic.readline())
achil = eval(fic.readline())
pinky = eval(fic.readline())
fic.close()
print(date)
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
cursor.execute("INSERT INTO dates VALUES(?, ?)", (idLog, date,))
for keys in dicoLog:
	cursor.execute("INSERT INTO logs VALUES(?, ?, ?, ?, ?)",(idLog, key, round(dicoLog[key][0],2), round(dicoLog[key][1],2), dicoLog[key][2]))
# On commit les résultats
connection.commit()
