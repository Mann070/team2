import sqlite3

# connect (creates DB if not exists)
conn = sqlite3.connect("database/reports.db")
cursor = conn.cursor()

# create table (schema)
cursor.execute("""
CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_id TEXT,
    issue_type TEXT,
    product TEXT,
    customer_name TEXT,
    root_cause TEXT,
    resolution_action TEXT
)
""")

conn.commit()
conn.close()

print("SQLite DB created and schema initialized")
