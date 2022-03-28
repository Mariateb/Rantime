ladate=$(date +'%Y/%m/%d %H:%M:%S')
echo $ladate
echo $ladate > sondes/result.txt
python sondes/talon.py
python sondes/achil.py
bash sondes/pinky.sh
python sondes/logger.py
