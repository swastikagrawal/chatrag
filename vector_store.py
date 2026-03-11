import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL, TOP_K_CHUNKS, SIMILARITY_THRESHOLD


index = None
chunks = []
sources = []
model = None


def load_model():
    global model
    if model is None:
        print("System: Loading embedding model, please wait...")
        model = SentenceTransformer(EMBEDDING_MODEL)


def build_index(new_chunks, new_sources=None):
    global index, chunks, sources

    load_model()

    chunks = new_chunks

    if new_sources is None:
        sources = []
    else:
        sources = new_sources

    embeddings = model.encode(chunks)
    embeddings = np.array(embeddings).astype("float32")

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)


def search(query):
    load_model()

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, TOP_K_CHUNKS)

    results = []
    i = 0
    while i < len(indices[0]):
        idx = indices[0][i]
        distance = distances[0][i]

        if idx == -1:
            i += 1
            continue

        if distance > SIMILARITY_THRESHOLD:
            i += 1
            continue

        result = {}
        result["chunk"] = chunks[idx]

        if len(sources) > 0:
            result["source"] = sources[idx]

        results.append(result)
        i += 1

    return results