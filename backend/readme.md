project structure 


meeting-ai-assistant/
│
├── backend/
│   ├── __init__.py
│   │
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── transcription_agent.py
│   │   ├── summarization_agent.py
│   │   ├── action_item_agent.py
│   │   ├── insight_agent.py
│   │   └── dependency_graph_agent.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── speech_service.py
│       ├── nlp_service.py
│       ├── llm_service.py
│       └── graph_service.py
│
├── utils/
│   ├── __init__.py
│   └── file_handler.py
│
|
├── .env (add you own)
├── config.py 
├── app.py
└── requirements.txt