import pygal
import sqlite3
import webbrowser

# Connection à la base SQL
connection = sqlite3.connect("database/logs.db")
cursor = connection.cursor()
# Récupération des données
command = "SELECT distinct(user) FROM logs"
cursor.execute(command)
listeUsers = cursor.fetchall()
for ligUsers in listeUsers:
	user = ligUsers[0]
	print(user)
	command = "SELECT * FROM dates NATURAL JOIN logs WHERE user = '" + user + "' ORDER BY date_log ASC"
	cursor.execute(command)
	listLogs = cursor.fetchall()
	# On transforme la base en dictionnaire de listes de 3 listes
	for ligne in listLogs:
		print(ligne)
	# On crée le graphe pour chaque utilisateur
	# On génère le svg (qui sera utilisé par le HTML)
line_chart = pygal.Line()
line_chart.title = 'Browser usage evolution (in %)'
line_chart.x_labels = map(str, range(2002, 2013))
line_chart.add('Firefox', [None, None,    0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
line_chart.render_to_file("graphs/images/user.svg")
# On ouvre le fichier HTML
# webbrowser.open_new_tab("graphs/index.html")
