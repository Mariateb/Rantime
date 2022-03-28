FILE=database/saved.db
if [ -f "$FILE" ]; then
	`cp database/saved.db database/logs.db`
fi
