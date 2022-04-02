OIFS="$IFS"
IFS=$'\n'

lesUsers=`users`
laListe=`ps -ux | sed 's/  */ /g' | cut -d" " -f1,5`
printf "{" >> sondes/result.txt
for user in $lesUsers; do
	quantiteUser=0
	for line in $laListe; do
		userLine=`echo $line | cut -d" " -f1`
		if [ "$user" = "$userLine" ]; then
			quantiteLine=`echo $line | cut -d" " -f2`
			quantiteUser=$(($quantiteUser+$quantiteLine))
		fi
	done
	printf "'$user': $quantiteUser," >> sondes/result.txt
done
`truncate -s-2 sondes/result.txt`
echo "}" >> sondes/result.txt

IFS="$OIFS"
