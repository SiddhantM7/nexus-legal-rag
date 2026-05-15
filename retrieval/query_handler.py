import sys
import os
import re

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from vector_db.faiss_db import db_instance


SPECIFIC_REF_PATTERN = re.compile(
    r'\b(article|section)\s+(\d+[A-Za-z\-]*)\b',
    re.IGNORECASE
)


# DIRECT LEGAL SECTION MAP
# MOST IMPORTANT FIX

LEGAL_SECTION_MAP = {

    "theft": [
        "Section 378",
        "Section 379"
    ],

    "murder": [
        "Section 302"
    ],

    "cheating": [
        "Section 420"
    ],

    "rape": [
        "Section 376"
    ],

    "kidnapping": [
        "Section 363"
    ]
}


def get_direct_legal_matches(query):

    query_lower = query.lower()

    direct_results = []

    for keyword, target_sections in LEGAL_SECTION_MAP.items():

        if keyword in query_lower:

            for target in target_sections:

                target = target.lower()

                for key, chunk in db_instance.metadata.items():

                    stored = chunk.get(
                        "section_number",
                        ""
                    ).lower().strip()

                    if stored == target:

                        direct_results.append({

                            "score": 1000.0,

                            "chunk": chunk
                        })

    return direct_results


def find_exact_chunks(query):

    matches = SPECIFIC_REF_PATTERN.findall(query)

    if not matches:
        return []

    exact_results = []

    for ref_type, ref_num in matches:

        target = f"{ref_type.capitalize()} {ref_num}"

        target = target.lower().strip()

        for key, chunk in db_instance.metadata.items():

            stored = chunk.get(
                "section_number",
                ""
            ).lower().strip()

            if stored == target:

                exact_results.append({

                    "score": 999.0,

                    "chunk": chunk
                })

    return exact_results


def normalize_query(query):

    query = query.strip()

    article_match = re.search(
        r'article\s+(\d+)',
        query,
        re.IGNORECASE
    )

    if article_match:

        num = article_match.group(1)

        query += f"""
        Constitution of India
        Fundamental Rights
        Article {num}
        """

    section_match = re.search(
        r'section\s+(\d+)',
        query,
        re.IGNORECASE
    )

    if section_match:

        num = section_match.group(1)

        query += f"""
        Indian Penal Code
        Bharatiya Nyaya Sanhita
        Criminal Law
        Section {num}
        """

    return query


def search_legal_context(query, top_k=2):

    seen = set()

    merged = []

    def add(results):

        for r in results:

            key = (
                r["chunk"]["section_number"]
                +
                r["chunk"]["text"][:100]
            )

            if key not in seen:

                seen.add(key)

                merged.append(r)

    # STEP 1:
    # DIRECT LEGAL MAPPING
    direct_results = get_direct_legal_matches(query)

    add(direct_results)

    # STEP 2:
    # EXACT ARTICLE/SECTION MATCH
    exact_results = find_exact_chunks(query)

    add(exact_results)

    # STEP 3:
    # SEMANTIC SEARCH ONLY IF NEEDED
    if len(merged) < top_k:

        normalized_query = normalize_query(query)

        semantic_results = db_instance.search(
            normalized_query,
            k=top_k
        )

        add(semantic_results)

    # Highest score first
    merged.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print(
        "\n=========== FINAL RESULTS ===========\n"
    )

    for i, r in enumerate(merged):

        print(f"FINAL RANK {i+1}")

        print(
            f"Score: {r['score']}"
        )

        print(
            r["chunk"]["section_number"]
        )

        print(
            r["chunk"]["text"][:300]
        )

        print(
            "\n==============================\n"
        )

    return merged[:top_k]