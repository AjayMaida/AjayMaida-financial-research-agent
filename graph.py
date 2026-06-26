from langgraph.graph import StateGraph, END
from agents.planner import planner_agent
from agents.retriever import retriever_agent
from agents.analyst import analyst_agent
from agents.responder import responder_agent
from typing import TypedDict

# Define the state schema
class AgentState(TypedDict):
    query: str
    plan: dict
    retrieved: dict
    analysis: str
    final_answer: str

# Build the graph
def build_graph():
    workflow = StateGraph(AgentState)

    # Add nodes
    workflow.add_node("planner", planner_agent)
    workflow.add_node("retriever", retriever_agent)
    workflow.add_node("analyst", analyst_agent)
    workflow.add_node("responder", responder_agent)

    # Add edges (sequential flow)
    workflow.set_entry_point("planner")
    workflow.add_edge("planner", "retriever")
    workflow.add_edge("retriever", "analyst")
    workflow.add_edge("analyst", "responder")
    workflow.add_edge("responder", END)

    return workflow.compile()

# Build the graph once and reuse it
graph = build_graph()

# Run the graph
def run_agent(query: str) -> str:
    initial_state = {
        "query": query,
        "plan": {},
        "retrieved": {},
        "analysis": "",
        "final_answer": ""
    }
    result = graph.invoke(initial_state)
    return result["final_answer"]


if __name__ == "__main__":
    query = "What is the current stock price and latest news about Infosys?"
    print("Running Financial Research Agent...\n")
    answer = run_agent(query)
    print("Final Answer:\n")
    print(answer)