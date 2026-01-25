import sqlite3

conn = sqlite3.connect("database/reports.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM reports")
conn.commit()
conn.close()

print("Old data cleared from reports table")
