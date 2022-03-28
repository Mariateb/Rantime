import sqlite3

connection = sqlite3.connect("database/logs.db")
cursor = connection.cursor()

command = "SELECT * FROM logs WHERE cpu > 50;"
cursor.execute(command)
listeUrgences = cursor.fetchall()

print("*******************")
print("       STATUT      ")
print("*******************")

if listeUrgences != []:
	print("Urgence(s) détectée(s) !")
	for row in listeUrgences:
		print("Identifiant : " + row[0] + ", User : " + row[1])
	print("Envoi du mail...")
		
else:
	print("Aucune urgence détectée")
