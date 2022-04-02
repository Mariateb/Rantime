#!/bin/bash

python RantimeGraphUpdate.py

echo "Liste des sondes :"
for filename in sondes/sonde*; do
	echo "$filename"
done
for filename in graphs/images/*; do
	if [ -d "$filename" ]; then
		echo "Données pour l'utilisateur $filename :"
		feh -g -d -S filename "$filename"
	fi
done
