from langchain_pinecone import PineconeVectorStore
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

# force correct key (temporary)
os.environ["PINECONE_API_KEY"] = "pcsk_6xPe5H_22UE2M7NhmFM7Qvbyw648Ewsa1ABfX5g9qxd2ZTU4cipqdWUscBYrxqNGL8xZtV"
# same embedding model you used during ingestion
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = PineconeVectorStore(
    index_name="infosys-emails",
    embedding=embeddings
)

query = input("Ask something: ").lower()

# detect filters
filter_dict = {}

people = ["diana", "alice", "bob", "george", "fiona", "harry", "charles", "edward"]
projects = ["atlas", "orion", "cloud"]

for p in people:
    if p in query:
        filter_dict["sender"] = p

for pr in projects:
    if pr in query:
        filter_dict["project"] = pr

print("\n⚠ DEBUG MODE → FILTER DISABLED")

results = vectorstore.similarity_search(
    query,
    k=3
)

print("\nResults:\n")

if not results:
    print("No results at all in index.")
else:
    for r in results:
        print("FULL METADATA:", r.metadata)
        print()
        print(r.page_content)
        print("\n" + "="*60 + "\n")



