# from requirement.parser import RequirementParser


# parser = RequirementParser()

# query = input("\nEnter your requirement: ").strip()

# result = parser.parse(query)

# print("\n" + "=" * 70)
# print("PARSED REQUIREMENT")
# print("=" * 70)

# for key, value in result.items():
#     print(f"{key}: {value}")

from requirement.parser import RequirementParser


parser = RequirementParser()

test_queries = [
    "I need a Hindi model for automatic speech recognition",
    "I need a low cost English chatbot with 8GB GPU memory",
    "I need an open source multilingual embedding model",
    "I need a lightweight quantized language model with low latency"
]

for query in test_queries:

    print("\n" + "=" * 70)
    print("QUERY:")
    print(query)

    print("\nPARSED REQUIREMENT:")

    result = parser.parse(query)

    for key, value in result.items():
        print(f"{key}: {value}")