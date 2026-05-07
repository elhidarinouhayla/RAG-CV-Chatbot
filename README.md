# RAG-CV-Chatbot

An intelligent chatbot that answers questions about your CV using Retrieval Augmented Generation (RAG)



 Objective
 
Build a chatbot that:

✅ Answers questions about your CV

✅ Uses a free LLM (Gemini 2.5 Flash )

✅ Implements RAG (Retrieval Augmented Generation)

✅ Uses a vector database (ChromaDB) 









##  Architecture

### Simple Version (chatbot_minimal.py)
```
CV Text → Gemini API → Response
```

### RAG Version (Full Stack)
```
PDF → Load → Chunk → Embed → ChromaDB
                                    ↓
User Question → Embed → Retrieve → LLM → Response
```

##  Project Structure

```

RAG-CV-CHATBOT/
├── data/
│   ├── pdf/                
│   └── vectordb/          
├── utils/                  
│   ├── __init__.py
│   ├── config.py          
│   ├── embedding.py       
│   ├── pdf_loading.py      
│   └── text_splitter.py   
├── venv/                  
├── .env                    
├── .gitignore              
├── app.py                 
├── ingest.py               
├── README.md               
└── requirements.txt
```

##  Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **LLM** | Gemini 2.5 Flash / Groq Llama 3.1 | Text generation |
| **Framework** | LangChain / Google GenAI | Orchestration |
| **Vector DB** | ChromaDB | Semantic search |
| **Embeddings** | HuggingFace (all-MiniLM-L6-v2) | Text → Vectors |
| **PDF Processing** | PyPDF / LangChain | Document loading |



##  API Keys (Free)

### Gemini 2.5 Flash (Recommended)
1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google
3. Click "Create API Key"
4. Copy the key (starts with `AIza...`)

**Limits**: 1500 requests/day, 60 requests/minute - FREE!


## Testing

### Test Questions 

** Should have answers (in CV):**
```
- "What are my technical skills?"
- "Tell me about my work experience"
- "What is my educational background?"
- "Which programming languages do I know?"
- "Where did I work as a Data Scientist?"
```


** Should NOT have answers (not in CV):**
```
- "Do I have experience in cooking?"
- "Can I play the piano?"
- "Have I worked in healthcare?"
```





## Troubleshooting

### "Module not found"
```bash
pip install -r requirements.txt
```

### "CV not found"
```bash
# Make sure your CV is in the right place
ls data/cv.pdf
```
