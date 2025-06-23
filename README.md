# 🧠 Memora AI

**Memora AI is a macOS desktop assistant that transforms your screen into an extension of your memory.** Highlight any text, press a shortcut, and instantly chat with an AI that remembers everything you've seen, learned, and asked.

[![Project Status](https://img.shields.io/badge/status-in%20development-yellow.svg)](https://github.com/tanishwas/memora-ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

## ✨ Features

- **🔍 Universal Capture**: Highlight text in any application on your Mac, press `⌘+⇧+M`, and start a conversation.
- **🧠 Personal Memory Base**: Every interaction is stored, embedded, and used to provide more contextually relevant answers over time.
- **💬 Context-Aware Chat**: When you highlight similar text again, Memora automatically retrieves past conversations and insights.
- **📝 Automated Note-Taking**: Let the AI agent summarize your discussions and highlighted material into clean, bullet-pointed notes.
- **🔄 Adaptive Learning**: The system learns what you know, tracks what you struggle with, and helps you connect ideas across different sources.

## 🚀 Getting Started

### Prerequisites

- macOS
- Node.js + Yarn (or npm)
- Python 3.10+
- An [OpenAI API Key](https://platform.openai.com/account/api-keys)
- Homebrew (`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`)
- Tesseract for OCR fallback: `brew install tesseract`

### Run Locally

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/tanishwas/memora-ai.git](https://github.com/tanishwas/memora-ai.git)
    cd memora-ai
    ```

2.  **Setup the Backend:**

    ```bash
    cd backend
    pip install -r requirements.txt
    cp .env.example .env
    # Now, add your OpenAI API Key to the .env file
    python app.py
    ```

    The backend server will be running on `http://localhost:8000`.

3.  **Setup the Frontend:**
    ```bash
    # Open a new terminal window in the project root
    cd client
    yarn install
    yarn start # (Note: This is a placeholder, full Electron setup required)
    ```

## 🧱 Tech Stack

| Layer            | Technology                      | Purpose                                          |
| :--------------- | :------------------------------ | :----------------------------------------------- |
| **UI (macOS)**   | Electron, React, TypeScript     | Desktop application frame, UI rendering          |
| **Backend**      | Python, FastAPI                 | Core API server for all intelligent operations   |
| **AI/LLM**       | LangChain, OpenAI API           | Orchestrating prompts, chat logic, summarization |
| **Embeddings**   | FAISS, `text-embedding-3-small` | Vector storage and semantic search               |
| **Data Storage** | SQLite                          | Storing metadata and chat history                |
| **Native APIs**  | Swift / Objective-C (Optional)  | For robust, native text-capture                  |
| **OCR Fallback** | Tesseract                       | Capturing text from non-selectable areas         |

## 🧠 Architecture

<img src="./docs/architecture.png" width="700" alt="Memora AI Architecture Diagram" />

## 🔓 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Tanish Pradhan Wong Ah Sui**

- **GitHub**: [@tanishwas](https://github.com/tanishwas)
- **LinkedIn**: [LinkedIn Profile](https://www.linkedin.com/in/your-profile-url) ```

---

### ✅ Action 5: GitHub Issues for Project Board

Here is a list of starter issues based on your MVP. You can create these in your GitHub repository's "Issues" tab. This will give you a great starting point for a Kanban or project board.

**Issue 1: Core Backend Setup**

- **Title**: `[CORE] Setup FastAPI Backend with Docker`
- **Description**:
  - As a developer, I need a basic FastAPI server running.
  - **Acceptance Criteria:**
    - `backend/app.py` is created.
    - `requirements.txt` includes `fastapi` and `uvicorn`.
    - A simple `/health` endpoint returns `{"status": "ok"}`.
    - A `.env.example` file is present for environment variables.

**Issue 2: Database Schema & Setup**

- **Title**: `[DB] Define and Implement SQLite Schema`
- **Description**:
  - As the backend, I need a database to store conversations and metadata.
  - **Acceptance Criteria:**
    - Use `sqlite-utils` or `SQLAlchemy` to manage the DB.
    - Define tables for `conversations` (id, user_id, timestamp) and `messages` (id, convo_id, role, content, highlighted_text).
    - Create a utility function to initialize the database if it doesn't exist.

**Issue 3: Text Capture (Electron)**

- **Title**: `[FEAT] Implement Global Shortcut and Text Capture`
- **Description**:
  - As a user, I want to press a global shortcut (`⌘+⇧+M`) to trigger the app.
  - **Acceptance Criteria:**
    - Electron's `globalShortcut` module is used to register the shortcut.
    - When triggered, the app should capture the currently highlighted text system-wide.
    - Investigate using native macOS APIs (via a Swift/Node bridge like `node-swift`) for the most reliable text capture.
    - The captured text should be passed to the main chat window.

**Issue 4: Chat UI Popup**

- **Title**: `[UI] Build Chat Popup Window`
- **Description**:
  - As a user, when I trigger the shortcut, I want a chat window to appear.
  - **Acceptance Criteria:**
    - A borderless Electron window is created.
    - The React component `App.tsx` renders the chat interface.
    - The interface shows the highlighted text, an input box for a query, and a display area for the conversation.
    - The window can be closed easily (e.g., by pressing `Esc` or clicking outside).

**Issue 5: API Integration**

- **Title**: `[API] Connect Frontend to Backend Chat Endpoint`
- **Description**:
  - As a user, when I submit a query, I want it sent to the backend for processing.
  - **Acceptance Criteria:**
    - The Electron/React frontend makes a `POST` request to the FastAPI `/api/chat` endpoint.
    - The request body includes the `highlighted_text` and `query`.
    - The frontend displays the `answer` from the API response.

**Issue 6: Embedding & Storage Logic**

- **Title**: `[AI] Implement Embedding and FAISS/SQLite Storage`
- **Description**:
  - As the backend, I need to process and store each interaction for future retrieval.
  - **Acceptance Criteria:**
    - Integrate the OpenAI embeddings model (`text-embedding-3-small`).
    - After a chat, generate an embedding for the `highlighted_text`.
    - Store the embedding in a FAISS index, saved to the `embeddings/` directory.
    - Store the corresponding text and conversation metadata in the SQLite database.

**Issue 7: Memory Retrieval**

- **Title**: `[AI] Implement Semantic Search for Memory Retrieval`
- **Description**:
  - As the backend, before querying the LLM, I need to retrieve relevant past conversations.
  - **Acceptance Criteria:**
    - When `/api/chat` is called, generate an embedding for the new `highlighted_text`.
    - Use the new embedding to search the FAISS index for the top `k` most similar past highlights.
    - Retrieve the context of those past highlights from SQLite.
    - Pass this retrieved context into the final LLM prompt.

**Issue 8: Auto-Note Summarization**

- **Title**: `[AI] Create LangChain Agent for Note Summarization`
- **Description**:
  - As a user, I want to receive an automatic summary of my interaction.
  - **Acceptance Criteria:**
    - Create a LangChain "chain" or "agent" responsible for summarization.
    - The agent takes the current conversation (highlight, query, answer) as input.
    - It calls the LLM with a specific prompt to generate bullet-pointed notes.
    - The summary is returned as part of the `/api/chat` response.

---

You now have a complete, structured project ready for you to start building. Your next step is to run the commands from Action 3, set up your Git repository, and start tackling the GitHub issues one by one. Good luck!
