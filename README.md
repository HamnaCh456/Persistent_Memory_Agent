# Streamlit Memory Agent (Groq + Mem0)

This is a simple Streamlit-based conversational agent that combines **Groq** LLM responses with persistent memory storage using the **Mem0** API.  
The app retrieves past user conversations based on similarity search and uses them to provide personalized responses.

---

## Features

- 🔁 Stores each user/assistant message in Mem0
- 🔍 Retrieves relevant memories for a new user query
- 🤖 Uses Groq API (LLM) to generate responses conditioned on the retrieved memory
- 🌐 Web-based interface powered by Streamlit

---

## ⚙️ Setup

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd <repo>
````

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API keys to a `.env` file

Create a file named `.env` in the root folder and add:

```
GROQ_API_KEY=your_groq_api_key
MEM0_API_KEY=your_mem0_api_key
```

---

## Run the app

```bash
streamlit run <your_python_file>.py
```

---

## How it works

1. The user enters a query in the StreamlitInput.
2. The app fetches relevant memory from Mem0 using similarity search.
3. The retrieved memory is provided as context to the Groq LLM.
4. The generated response is displayed to the user and stored in Mem0 along with the query.

---

## Project Structure

```
.
├─ <your_python_file>.py   # Main Streamlit app
├─ requirements.txt
└─ .env                    # (not committed) – contains your API keys
```

---

## Notes

* The user\_id is currently hard-coded as `"john"`.
  Update it if you want to support multiple users.
