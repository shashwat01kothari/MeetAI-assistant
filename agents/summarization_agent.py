# backend/agents/summarization_agent.py

from services.llm_services import LLMService

class SummarizationAgent:
    """
    Agent responsible for generating a summary of a transcript.
    """
    def __init__(self):
        self.llm_service = LLMService()

    def summarize(self, transcript: str) -> str:
        """
        Generates a summary for the given transcript.

        Args:
            transcript (str): The meeting transcript.

        Returns:
            str: The summary text.
        """
        prompt = f"""You are an AI meeting assistant tasked with summarizing meetings. 
Read the transcript below and extract the most important points.

Instructions:
- Generate 5–8 concise key points that capture main discussions, decisions, and outcomes.
- Focus only on information that is relevant to understanding what happened in the meeting.
- Do NOT include action items or assignments; those are handled by another agent.
- Each point should be 1–2 sentences.

Transcript:
---
{transcript}
---

Output format:
- Summary Points:
  - 
"""
        print("Summarization Agent: Generating summary...")
        summary = self.llm_service.generate_text(prompt)
        print("Summarization Agent: Summary generated.")
        return summary