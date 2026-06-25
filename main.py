from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from graph import run_agent
import uvicorn

app = FastAPI(
    title="Financial Research Agent",
    description="Multi-Agent AI system for financial research",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query: str
    answer: str

@app.get("/")
def root():
    return {"status": "running", "message": "Financial Research Agent API is live!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/research", response_model=QueryResponse)
def research(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    try:
        answer = run_agent(request.query)
        return QueryResponse(query=request.query, answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)