# AI Ollama Chroma - Mobile Phone Review Q&A System

A Retrieval-Augmented Generation (RAG) application that answers questions about mobile phones using Amazon product reviews. This project combines vector embeddings, semantic search, and local LLM inference to provide intelligent answers based on real customer reviews.

## 🎯 Features

- **Semantic Search**: Uses vector embeddings to find the most relevant reviews based on meaning, not just keywords
- **Local AI Processing**: Runs entirely on your machine using Ollama - no external API calls required
- **Persistent Vector Database**: Chroma database stores embeddings for fast retrieval
- **Interactive Q&A**: Command-line interface for asking questions about mobile phones
- **Context-Aware Answers**: Retrieves top 3 most relevant reviews to provide accurate, context-rich responses

## 🛠️ Technology Stack

- **LangChain**: Framework for building LLM applications
- **Ollama**: Local LLM for embeddings (`mxbai-embed-large`) and text generation (`llama3.2`)
- **Chroma**: Vector database for storing and searching embeddings
- **Pandas**: Data processing and CSV handling
- **Python 3.12+**: Required Python version

## 📋 Prerequisites

1. **Ollama installed and running** on your system
   - Download from: https://ollama.ai
   - Install required models:
     ```bash
     ollama pull mxbai-embed-large
     ollama pull llama3.2
     ```

2. **Python 3.12 or higher**

3. **Dataset**: `Amazon_Unlocked_Mobile.csv` file in the project root

## 🚀 Installation

1. **Clone or navigate to the project directory**

2. **Install dependencies using uv**:
   ```bash
   uv sync
   ```

   Or if you prefer pip:
   ```bash
   pip install -e .
   ```

3. **Ensure your dataset is in place**:
   - The project expects `Amazon_Unlocked_Mobile.csv` in the root directory
   - The CSV should contain columns: Product Name, Brand Name, Reviews, Price, Rating, Review Votes

## 📖 Usage

1. **Run the main application**:
   ```bash
   python main.py
   ```

2. **Ask questions about mobile phones**:
   - The system will retrieve relevant reviews and generate answers
   - Type `q` to quit

### Example Questions:
- "What's the best phone for photography?"
- "Which phone has the longest battery life?"
- "What are the most common complaints about iPhone?"
- "Recommend a budget-friendly Android phone"

## 📁 Project Structure

```
ai-ollama-chroma/
├── main.py                 # Interactive Q&A application
├── vector.py               # Vector database setup and document processing
├── Amazon_Unlocked_Mobile.csv  # Dataset (Amazon mobile phone reviews)
├── chome_langchain_db/     # Chroma vector database (created on first run)
├── pyproject.toml          # Project dependencies
└── README.md               # This file
```

## 🔧 How It Works

### 1. **Data Processing** (`vector.py`)
   - Loads Amazon mobile phone reviews from CSV
   - Processes each review into a LangChain Document with:
     - **Content**: Product name, brand, review text, and price
     - **Metadata**: Rating and review votes
   - Generates vector embeddings using Ollama's embedding model
   - Stores embeddings in Chroma database (persisted to disk)

### 2. **Question-Answering** (`main.py`)
   - User asks a question about mobile phones
   - System converts question to embedding and searches vector database
   - Retrieves top 3 most semantically similar reviews
   - Sends retrieved reviews + question to Ollama LLM
   - LLM generates answer based on the retrieved context
   - Answer is displayed to user

### 3. **Vector Database**
   - First run: Processes all reviews and creates embeddings (may take time)
   - Subsequent runs: Loads existing database for fast retrieval
   - Database location: `./chome_langchain_db/`

## ⚙️ Configuration

### Changing the Number of Retrieved Reviews

Edit `vector.py`:
```python
retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}  # Change this number
)
```

### Changing the LLM Model

Edit `main.py`:
```python
model = OllamaLLM(model="llama3.2")  # Change to your preferred model
```

### Changing the Embedding Model

Edit `vector.py`:
```python
embeddings = OllamaEmbeddings(model="mxbai-embed-large")  # Change embedding model
```

## 🔄 Re-indexing the Database

To reprocess the dataset and recreate the vector database:

1. Delete the database directory:
   ```bash
   rm -rf chome_langchain_db
   ```

2. Run the application again - it will automatically re-index

## 📝 Notes

- The vector database is created automatically on first run
- Processing time depends on dataset size (typically a few minutes for ~2000 reviews)
- All processing happens locally - no data is sent to external services
- The system handles missing/null values in the dataset gracefully

## 🤝 Contributing

Feel free to submit issues or pull requests to improve this project!

## 📄 License

This project is open source and available for educational purposes.

