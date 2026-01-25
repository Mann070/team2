import sqlite3

def insert_report(report):
    conn = sqlite3.connect("database/reports.db")
    cursor = conn.cursor()

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
        report["report_id"],
        report["issue_type"],
        report["product"],
        report["customer_name"],
        report["root_cause"],
        report["resolution_action"]
    ))

    conn.commit()
    conn.close()
