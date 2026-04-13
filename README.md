# 🚀 Enterprise RAG Q&A System (AWS Bedrock)

## 📌 Overview  
This project is an **Enterprise-grade Retrieval-Augmented Generation (RAG) Q&A system** built using **AWS Bedrock**, designed to answer user queries based on custom documents.  

It demonstrates how **Generative AI + Retrieval Systems** can be combined to build intelligent, scalable, and production-ready applications using AWS cloud services.

---

## ✨ Key Features  
- 🔹 Retrieval-Augmented Generation (RAG) pipeline  
- 🔹 Integration with AWS Bedrock Knowledge Base  
- 🔹 Semantic search using vector embeddings  
- 🔹 Document ingestion via Amazon S3  
- 🔹 Scalable vector storage using OpenSearch Serverless  
- 🔹 Secure access using IAM Roles (no hardcoded credentials)  
- 🔹 Real-time Q&A system  

---

## 🛠️ Tech Stack  

| Category | Tools / Services |
|--------|----------------|
| Backend | Python |
| AI/ML | AWS Bedrock |
| Storage | Amazon S3 |
| Vector DB | OpenSearch Serverless |
| SDK | Boto3 |
| Cloud | AWS |
| Version Control | Git & GitHub |

---

## 🧠 Architecture  

User Query  
↓  
Application (Python / API)  
↓  
AWS Bedrock Knowledge Base  
↓  
Vector Search (OpenSearch)  
↓  
Relevant Documents Retrieved  
↓  
LLM (Titan / Claude)  
↓  
Final Answer Generated  

---

## 📂 Project Structure  

enterprise-rag-bedrock-qa-system/  
│── app.py              # Main application logic  
│── requirements.txt    # Dependencies  
│── README.md           # Documentation  

---

## ⚙️ Setup & Installation  

### 1️⃣ Clone Repository  
```bash
git clone https://github.com/your-username/enterprise-rag-bedrock-qa-system.git
cd enterprise-rag-bedrock-qa-system
```

---

### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

---

### 3️⃣ AWS Configuration  

Ensure AWS is properly configured:

```bash
aws configure
```

OR use IAM Role (recommended for production / EC2):

✔ AmazonBedrockFullAccess  
✔ AmazonS3FullAccess  

---

### 4️⃣ Create Knowledge Base (IMPORTANT)

Before running the app:

1. Upload documents to S3 bucket  
2. Create Bedrock Knowledge Base  
3. Configure:
   - Embedding model (Titan Embeddings)
   - Vector store (OpenSearch Serverless)
4. Sync data source  

---

### 5️⃣ Update Configuration  

Replace your Knowledge Base ID in code:

```python
KNOWLEDGE_BASE_ID = "YOUR_KB_ID"
REGION = "us-east-1"
```

---

### 6️⃣ Run the Application  

```bash
python app.py
```

---

## 🔍 How It Works  

1. User enters a query  
2. Query is sent to Bedrock Knowledge Base  
3. Relevant documents are retrieved  
4. LLM generates context-aware response  
5. Final answer is returned to user  

---

## ⚠️ Challenges Faced  

- ❌ AWS service activation delays  
- ❌ IAM role misconfigurations  
- ❌ Region-based model availability  
- ❌ OpenSearch Serverless setup issues  

---

## ✅ Solutions  

- Used IAM roles instead of access keys  
- Fixed trust policies for Bedrock access  
- Ensured AWS account activation  
- Configured correct region (us-east-1)  

---

## 🚀 Future Enhancements  

- 🔹 Add Streamlit / Web UI  
- 🔹 Implement chat history (memory)  
- 🔹 Add authentication layer  
- 🔹 Optimize retrieval (chunking + ranking)  
- 🔹 Multi-document support  

---

## 👨‍💻 Author  

**Lokesh Naidu**  
B.Tech CSE (AI & ML)  
Data Science Trainee @ Innomatics  

---

## 📌 Note  

This project requires AWS Bedrock access.  
Ensure your AWS account is fully activated and has required permissions.
