import faiss
import json
import os
import numpy as np

from embedding.embedder import (
    get_embedding,
    get_embeddings
)

INDEX_FILE = "data/faiss_index.bin"

METADATA_FILE = "data/faiss_metadata.json"


class VectorDB:

    def __init__(self, dimension=384):

        self.dimension = dimension

        # Cosine similarity index
        if os.path.exists(INDEX_FILE):

            print(f"Loading FAISS index from {INDEX_FILE}")

            self.index = faiss.read_index(INDEX_FILE)

        else:

            print("Creating new FAISS cosine similarity index")

            self.index = faiss.IndexFlatIP(
                self.dimension
            )

        # Load metadata
        if os.path.exists(METADATA_FILE):

            print(f"Loading metadata from {METADATA_FILE}")

            with open(
                METADATA_FILE,
                'r',
                encoding='utf-8'
            ) as f:

                self.metadata = json.load(f)

        else:

            self.metadata = {}

    def add_chunks(self, chunks):

        """
        Add chunk embeddings into FAISS.
        """

        if not chunks:
            return 0

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        # -----------------------------
        # Batch embedding generation
        # -----------------------------

        all_embeddings = []

        BATCH_SIZE = 16

        for i in range(
            0,
            len(texts),
            BATCH_SIZE
        ):

            batch = texts[
                i:i + BATCH_SIZE
            ]

            print(
                f"Embedding batch "
                f"{i} to {i + len(batch)}"
            )

            batch_embeddings = get_embeddings(
                batch
            )

            all_embeddings.extend(
                batch_embeddings
            )

        embeddings = np.array(
            all_embeddings,
            dtype=np.float32
        )

        # Normalize for cosine similarity
        faiss.normalize_L2(embeddings)

        # Add to FAISS
        start_id = self.index.ntotal

        self.index.add(embeddings)

        # Store metadata
        for i, chunk in enumerate(chunks):

            self.metadata[
                str(start_id + i)
            ] = chunk

        print(
            f"Added {len(chunks)} chunks."
        )

        return len(chunks)

    def search(self, query: str, k=3):

        """
        Search similar chunks.
        """

        if self.index.ntotal == 0:
            return []

        # Query embedding
        query_vector = get_embedding(query)

        query_vector = np.array(
            [query_vector],
            dtype=np.float32
        )

        # Normalize query vector
        faiss.normalize_L2(query_vector)

        # Search
        scores, indices = self.index.search(
            query_vector,
            k
        )

        results = []

        print(
            "\n========== RETRIEVED RESULTS ==========\n"
        )

        for i, idx in enumerate(indices[0]):

            if idx == -1:
                continue

            # Filter weak matches
            if scores[0][i] < 0.45:
                continue

            meta = self.metadata[str(idx)]

            print(f"Rank {i+1}")

            print(
                f"Score: {scores[0][i]}"
            )

            print(
                f"Section: "
                f"{meta['section_number']}"
            )

            print(meta["text"][:400])

            print(
                "\n----------------------------------\n"
            )

            results.append({

                "score": float(scores[0][i]),

                "chunk": meta
            })

        return results

    def save(self):

        faiss.write_index(
            self.index,
            INDEX_FILE
        )

        with open(
            METADATA_FILE,
            'w',
            encoding='utf-8'
        ) as f:

            json.dump(
                self.metadata,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"Saved {self.index.ntotal} vectors."
        )


# Singleton instance
db_instance = VectorDB()