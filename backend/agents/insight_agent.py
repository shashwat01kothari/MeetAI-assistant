# backend/agents/insight_agent.py
from backend.services.llm_service import LLMService
from backend.services.nlp_service import NLPService

class InsightAgent:
    """
    Agent that detects potential risks, challenges, or opportunities.
    """
    def __init__(self):
        self.llm_service = LLMService()
        self.nlp_service = NLPService()

    def generate_insights(self, transcript: str) -> str:
        """
        Generates insights from the transcript.

        Args:
            transcript (str): The meeting transcript.

        Returns:
            str: A string containing insights and risks.
        """
        critical_sentences = self.nlp_service.analyze_sentiment(transcript)
        
        prompt = f"""
        Based on the following meeting transcript and the identified critical sentences,
        generate a list of 2-5 potential insights, risks, or opportunities.
        Focus on strategic points that could impact the project.

        Identified Critical Sentences:
        ---
        {' '.join(critical_sentences) or "None"}
        ---

        Full Transcript:
        ---
        {transcript}
        ---
        """
        print("Insight Agent: Generating insights...")
        insights = self.llm_service.generate_text(prompt)
        print("Insight Agent: Insights generated.")
        return insights