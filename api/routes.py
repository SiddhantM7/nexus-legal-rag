from fastapi import APIRouter
from pydantic import BaseModel
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.query_handler import search_legal_context
from llm.generator import generate_answer

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str
    sources: list

@router.post("/api/query", response_model=QueryResponse)
def handle_user_query(request: QueryRequest):
    chunks = search_legal_context(request.query, top_k=5)
    answer, sources = generate_answer(request.query, chunks)
    return QueryResponse(answer=answer, sources=sources)
