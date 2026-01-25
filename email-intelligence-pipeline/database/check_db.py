import sqlite3

conn = sqlite3.connect("database/reports.db")
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM reports LIMIT 5").fetchall()

print("Showing first 5 rows from reports table:")
for row in rows:
    print(row)

conn.close()
