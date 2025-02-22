from praisonaiagents import Agent


# RAG configuration
config = {
    "vector_store":{
        "provider": "chroma",
        "config":{
            "collection_name": "praison",
            "path": ".praison"
        }
    },
    "llm":{
        "provider": "ollama",
        "config":{
            "model": "deepseek-r1:latest",
            "temperature": 0,
            "max_tokens": 500,
            "ollama_base_url": "http://localhost:11434",
        },
    },
    "embedder":{
        "provider": "ollama",
        "config":{
            "model": "nomic-embed-text:latest",
            "ollama_base_url": "http://localhost:11434",
            "embedding_dims": 1536 
        }
    }
}



agent = Agent(
    name = "Knowledge Agent",
    instructions="You answer question based on the provided knowledge.",
    knowledge=["kag-research-paper.pdf"], #indexing
    knowledge_config=config,
    user_id="user1",
    llm="deepseek-r1"
)


# agent = Agent(
#     name="Knowledge Agent",
#     instructions="You answer questions based on the provided knowledge.",
#     knowledge=["kag-research-paper.pdf"],  # Indexing
#     knowledge_config=config,
#     user_id="user1",
#     llm={
#         "provider": "ollama",  # Explicitly define Ollama
#         "config": {
#             "model": "deepseek-r1",
#             "ollama_base_url": "http://localhost:11434",
#             "temperature": 0
#         }
#     }
# )




agent.start("What is KAG in one line?") #Retrival