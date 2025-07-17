# APIAgentX 🔁🤖

**Agentic AI-Powered API Lifecycle Tool**  
Built using LangChain, HuggingFace LLMs, and Python

> APIAgentX leverages autonomous AI agents to transform user requirements into complete, production-ready API specifications, code, test cases, and documentation — all in one pipeline.

---

## 🚀 Key Features

| Agent Type           | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🔧 **Spec Generator**  | Converts natural language descriptions to OpenAPI 3.0 or gRPC proto specs   |
| ✅ **Validator Agent** | Reviews specs for errors, completeness, and best practices                 |
| 💻 **Code Generator**  | Generates REST stubs or gRPC server/client code (via OpenAPI or `protoc`) |
| 🧪 **Test Generator**  | Creates unit and integration test cases (Pytest, gRPC test stubs)          |
| 📘 **Doc Generator**   | Produces Markdown / Swagger docs from spec with examples                   |
| 🔁 **Multi-Agent Chain** | LangGraph-powered orchestration with feedback loop                       |
| 🔍 **RAG (Retrieval)** | Uses example specs and templates in vector DB to ground generation         |
| 🌐 **Streamlit UI**     | Interactive frontend to demo and test each phase                          |

---

## 🧠 Powered By

- [LangChain](https://www.langchain.com/)
- [HuggingFace Transformers](https://huggingface.co/models)
- [OpenAPI Python Client](https://github.com/openapi-generators/openapi-python-client)
- [Streamlit](https://streamlit.io/)
- [FAISS](https://github.com/facebookresearch/faiss) for RAG

---

1. Clone the repo, Run the following commands in your terminal:

git clone https://github.com/yourusername/APIAgentX.git  
cd APIAgentX

2. Setup virtual environment

python3 -m venv venv && source venv/bin/activate  
pip install -r requirements.txt

3. Set HuggingFace API key

echo "HUGGINGFACEHUB_API_TOKEN=your_token_here" > .env

4. Run Agent Pipeline from CLI

python main.py

5. Launch Streamlit UI

streamlit run ui/streamlit_app.py

🧠 Example Input
File: examples/input_description.txt

Example content:

Design a REST API to manage user profiles and accounts. It should support registration, login, password reset, and updating profile fields. Use JWT for authentication.

The agents will generate:

Full OpenAPI spec
Validation report
Python FastAPI stubs
Pytest unit tests
Markdown/Swagger docs

🔮 Future Roadmap

✅ gRPC support with protoc
✅ LangGraph-based feedback loops
✅ Semantic RAG from internal knowledge base
🔐 OAuth2/OpenID agent flows
📁 Export to Postman, Insomnia, or SwaggerHub
📦 Docker + GitHub Actions for CI/CD

