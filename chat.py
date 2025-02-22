from praisonaiagents import Agent

# RAG configuration (remains the same)
config = {
    "vector_store": {
        "provider": "chroma",
        "config": {
            "collection_name": "praison",
            "path": ".praison"  # Uses the existing stored embeddings
        }
    },
    "llm": {
        "provider": "ollama",
        "config": {
            "model": "deepseek-r1:latest",
            "temperature": 0,
            "max_tokens": 8000,
            "ollama_base_url": "http://localhost:11434",
        },
    }
}

# Initialize the agent without re-indexing
agent = Agent(
    name="Knowledge Agent",
    instructions="You answer questions based on the stored knowledge.",
    knowledge=[],  # No need to re-index, we just query the stored embeddings
    knowledge_config=config,
    user_id="user1",
    llm="deepseek-r1"
)

# Start chat with the stored embeddings
while True:
    user_query = input("Ask a question (type 'exit' to stop): ")
    if user_query.lower() == "exit":
        print("Chat ended.")
        break
    response = agent.start(user_query)
    print("\nAgent:", response)
