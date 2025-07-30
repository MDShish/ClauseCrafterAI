# decision_engine.py
from transformers import pipeline

llm = pipeline("text-generation", model="tiiuae/falcon-7b-instruct", device_map="auto")

DECISION_PROMPT_TEMPLATE = """
Given the following structured query and retrieved clauses, determine whether the claim should be approved or rejected. Also estimate the payout amount if applicable and explain the reasoning with specific clause references.

Structured Query:
{query_data}

Retrieved Clauses:
{clauses}

Output JSON format:
{{
  "decision": "Approved/Rejected",
  "amount": "Amount or null",
  "justification": "Explanation with clause reference",
  "references": ["Clause snippet or titles"]
}}
"""

def evaluate_claim(query_data, clauses):
    filled_prompt = DECISION_PROMPT_TEMPLATE.format(query_data=query_data, clauses=clauses)
    response = llm(filled_prompt, max_new_tokens=500, do_sample=True)[0]["generated_text"]
    return response
