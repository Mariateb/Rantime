import os, webbrowser


exec(open("RantimeGraphUpdate.py").read())
fic = open("graphs/index.html", "w")
fic.write("""
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
	<link rel="stylesheet" href="https://www.w3schools.com/lib/w3-theme-deep-orange.css">
	<title>Rantime Web Viewer</title>
</head>
<body>
	<div class="w3-container w3-theme-d2 w3-center">
		<h1 class="w3-text-white">Rantime Web Viewer</h1>
		<p>Pour les meilleures des sondes.</p>
	</div>
	<div class="w3-rows w3-margin-top">
		<div class="w3-quarter w3-margin-left w3-margin-right w3-theme-d2">
			<div class="w3-margin">
				<h3>Qu'est-ce que Rantime ?</h3>
				<p>Rantime est un logiciel en lignes de commandes qui permet de monitorer l'activité sur une machine Linux (peu importe le système d'exploitation.</p>
				<p>Il y a trois sondes dans Rantime : </p>
				<ul width="100%" class="w3-padding">
					<li>Achil (Python)</li>
					<li>Talon (Python)</li>
					<li>Pinky (Bash)</li>
				</ul>
				<a href="https://github.com/Mariateb/Rantime" class="w3-btn w3-theme-d3">Lien vers le repo git</a>
			</div>
		</div>
		<div class="w3-rest w3-margin w3-padding w3-theme-d2">
		<h3>Historiques</h3>
""")

fic.close()
fic = open("graphs/index.html", "a")
for dir in os.listdir("graphs/images"):
	fic.write("""
			<div class="w3-margin w3-padding w3-theme-d3">
				<h3>Utilisateur : """ + dir + """</h3>
				<table class="w3-table-border" width="100%">
					<tr>
	""")
	for file in os.listdir("graphs/images/" + dir):
		fic.write("""
						<td><img src='images/""" + dir + "/" + file + """'></td>
		""")
	fic.write("""
					</tr>
				<table>
			</div>
	""")
fic.write("""
		</div>
	</div>
</body>
</html>
""")

webbrowser.open("graphs/index.html")
