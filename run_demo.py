from pipeline import build_index, ask

if __name__ == "__main__":
    build_index()
    query = input("\nAsk about the available models: ").strip()
    if query:
        result = ask(query, top_k=3)
        print("\nRETRIEVED MODELS")
        for item in result["retrieved_models"]:
            print(f"- {item['metadata'].get('model_name')} | relevance={item['relevance_score']}")
        print("\nGROUNDED ANSWER\n")
        print(result["answer"])
