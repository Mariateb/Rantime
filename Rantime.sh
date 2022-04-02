ladate=$(date +'%Y/%m/%d %H:%M:%S')
echo $ladate
echo $ladate > sondes/result.txt
python sondes/sondeTalon.py
python sondes/sondeAchil.py
bash sondes/sondePinky.sh
python sondes/logger.py
python urgences/detecterUrgence.py
