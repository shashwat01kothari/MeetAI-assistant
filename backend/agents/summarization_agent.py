# backend/agents/summarization_agent.py
from backend.services.llm_service import LLMService

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
        prompt = f"Summarize the following meeting transcript into 5-8 key bullet points:\n\n---\n{transcript}\n---"
        print("Summarization Agent: Generating summary...")
        summary = self.llm_service.generate_text(prompt)
        print("Summarization Agent: Summary generated.")
        return summary