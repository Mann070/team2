import sqlite3
import csv

conn = sqlite3.connect("database/reports.db")
cursor = conn.cursor()

with open("data/structure_docs.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)

    print("CSV Columns:", reader.fieldnames)  # DEBUG LINE

    for row in reader:
        cursor.execute("""
        INSERT INTO reports (
            report_id,
            issue_type,
            product,
            customer_name,
            root_cause,
            resolution_action
        ) VALUES (?, ?, ?, ?, ?, ?)
        """, (
            row.get("report_id") or row.get("id") or row.get("document_id"),
            row.get("issue_type"),
            row.get("product"),
            row.get("customer_name"),
            row.get("root_cause"),
            row.get("resolution_action")
        ))

conn.commit()
conn.close()

print("Reports inserted into SQLite DB")
