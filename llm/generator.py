import requests
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

OLLAMA_URL = "http://localhost:11434/api/generate"


def format_context(retrieved_chunks):

    """
    Build clean legal context.
    """

    context_parts = []

    sources = []

    for idx, res in enumerate(retrieved_chunks):

        chunk = res["chunk"]

        law = chunk.get(
            "law_type",
            "Unknown Law"
        )

        sec = chunk.get(
            "section_number",
            "Unknown Section"
        )

        doc = chunk.get(
            "document_name",
            "Unknown File"
        )

        text = chunk.get(
            "text",
            ""
        )

        source_id = (
            f"[{law}] {sec} "
            f"(from {doc})"
        )

        sources.append(source_id)

        cleaned_text = text[:2500]

        context_parts.append(
            f"""
SOURCE {idx+1}

Law: {law}

Section: {sec}

Document: {doc}

Legal Text:
{cleaned_text}
"""
        )

    return "\n\n".join(context_parts), sources


def has_exact_match(retrieved_chunks):

    """
    Exact metadata match detection.
    """

    if not retrieved_chunks:
        return False

    return retrieved_chunks[0]["score"] >= 999


def render_direct(retrieved_chunks):

    """
    Direct exact legal text rendering.
    No LLM = zero hallucination.
    """

    parts = []

    for res in retrieved_chunks:

        if res["score"] < 999:
            continue

        c = res["chunk"]

        law = c.get(
            "law_type",
            "Unknown"
        )

        sec = c.get(
            "section_number",
            "Unknown"
        )

        doc = c.get(
            "document_name",
            "Unknown"
        )

        text = c.get(
            "text",
            ""
        ).strip()

        parts.append(
            f"""
## {sec}

**Law:** {law}

**Source:** {doc}

{text}
"""
        )

    return "\n\n---\n\n".join(parts)


def build_prompt(query, context_text):

    return f"""
You are an Indian Legal AI Assistant.

STRICT RULES:

1. Answer ONLY using the provided legal context.
2. NEVER invent laws, punishments, sections, or articles.
3. If answer is missing, say:
   "I could not find the exact legal provision in the ingested documents."
4. Keep answers SHORT, CLEAR, and FACTUAL.
5. Do NOT repeat the same information.
6. Respond in proper markdown format.
7. Respond in English only.

FORMAT:

## Legal Provision
- Mention Act / Section

## Punishment
- Mention imprisonment
- Mention fine

## Short Explanation
- One concise explanation only

LEGAL CONTEXT:
{context_text}

QUESTION:
{query}

LEGAL ANSWER:
"""

def generate_answer(query: str, retrieved_chunks: list):

    """
    Main answer generation.
    """

    if not retrieved_chunks:

        return (
            "I could not find relevant legal sections in the database.",
            []
        )

    # EXACT MATCH
    if has_exact_match(retrieved_chunks):

        direct_answer = render_direct(
            retrieved_chunks
        )

        if direct_answer.strip():

            return (
                direct_answer,
                []
            )

    # Build context
    context_text, sources = format_context(
        retrieved_chunks
    )

    prompt = build_prompt(
        query,
        context_text
    )

    payload = {

        "model": "mistral",

        "prompt": prompt,

        "stream": False,

        "options": {

            "temperature": 0.02,

            "top_p": 0.3,

            "repeat_penalty": 1.5
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        result = response.json().get(
            "response",
            "No response generated."
        )

        return result.strip(), sources

    except Exception as e:

        return (
            f"Error connecting to Ollama: {e}",
            []
        )