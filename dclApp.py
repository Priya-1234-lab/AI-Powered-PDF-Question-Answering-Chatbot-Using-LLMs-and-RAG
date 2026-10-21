import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import WebBaseLoader

load_dotenv()

st.set_page_config(
    page_title="PDF AI Assistant",
    layout="wide"
)


# ---------------- Sidebar ----------------

with st.sidebar:
    st.image("https://static.vecteezy.com/system/resources/previews/012/697/295/non_2x/3d-python-programming-language-logo-free-png.png", width=100)
    st.title("PDF AI Assistant")

    model = st.selectbox(
        "Choose Any Model",
        [
            # "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "openai/gpt-oss-20b"
        ]
    )

    if st.button("+ New Chat"):
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are an AI Assistant."
            }
        ]

# ---------------- Load PDF Only Once ----------------

if "retriever" not in st.session_state:

    loader = PyPDFLoader("data/pythonHandbook.pdf")
    documents = loader.load()

    txt_loader = TextLoader("data/java.txt", encoding="utf-8")
    documents.extend(txt_loader.load())

    docx_loader = Docx2txtLoader("data/js.docx")
    documents.extend(docx_loader.load())


    web_loader = WebBaseLoader("https://dheecodinglab.com/")
    web_documents = web_loader.load()

    print(f"Loaded {len(documents)} documents") 

     
    chunks = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )

    chunkedData = chunks.split_documents(documents)


    web_chunks = chunks.split_documents(web_documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_db = FAISS.from_documents(chunkedData, embeddings)

    web_vector_db = FAISS.from_documents(web_chunks, embeddings)

    st.session_state.retriever = vector_db.as_retriever(
        search_kwargs={"k": 3}
    )

    st.session_state.web_retriever = web_vector_db.as_retriever(
    search_kwargs={"k": 3}
    )

# ---------------- LLM ----------------

llm = ChatGroq(
    model_name=model,
    api_key=os.getenv("GAGAN_API_KEY")
)

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an AI assistant.

Answer only from the document with the provided context.

If the answer is not available in the document,
say:

"sorry I couldnt find the content what you are looking for in the document."

Context:
{context}

Question:
{question}

Answer:
"""
)

# ---------------- Messages ----------------

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": "You are an AI Assistant."
        }
    ]

# ---------------- Display Chats ----------------

for message in st.session_state.messages:

    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])

    elif message["role"] == "assistant":
        with st.chat_message("assistant"):
            st.write(message["content"])

# ---------------- Chat Input ----------------

question = st.chat_input("Ask anything from the PDF")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        response_placeholder = st.empty()

        retriever = st.session_state.retriever

        docs = retriever.invoke(question)


        web_retriever = st.session_state.web_retriever
        web_docs = web_retriever.invoke(question)

        all_docs = docs + web_docs

        context = "\n\n".join(
            [doc.page_content for doc in all_docs]
        )

        final_prompt = prompt_template.format(
            context=context,
            question=question
        )

        response = llm.invoke(final_prompt)

        answer = response.content

        response_placeholder.write(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )