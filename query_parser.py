# query_parser.py
from transformers import pipeline

llm = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", device_map="auto")

PROMPT_TEMPLATE = """
Extract the following information from the insurance query:
- Age
- Gender
- Treatment/Procedure
- Location
- Policy Duration (in months)

Query: "{query}"

Output as JSON:
"""

def parse_query(query):
    prompt = PROMPT_TEMPLATE.format(query=query)
    response = llm(prompt, max_new_tokens=300, do_sample=True)[0]["generated_text"]
    return response