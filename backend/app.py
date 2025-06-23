import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# --- Load Environment Variables ---
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- App Initialization ---
app = FastAPI(
    title="Memora AI Backend",
    description="Handles memory, embeddings, and LLM interactions for Memora AI.",
    version="1.0.0",
)

# --- Pydantic Models for API ---
class ChatRequest(BaseModel):
    highlighted_text: str
    query: str
    user_id: str = "default_user" # Placeholder for multi-user support

class ChatResponse(BaseModel):
    answer: str
    retrieved_context: list[str]
    auto_summary: str

# --- Placeholder for Core Logic ---
# In a real app, you would initialize your database, FAISS index, and LangChain components here.
# from memory.retriever import FaissRetriever
# from summarizer.agent import SummarizationAgent
# retriever = FaissRetriever("embeddings/faiss_index")
# summarizer = SummarizationAgent()

@app.on_event("startup")
async def startup_event():
    """Validate environment variables on startup."""
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY not found in .env file. Please add it.")
    print("Backend server started successfully.")
    # You could also connect to DB or load FAISS index here.
    # print("Connecting to database and loading FAISS index...")


@app.post("/api/chat", response_model=ChatResponse)
async def chat_with_memory(request: ChatRequest):
    """
    Main endpoint to handle user queries. It retrieves context, queries the LLM,
    and stores the interaction.
    """
    print(f"Received query: '{request.query}' for text: '{request.highlighted_text[:50]}...'")

    # 1. & 2. Embed and Retrieve (Placeholder)
    # similar_highlights = retriever.search(request.highlighted_text)
    similar_highlights = [
        "This is a retrieved past highlight that is semantically similar.",
        "You asked a similar question about this topic last week."
    ]

    # 3. Chat with GenAI (Placeholder)
    # You would use LangChain here to combine the query, highlighted text, and retrieved context.
    # answer = llm.invoke(f"Context: {similar_highlights}. Highlight: {request.highlighted_text}. Question: {request.query}")
    answer = f"This is a placeholder AI response to your question: '{request.query}'. I've noted you're looking at text about '{request.highlighted_text[:30]}...'."

    # 4. Auto-generated Notes (Placeholder)
    # summary = summarizer.generate_notes(conversation_history)
    summary = "• This is an auto-generated summary bullet point.\n• It would summarize the key takeaways from the conversation."

    # 5. Store Interaction (Placeholder)
    # db.store(user_id=request.user_id, highlight=request.highlighted_text, query=request.query, response=answer)
    print("Interaction would be stored in SQLite and FAISS now.")

    return ChatResponse(
        answer=answer,
        retrieved_context=similar_highlights,
        auto_summary=summary,
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)