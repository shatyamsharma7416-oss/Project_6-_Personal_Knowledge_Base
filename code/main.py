import argparse

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest="command")

ingest_parser = subparser.add_parser("ingest")
ingest_parser.add_argument("--docs", required=True)

query_parser = subparser.add_parser("query")
query_parser.add_argument("question")   # position argument

args = parser.parse_args()


def store(path_addr: str):
    from doc_extractor import extracted_content
    from chunker import recursive_split
    from store_embedding import store_chuks

    contents = extracted_content(path_addr)
    for i,key in enumerate(contents.keys()):
        text = contents[key]
        chunked_text = recursive_split(text)
        total_chunks += store_chuks(chunked_text)
    
    print(f"Ingested {total_chunks+1} chunks from {i+1} documents")

def retrieve(query: str):
    from chunk_retriever import relevent_chunks

    retrieved_chunks = ""
    chunks = relevent_chunks(query, top_k=1)
    for chunk in chunks:
        retrieved_chunks += chunk
    
    return retrieved_chunks

    

if args.command == "ingest":
    store(args.docs)
elif args.command == "query":
    retrieve(args.question)

