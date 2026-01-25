import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from database.db_writer import insert_report

emails = [
    "From: diana@company.com To: bob@enterprise.org Regarding Project Atlas",
    "From: george@company.com To: alice@enterprise.org Working on Cloud Migration",
    "From: fiona@company.com To: diana@enterprise.org AI Knowledge Graph update",
    "From: harry@company.com To: george@enterprise.org Client Delta discussion",
    "From: alice@company.com To: bob@enterprise.org Orion project review",
    "From: charles@company.com To: edward@enterprise.org Cloud Migration plan",
    "From: bob@company.com To: diana@enterprise.org AI Knowledge Graph progress",
    "From: george@company.com To: fiona@enterprise.org Atlas sprint update",
    "From: edward@company.com To: harry@enterprise.org Client Delta follow-up",
    "From: alice@company.com To: charles@enterprise.org Orion milestones",
    "From: fiona@company.com To: bob@enterprise.org AI pipeline design",
    "From: harry@company.com To: alice@enterprise.org Cloud Migration status",
    "From: diana@company.com To: george@enterprise.org Atlas delivery timeline",
    "From: charles@company.com To: bob@enterprise.org Project Orion sync",
    "From: edward@company.com To: diana@enterprise.org AI Knowledge Graph notes"
]

print(f"Processing {len(emails)} emails...\n")

# ---- Groq-like extraction ----
def extract_with_groq(email):
    if "Atlas" in email:
        return {"type": "WORKS_ON", "source": "person:diana", "target": "project:atlas"}
    if "Orion" in email:
        return {"type": "WORKS_ON", "source": "person:alice", "target": "project:orion"}
    if "Cloud" in email:
        return {"type": "WORKS_ON", "source": "person:george", "target": "project:cloud_migration"}
    if "AI" in email:
        return {"type": "WORKS_ON", "source": "person:fiona", "target": "technology:ai_knowledge_graph"}
    if "Delta" in email:
        return {"type": "RELATED_TO", "source": "person:harry", "target": "client:delta"}
    return None


# ---- Run pipeline + store in DB ----
for i, email in enumerate(emails, start=1):
    print(f"\n--- Email {i} ---")
    print(email)

    extracted = extract_with_groq(email)

    if not extracted:
        print("No relevant entities found.")
        continue

    print("Extracted JSON:", extracted)

    # map extracted data → DB schema
    report = {
        "report_id": f"E{i}",
        "issue_type": extracted["type"],
        "product": extracted["target"].split(":")[1],
        "customer_name": extracted["source"].split(":")[1],
        "root_cause": "Derived from email",
        "resolution_action": "Pending"
    }

    insert_report(report)
    print("Inserted into SQLite DB")
