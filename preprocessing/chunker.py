import re


def clean_text(text):

    text = re.sub(r'\s+', ' ', text)

    text = re.sub(
        r'A\s*r\s*t\s*i\s*c\s*l\s*e',
        'Article',
        text,
        flags=re.IGNORECASE
    )

    text = re.sub(
        r'S\s*e\s*c\s*t\s*i\s*o\s*n',
        'Section',
        text,
        flags=re.IGNORECASE
    )

    return text.strip()


def fallback_chunking(
    text,
    get_page_func,
    doc_name,
    law_type,
    chunk_size=500
):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk_text = text[i:i + chunk_size]

        page_num = get_page_func(i)

        embedding_text = f"""
Law Type: {law_type}

Document: {doc_name}

Content:
{chunk_text}
"""

        chunks.append({

            "text": embedding_text.strip(),

            "section_number": "Unknown",

            "law_type": law_type,

            "document_name": doc_name,

            "page_number": page_num
        })

    return chunks


def split_into_sections(pages_text):

    chunks = []

    if not pages_text:
        return chunks

    doc_name = pages_text[0]["document_name"]

    law_type = pages_text[0]["law_type"]

    section_pattern = re.compile(
        r'''(?imx)

        ^\s*

        (?:
            (ARTICLE|Article|SECTION|Section)\s*
            |
            (?<=\n)
        )

        (\d+[A-Z\-]*)

        [\.\:\-\)]*

        \s*

        (.{0,120})?
        '''
    )

    full_text = ""

    page_map = []

    for page in pages_text:

        cleaned_page = clean_text(
            page["text"]
        )

        start_idx = len(full_text)

        full_text += cleaned_page + "\n"

        page_map.append(
            (
                start_idx,
                page["page_number"]
            )
        )

    def get_page(index):

        found_page = 1

        for start_idx, page_num in page_map:

            if index >= start_idx:
                found_page = page_num

        return found_page

    matches = list(
        section_pattern.finditer(full_text)
    )

    print(f"\nTOTAL MATCHES FOUND: {len(matches)}\n")

    if not matches:

        print(
            "No matches found. Using fallback chunking."
        )

        return fallback_chunking(
            full_text,
            get_page,
            doc_name,
            law_type
        )

    for i, match in enumerate(matches):

        start = match.start()

        end = (
            matches[i + 1].start()
            if i + 1 < len(matches)
            else len(full_text)
        )

        section_type = match.group(1)

        section_num = match.group(2)

        section_heading = (
            match.group(3) or ""
        ).strip()

        if not section_type:

            if "constitution" in law_type.lower():

                section_type = "Article"

            else:

                section_type = "Section"

        section_type = section_type.capitalize()

        section_title = (
            f"{section_type} {section_num}"
        )

        # FIXED ORDER
        chunk_text = full_text[start:end].strip()

        chunk_text = chunk_text[:1500]

        if len(chunk_text) < 80:
            continue

        page_num = get_page(start)

        embedding_text = f"""
Law Type: {law_type}

Document: {doc_name}

Section: {section_title}

Heading:
{section_heading}

Legal Text:
{chunk_text}
"""

        print(f"CREATED CHUNK: {section_title}")

        chunks.append({

            "text": embedding_text.strip(),

            "section_number": section_title,

            "law_type": law_type,

            "document_name": doc_name,

            "page_number": page_num
        })

    print(f"\nTOTAL CHUNKS CREATED: {len(chunks)}\n")

    return chunks