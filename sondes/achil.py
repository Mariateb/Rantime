import subprocess

commande = "ps -ux"
process =  subprocess.Popen(commande.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
listeProcess = output.split("\n".encode())
for i in range(len(listeProcess)):
	listeProcess[i] = b" ".join(listeProcess[i].split())
	listeProcess[i] = listeProcess[i].split(" ".encode())
listeProcess.pop(0)
listeProcess.pop(len(listeProcess)-1)
newListeProcess = []
for i in range(len(listeProcess)):
	sousListe = []
	sousListe.append(listeProcess[i][0])
	sousListe.append(listeProcess[i][2])
	newListeProcess.append(sousListe)
# on passe la liste en dictionnaire avec les valeurs additionnees :))))
dicoUsage = {}
for i in range(len(newListeProcess)):
	user = newListeProcess[i][0].decode()
	if user in dicoUsage:
		dicoUsage[user] += float(newListeProcess[i][1])
	else:
		dicoUsage[user] = float(newListeProcess[i][1])
fic = open("result.txt", "a")
fic.write(str(dicoUsage) + '\n')
fic.close()
