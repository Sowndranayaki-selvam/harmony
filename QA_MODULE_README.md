# 🤖 Custom Q&A Module

Your PDF-based question answering system that **only uses your data** - no external knowledge or third-party data allowed! Uses **FREE, local AI** with Ollama - no API keys or billing needed!

## ✨ Features

- ✅ Trains on **your `full data.pdf`** only
- ✅ **No external knowledge** - answers come exclusively from your data
- ✅ **100% FREE** - Uses Ollama local LLM (no API costs!)
- ✅ Vector embeddings for fast, accurate retrieval
- ✅ Source tracking - see which pages answer your questions
- ✅ Interactive & programmatic interface
- ✅ Built with LangChain + ChromaDB + HuggingFace embeddings

## 🚀 Quick Start (3 Steps)

### Step 1️⃣ Install Ollama (One-time setup)

**Windows:**
1. Download from [ollama.ai](https://ollama.ai)
2. Install the .exe
3. Run this in PowerShell:
```powershell
ollama pull mistral
```

### Step 2️⃣ Start Ollama Server

Keep this running while using Q&A module:
```powershell
ollama serve
```

### Step 3️⃣ Run Q&A Module

In a **new** PowerShell window:
```powershell
cd "c:\Users\USER\Desktop\harmony\python\openai_harmony"
python ask.py
```

**That's it!** Start asking questions! 🎯

## 💰 Cost: $0

- ✅ No API keys needed
- ✅ No billing accounts  
- ✅ No rate limits
- ✅ Runs locally on your machine

## 🎯 Example Usage

```
============================================================
🤖 Q&A Module - Trained on Your PDF Data Only
============================================================

⚙️  Checking for Ollama (local AI model)...
✅ Ollama found

🔄 Initializing Q&A module...
📄 Loading PDF: ../../data/full data.pdf
✅ Loaded 275 text chunks from PDF

============================================================
📝 Ask questions about your PDF (type 'quit' to exit)
============================================================

❓ Your question: What is the main topic?
🔍 Searching your data...
✅ Answer: Based on your PDF, the main topic is...
📄 Source pages: [1, 3, 5]

❓ Your question: quit
👋 Goodbye!
```

## 📁 File Structure

```
harmony/
├── data/
│   ├── full data.pdf          ← Your training data
│   └── chroma_db/             ← Vector embeddings (auto-created)
├── python/openai_harmony/
│   ├── qa_module.py           ← Main Q&A logic
│   ├── ask.py                 ← Interactive interface
│   └── __init__.py            ← Module exports
├── setup_ollama.bat           ← Auto-setup script (Windows)
└── QA_MODULE_README.md        ← This file
```

## 🔒 Data Privacy

- Your PDF stays on **YOUR computer**
- All processing is **local** (except AI model inference)
- No cloud storage
- No tracking
- Zero data collection

## 📖 Programmatic Usage

```python
from openai_harmony import CustomQAModule

# Initialize
qa = CustomQAModule("../../data/full data.pdf")

# Ask questions
result = qa.ask("What is the main topic?")
print(result["answer"])
print(result["sources"])

# Batch questions
results = qa.batch_ask([
    "Question 1?",
    "Question 2?",
])
```

## ⚙️ How It Works

1. **Load PDF** → Extract text from your document
2. **Split into chunks** → Break into searchable pieces
3. **Create embeddings** → Convert to vectors (HuggingFace - free!)
4. **Store in Vector DB** → ChromaDB for fast retrieval
5. **Process questions** → Find relevant chunks from YOUR PDF
6. **Generate answers** → Local Ollama AI uses only your data

## 🛠️ Troubleshooting

### "Ollama not found"
- Install from https://ollama.ai
- Make sure `ollama serve` is running in another terminal

### "Connection refused to localhost:11434"
- Start Ollama: `ollama serve`
- Keep that terminal open while using Q&A module

### "Model not found"
- Run: `ollama pull mistral`
- Wait for download to complete

### Slow responses
- First run creates embeddings (takes 1-2 min)
- Subsequent runs are faster (cached embeddings)
- Responses depend on PDF complexity

## 📦 Installed Packages

```
PyPDF2              - PDF reading
langchain           - LLM framework
langchain-core      - Core components
langchain-huggingface - Free embeddings
chromadb            - Vector database
ollama              - Local AI models
sentence-transformers - Embedding models
```

## 🎓 Advanced: Use Different Models

Want a faster model or specific language?

```bash
# Faster, smaller model
ollama pull neural-chat

# Better quality, larger model  
ollama pull llama2

# Download and use
ollama pull phi
```

Then update `qa_module.py`:
```python
llm = Ollama(
    model="your-model-name",  # Change this
    temperature=0,
    base_url="http://localhost:11434"
)
```

## 📝 Notes

- ✅ PDF: 275 text chunks extracted
- ✅ Embedding model: sentence-transformers/all-MiniLM-L6-v2 (free, fast)
- ✅ LLM: Mistral (7B parameters, accurate)
- ✅ Storage: Local ChromaDB (~50MB)

## 🚨 Important

This module **ONLY answers from your PDF**. It will NOT:
- ❌ Use Google or internet searches
- ❌ Use external knowledge bases
- ❌ Access third-party APIs
- ❌ Use real-time data

Perfect for confidential documents! 🔒

---

**Your module is ready!** 🎉

Start Ollama → Ask questions → Get answers from YOUR data!

