import pygal, datetime, os
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
	command = "SELECT * FROM dates NATURAL JOIN logs WHERE user = '" + user + "' ORDER BY date_log ASC"
	cursor.execute(command)
	listLogs = cursor.fetchall()
	laListe = [[],[],[],[]]
	for ligne in listLogs:
		# On fait une liste des datetimes
		laListe[0].append(ligne[1].replace("/", " ").replace(":", " ").replace('\n', " ").split(" "))
		# Liste de cpu usage
		laListe[1].append(ligne[3])
		# Liste de ram usage
		laListe[2].append(ligne[4])
		# Liste de VSZ
		laListe[3].append(ligne[5])
	# Liste des datetimes
	listeDatetime = []
	for i in laListe[0]:
		listeDatetime.append(datetime.datetime(int(i[0]), int(i[1]), int(i[2]), int(i[3]), int(i[4]), int(i[5])))
	# On crée le directory si il n'existe pas
	if not os.path.exists("graphs/images/" + user):
		os.mkdir("graphs/images/" + user)
	# VSZ
	lineChart = pygal.Line(x_label_rotation=40)
	lineChart.title = "VSZ allouée pour l'utilisateur " + user
	lineChart.x_labels = map(lambda d: d.strftime('%Y/%m/%d %H:%M:%S'), listeDatetime)
	lineChart.add("VSZ", laListe[3])
	lineChart.render_to_file("graphs/images/" + user + "/vsz.svg")
	# CPU
	lineChart = pygal.Line(x_label_rotation=40)
	lineChart.title = "CPU utilisé pour l'utilisateur " + user
	lineChart.x_labels = map(lambda d: d.strftime('%Y/%m/%d %H:%M:%S'), listeDatetime)
	lineChart.add("CPU", laListe[1])
	lineChart.render_to_file("graphs/images/" + user + "/cpu.svg")
	# RAM
	lineChart = pygal.Line(x_label_rotation=40)
	lineChart.title = "RAM utilisée pour l'utilisateur " + user
	lineChart.x_labels = map(lambda d: d.strftime('%Y/%m/%d %H:%M:%S'), listeDatetime)
	lineChart.add("RAM", laListe[2])
	lineChart.render_to_file("graphs/images/" + user + "/ram.svg")
