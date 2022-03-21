OIFS="$IFS"
IFS=$'\n'

`touch ../result.txt`

lesUsers=`less /etc/passwd | cut -d":" -f1`
laListe=`ps -aux | sed 's/  */ /g' | cut -d" " -f1,5`
printf '\n' >> ../result.txt
printf "{" >> ../result.txt
for user in $lesUsers; do
	quantiteUser=0
	for line in $laListe; do
		userLine=`echo $line | cut -d" " -f1`
		if [ "$user" = "$userLine" ]; then
			quantiteLine=`echo $line | cut -d" " -f2`
			quantiteUser=$(($quantiteUser+$quantiteLine))
		fi
	done
	if [ $quantiteUser != 0 ]; then
		printf "'$user': $quantiteUser," >> ../result.txt
	fi
done
`truncate -s-2 ../result.txt`
echo "}" >> ../result.txt

IFS="$OIFS"
