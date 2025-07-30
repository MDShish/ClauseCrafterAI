# main.py
import streamlit as st
from query_parser import parse_query
from doc_parser import parse_document
from retriever import ClauseRetriever
from decision_engine import evaluate_claim
from utils import log_event

st.set_page_config(page_title="ClauseCrafterAI", layout="wide")
st.title("📄 ClauseCrafter AI")

uploaded_file = st.file_uploader("Upload policy PDF/DOCX/text file", type=["pdf", "docx", "txt"])
query = st.text_input("Enter insurance claim query")

if uploaded_file and query:
    log_event("UPLOAD", uploaded_file.name)
    with st.spinner("Parsing document..."):
        chunks = parse_document(uploaded_file)

    with st.spinner("Indexing clauses..."):
        retriever = ClauseRetriever()
        retriever.index_clauses(chunks)

    with st.spinner("Parsing query..."):
        parsed = parse_query(query)

    with st.spinner("Retrieving relevant clauses..."):
        matches = retriever.retrieve(query)
        retrieved_clauses = "\n".join([m[0] for m in matches])

    with st.spinner("Evaluating claim..."):
        decision = evaluate_claim(parsed, retrieved_clauses)

    st.subheader("🔍 Parsed Query")
    st.code(parsed, language="json")

    st.subheader("📜 Retrieved Clauses")
    st.code(retrieved_clauses)

    st.subheader("✅ Decision Output")
    st.code(decision, language="json")