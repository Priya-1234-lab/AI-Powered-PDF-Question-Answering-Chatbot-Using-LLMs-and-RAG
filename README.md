# 🤖 AI-Powered PDF Question Answering Chatbot Using LLMs and RAG

An AI-powered PDF Question Answering Chatbot built using Python, Streamlit, LangChain, Large Language Models (LLMs), Hugging Face Embeddings, and FAISS. The application allows users to ask questions about documents and receive relevant, context-aware answers.

## 📌 Project Overview

Reading and searching through lengthy documents can be time-consuming. This project simplifies document analysis by allowing users to interact with their documents through a conversational AI interface.

The application processes document content, converts text into embeddings, retrieves relevant information using vector similarity search, and uses a Large Language Model (LLM) to generate answers based on the retrieved context.

## ✨ Features

- 📄 **Document-Based Question Answering:** Ask questions about document content.
- 🧠 **LLM Integration:** Generate context-aware answers using a supported language model.
- 🔍 **Semantic Search:** Retrieve relevant document content using embeddings and FAISS.
- 📚 **Document Processing:** Extract and split text into manageable chunks.
- 💬 **Interactive Interface:** User-friendly chatbot interface built with Streamlit.
- 🐍 **Python Backend:** Document processing and AI integration using Python.
- 📂 **Multiple Document Formats:** Supports the formats configured in the application.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Frontend / User Interface:** Streamlit
- **LLM Framework:** LangChain
- **Language Models:** Supported LLM providers configured in the application
- **Embeddings:** Hugging Face Embeddings
- **Vector Database:** FAISS
- **Document Processing:** LangChain document loaders and text splitters
- **Environment Configuration:** Python dotenv
- **Version Control:** Git and GitHub

## ⚙️ System Requirements

- Python 3.10 or a compatible version supported by the project dependencies
- Git
- Visual Studio Code or another Python IDE
- A valid API key for the configured LLM provider

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gagannaik-n/RAG.git
```

### 2. Navigate to the Project Folder

```bash
cd RAG
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a `.env` file in the project root directory, alongside `dclApp.py`.

Add the API key variable expected by your application. For example, if the application uses Groq:

```env
GROQ_API_KEY=your_actual_api_key
```

Replace the placeholder with your own API key. If your application uses a different provider or variable name, configure it accordingly.

**Security:** Never commit your `.env` file or expose API keys in your source code.

### 7. Run the Application

```bash
python -m streamlit run dclApp.py
```

### 8. Open the Application

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🔄 How It Works

1. **Document Input:** The application accesses or loads the supported documents.
2. **Text Extraction:** Document content is extracted for processing.
3. **Text Chunking:** Large text is split into smaller chunks.
4. **Embedding Generation:** Embeddings represent document chunks as numerical vectors.
5. **Vector Indexing:** FAISS indexes the vectors for similarity search.
6. **Question Processing:** The user submits a question through the Streamlit interface.
7. **Context Retrieval:** Relevant document chunks are retrieved based on the question.
8. **Answer Generation:** The configured LLM uses the retrieved context to generate a response.
9. **Display:** The answer is presented in the chatbot interface.

## 📁 Project Structure

```text
RAG/
├── data/
│   ├── java.txt
│   ├── js.docx
│   └── pythonHandbook.pdf
├── dclApp.py
├── requirements.txt
├── .gitignore
├── .env                 # Create locally; not committed
└── README.md
```

The `.venv/` directory is created locally during setup and should not be uploaded to GitHub.

## 🎯 Learning Outcomes

- Understanding Large Language Models and Retrieval-Augmented Generation (RAG).
- Integrating LLMs into Python applications.
- Processing and splitting document text.
- Generating and searching vector embeddings.
- Using FAISS for semantic retrieval.
- Building interactive AI applications with Streamlit.
- Managing dependencies and API keys securely.

## 🔮 Future Enhancements

- Support for additional document formats.
- Conversation history and multi-turn chat.
- Improved source references for generated answers.
- User authentication and document management.
- Deployment as a web application.
- Enhanced error handling and document upload controls.

## 👨‍💻 Author

**Gagan Gopal Naik**

GitHub: [@gagannaik-n](https://github.com/gagannaik-n)

Project Repository: [AI-Powered PDF Question Answering Chatbot](https://github.com/gagannaik-n/RAG)

## 📄 License

This project is intended for educational and portfolio purposes. Add a suitable open-source license if you decide to distribute it publicly.
