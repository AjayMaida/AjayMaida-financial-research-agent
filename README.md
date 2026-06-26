# 📈 Financial Research Agent

This project implements a multi-agent AI system for conducting financial research. It uses a combination of Streamlit for the user interface, FastAPI for the backend API, and LangGraph to orchestrate a team of specialized AI agents.

The system is designed to take a user's query about a stock or company, break it down into a research plan, gather information, analyze it, and generate a comprehensive, human-readable answer.

## ✨ Features

- **Multi-Agent System:** Utilizes a graph of AI agents, each with a specific role (Planner, Retriever, Analyst, Responder).
- **Web Interface:** A clean and simple UI built with Streamlit.
- **Scalable Backend:** A robust API powered by FastAPI.
- **Intelligent Workflow:** Uses LangGraph to define and execute the research process in a structured and repeatable way.

---

## ⚙️ How It Works: The Application Flow

The application is composed of three main parts: a Streamlit frontend, a FastAPI backend, and a LangGraph-powered agentic workflow.

1.  **Frontend (Streamlit):** The user enters a financial query (e.g., "What is the latest news about Infosys?") into the web UI. The frontend sends this query to the backend API.

2.  **Backend (FastAPI):** The API server receives the query and triggers the LangGraph research agent.

3.  **Agent Workflow (LangGraph):** This is the core of the application. The query is processed through a sequence of specialized agents:

    -   **`planner_agent` (The Manager):**
        -   **Input:** The raw user query.
        -   **Task:** Analyzes the query and creates a structured research plan.
        -   **Output:** A dictionary of tasks, like `{"tasks": ["find stock price for 'INFY'", "search for recent news"]}`.

    -   **`retriever_agent` (The Data Gatherer):**
        -   **Input:** The research plan.
        -   **Task:** Executes the plan by using tools (e.g., web search) to fetch the required raw data (stock prices, news articles, etc.).
        -   **Output:** A collection of retrieved, unstructured data.

    -   **`analyst_agent` (The Thinker):**
        -   **Input:** The raw data from the retriever.
        -   **Task:** Synthesizes the information, identifies key insights, and connects the dots (e.g., correlates news with stock movements).
        -   **Output:** A structured summary of the analysis.

    -   **`responder_agent` (The Communicator):**
        -   **Input:** The structured analysis.
        -   **Task:** Formats the analysis into a polished, well-written, and easy-to-understand final answer for the user.
        -   **Output:** The final string of text that the user will see.

This final answer is then sent back through the API to the Streamlit frontend and displayed to the user.

---

## 🚀 Running the Project

1.  **Start the Backend:**
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
2.  **Run the Frontend:**
    ```bash
    streamlit run streamlit_app.py
    ```