from pipeline import ask


query = "I need a Hindi model for automatic speech recognition"


result = ask(query)


print("\n" + "=" * 70)
print("QUERY")
print("=" * 70)
print(result["query"])


print("\n" + "=" * 70)
print("PARSED REQUIREMENT")
print("=" * 70)

for key, value in result["parsed_requirement"].items():
    print(f"{key}: {value}")


print("\n" + "=" * 70)
print("RETRIEVED MODELS")
print("=" * 70)

for item in result["retrieved_models"]:
    metadata = item["metadata"]

    print(f"\nModel: {metadata.get('model_name')}")
    print(f"Task: {metadata.get('task')}")
    print(f"Languages: {metadata.get('supported_languages')}")
    print(f"Score: {item.get('relevance_score')}")


print("\n" + "=" * 70)
print("FILTERED MODELS")
print("=" * 70)

if not result["filtered_models"]:
    print("No models matched all requirements.")

for item in result["filtered_models"]:
    metadata = item["metadata"]

    print(f"\nModel: {metadata.get('model_name')}")
    print(f"Task: {metadata.get('task')}")
    print(f"Languages: {metadata.get('supported_languages')}")


print("\n" + "=" * 70)
print("FINAL ANSWER")
print("=" * 70)
print(result["answer"])