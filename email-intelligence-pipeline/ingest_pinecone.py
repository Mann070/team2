import os
from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document

import os

# force correct key (temporary)
os.environ["PINECONE_API_KEY"] = "pcsk_6xPe5H_22UE2M7NhmFM7Qvbyw648Ewsa1ABfX5g9qxd2ZTU4cipqdWUscBYrxqNGL8xZtV"

# embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# connect to index
vectorstore = PineconeVectorStore(
    index_name="infosys-emails",
    embedding=embeddings
)

# read data file
with open("data/emails_cleaned.txt", "r", encoding="utf-8") as f:
    text = f.read()

# simple split (we improve later)
emails = text.split("From:")

import re

docs = []

for e in emails:
    if not e.strip():
        continue

    email_text = "From:" + e

    sender = re.search(r"From:\s*(\w+)@", email_text)
    receiver = re.search(r"To:\s*(\w+)@", email_text)
    project = re.search(r"Project\s+(\w+)", email_text)

    metadata = {
        "sender": sender.group(1).lower() if sender else "unknown",
        "receiver": receiver.group(1).lower() if receiver else "unknown",
        "project": project.group(1).lower() if project else "general",
    }

    docs.append(
        Document(
            page_content=email_text,
            metadata=metadata
        )
    )

print("Uploading", len(docs), "emails...")

# upload
vectorstore.add_documents(docs)

print("Ingestion complete")
