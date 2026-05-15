from sentence_transformers import SentenceTransformer
import numpy as np


# Strong embedding model
model_name = "BAAI/bge-small-en-v1.5"

try:

    print(f"Loading embedding model: {model_name}")

    model = SentenceTransformer(
        model_name,
        trust_remote_code=True
    )

except Exception as e:

    print(f"Failed to load model: {e}")

    model = None


def get_embedding(text: str):

    """
    Generate normalized embedding vector.
    """

    if model is None:
        raise ValueError("Embedding model not loaded.")

    embedding = model.encode(
        text,
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    return embedding.astype(np.float32)


def get_embeddings(texts: list):

    """
    Batch embeddings for faster ingestion.
    """

    if model is None:
        raise ValueError("Embedding model not loaded.")

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    return embeddings.astype(np.float32)


def reload_model(path: str):

    global model

    model = SentenceTransformer(
        path,
        trust_remote_code=True
    )