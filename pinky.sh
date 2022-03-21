OIFS="$IFS"
IFS=$'\n'

`touch pinkyResults.txt | > pinkyResults.txt`

lesUsers=`less /etc/passwd | cut -d":" -f1`
laListe=`ps -aux | sed 's/  */ /g' | cut -d" " -f1,5`
for user in $lesUsers; do
	echo $user
	quantiteUser=0
	for line in $laListe; do
		userLine=`echo $line | cut -d" " -f1`
		if [ "$user" = "$userLine" ]; then
			quantiteLine=`echo $line | cut -d" " -f2`
			quantiteUser=$(($quantiteUser+$quantiteLine))
		fi
	done
	echo "{'$user': $quantiteUser}" >> pinkyResults.txt
done
IFS="$OIFS"
