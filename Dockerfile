FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . .

# Install uv
RUN pip install uv

# Install dependencies
RUN uv pip install --system langchain langgraph langchain-groq langchain-community \
    chromadb fastapi uvicorn streamlit python-dotenv requests yfinance langsmith pydantic

# Expose ports
EXPOSE 8000 8501

# Create data directory for ChromaDB
RUN mkdir -p /app/data/chroma_db

# Default command runs FastAPI
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

CMD ["streamlit", "run", "streamlit_app.py", "--server.port",  "8501", "--server.address", "0.0.0.0"]