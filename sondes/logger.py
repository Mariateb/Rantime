import subprocess
import sqlite3

# On lit le fichier results.txt, et on gère son contenu
fic = open("result.txt", "r")
date = fic.readline()
talon = eval(fic.readline())
achil = eval(fic.readline())
pinky = eval(fic.readline())
# On réunit tout en un seul dictionaire
dicoLog = {}
for key in talon:
	if (key in achil) and (key in pinky):
		dicoLog[key] = [talon[key],achil[key],pinky[key]]
# On enregistre nos trouvailles dans la base
