
# Meeting AI Assistant v1.0

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)![License](https://img.shields.io/badge/license-MIT-green)![Status](https://img.shields.io/badge/status-stable-brightgreen)

Transform chaotic meeting audio or text into structured, actionable intelligence. This multi-agent AI assistant automates the process of transcribing, summarizing, and analyzing meetings to save time and boost productivity.

![Demo Placeholder](https://user-images.githubusercontent.com/10213036/144653699-b1085954-20a2-4786-82f5-932f22b72445.png)
*(Demo GIF would go here)*

## ✨ Core Features (v1.0)

*   **Automated Audio Transcription**: Converts `.wav` or `.mp3` audio files into clean text transcripts using Google's Speech-to-Text engine.
*   **Intelligent Analysis Agent**: A powerful, efficient agent that generates both a concise summary and strategic insights (risks, opportunities) in a single, optimized API call.
*   **Robust Action Item Extraction**: A self-correcting agent that uses a hybrid NER + LLM approach to identify tasks and assign owners. It intelligently detects NER failures and adjusts its strategy to ensure the best possible results.
*   **Interactive Dependency Graph**: Visualizes the relationships between tasks and their owners using an interactive graph, making project dependencies clear at a glance.
*   **Resilient API Handling**: Implements an intelligent retry mechanism with exponential backoff that respects API rate limits and suggested wait times, ensuring the application runs smoothly.
*   **Intuitive UI**: A clean and simple user interface built with Streamlit for easy file uploads and text input.

## 🏛️ Project Architecture

This project is built on a modular, agent-based architecture that separates concerns for maintainability and scalability.

*   **Services (`/services`)**: These are the specialized "tools" of the system. Each service performs one core function, such as interfacing with the Gemini LLM (`llm_service.py`), handling speech-to-text (`speech_service.py`), or performing NLP tasks (`nlp_service.py`).
*   **Agents (`/agents`)**: These are the "orchestrators" or "brains." An agent is responsible for accomplishing a complex goal by intelligently using one or more services. For example, the `ActionItemAgent` uses both the `NLPService` and the `LLMService` to complete its task.
*   **UI (`app.py`)**: The main Streamlit application that orchestrates the agents and presents the final output to the user.

## 🛠️ Tech Stack

*   **LLM API**: Google Gemini 1.5 Flash
*   **UI**: Streamlit
*   **NLP**: spaCy, TextBlob
*   **Speech-to-Text**: SpeechRecognition
*   **Data Visualization**: NetworkX & Pyvis
*   **Core Language**: Python 3.10+

## 🚀 Setup and Installation

Follow these steps to get the Meeting AI Assistant running on your local machine.

### 1. Prerequisites
*   Python 3.10 or higher.
*   A Google Account.

### 2. Clone the Repository
```bash
git clone https://github.com/shashwat01kothari/MeetAI-assistant.git
cd meetingai-assistant
```

### 3. Create a Virtual Environment (Recommended)
This keeps your project dependencies isolated.
```bash
# Create the virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
Install all required libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 5. Download the NLP Model
The project uses a spaCy model for Named Entity Recognition. Download it with the following command:
```bash
python -m spacy download en_core_web_sm
```

### 6. Set Up Your API Key
The application requires a Google Gemini API key to function.

*   **Get your key**: Visit [Google AI Studio](https://aistudio.google.com/) and click **"Get API key"** to create a new key.
*   **Create a `.env` file**: In the root of the project, create a new file named `.env`.
*   **Add your key**: Add the following line to the `.env` file, replacing `"YOUR_API_KEY_HERE"` with the key you just copied.
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

## ▶️ Running the Application

With the setup complete, you can run the Streamlit app from the project's root directory.

```bash
streamlit run app.py
```

Open your web browser and navigate to the local URL provided by Streamlit (usually `http://localhost:8501`).

## 📁 Project Structure (v1.0)

Reflecting the new flattened architecture for simplicity.

```
meeting-ai-assistant/
│
├── agents/
│   ├── __init__.py
│   ├── transcription_agent.py
│   ├── analysis_agent.py
│   └── action_item_agent.py
│   └── dependency_graph_agent.py
│
├── services/
│   ├── __init__.py
│   ├── speech_service.py
│   ├── nlp_service.py
│   └── llm_service.py
│   └── graph_service.py
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py
│   └── decorators.py
│
├── .env
├── config.py
├── app.py
└── requirements.txt
```

## 🗺️ Roadmap: The Vision for v2.0

Version 1.0 provides a powerful tool for analyzing completed meetings. Version 2.0 will focus on real-time intelligence and deeper context awareness.

*   **🔮 Live Meeting Rendering**: An advanced agent will transcribe meeting audio in real-time, displaying the transcript, summary, and action items as they are spoken. This provides an immediate, shared understanding for all participants.

*   **💻 Screen Overlay Processing**: The assistant will gain the ability to process screen shares. By analyzing visuals from presentations, documents, or whiteboards, it will enrich the meeting context, understand visual cues, and generate more accurate and insightful summaries.

*   **🔗 Deeper Integrations**: Seamlessly push action items to project management tools like Jira, Asana, or Trello directly from the assistant's UI.

