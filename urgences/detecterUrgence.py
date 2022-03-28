import sqlite3
import smtplib, ssl

connection = sqlite3.connect("database/logs.db")
cursor = connection.cursor()

command = "SELECT * FROM logs WHERE cpu > 80;"
cursor.execute(command)
listeUrgences = cursor.fetchall()

print("*******************")
print("       STATUT      ")
print("*******************")

if listeUrgences != []:
	print("Urgence(s) détectée(s) !")
	identifiantsCrise = ""
	for row in listeUrgences:
		identifiant = "Identifiant : " + row[0] + ", User : " + row[1]
		identifiantsCrise += identifiant + "\n"
	print("Envoi du mail...")
	fic = open('urgences/mailTemplate.txt', 'r')
	mailTemplate = fic.read()
	fic.close()
	mailDest = mailTemplate.split("//////")[0]
	mailContenu = mailTemplate.split("//////")[1]
	print("Destinataire : " + mailDest)
	mailContenu = mailContenu.replace("$(list)", identifiantsCrise)
	
	context = ssl.create_default_context()
	with smtplib.SMTP_SSL("smtpz.univ-avignon.fr", 465, context=context) as server:
		mdp = input("Entrez le mot de passe pour envoyer le mail : ")
		server.login("sabri.moussa@alumni.univ-avignon.fr", mdp)
		server.sendmail("sabri.moussa@alumni.univ-avignon.fr", mailDest, mailContenu)
	print("Mail envoyé !")
	
else:
	print("Aucune urgence détectée")

