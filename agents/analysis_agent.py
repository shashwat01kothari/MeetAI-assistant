# backend/agents/analysis_agent.py

import json
from services.llm_services import LLMService
from services.nlp_services import NLPService

class AnalysisAgent:
    """
    A powerful agent that combines summarization and insight generation
    into a single, efficient operation.
    """
    def __init__(self):
        self.llm_service = LLMService()
        self.nlp_service = NLPService()

    def analyze(self, transcript: str) -> dict:
        """
        Analyzes a transcript to generate a summary and insights in a single call.

        Args:
            transcript (str): The meeting transcript.

        Returns:
            dict: A dictionary containing 'summary' and 'insights' keys.
                  Returns a default structure on failure.
        """
        critical_sentences = self.nlp_service.analyze_sentiment(transcript)
        
        prompt = f"""
        You are an expert meeting analyst. Your task is to process the following meeting transcript
        and provide a concise summary and strategic insights.

        Based on the full transcript and the provided critical sentences, generate:
        1. A summary of 5-8 key bullet points.
        2. A list of 2-5 potential insights, risks, or opportunities.

        Please return your response as a single, valid JSON object with two keys: "summary" and "insights".
        The "summary" key should have a value of an array of strings.
        The "insights" key should have a value of an array of strings.

        Example Format:
        {{
          "summary": ["Key discussion point one.", "Decision made on project X.", "Follow-up required from Alice."],
          "insights": ["Risk: The deadline for module Y is tight.", "Opportunity: We can leverage the new library to speed up development."]
        }}

        ---
        Identified Critical Sentences:
        {' '.join(critical_sentences) or "None"}
        ---
        Full Meeting Transcript:
        {transcript}
        ---
        """
        
        print("Analysis Agent: Generating summary and insights...")
        response_text = self.llm_service.generate_text(prompt)
        
        # --- Robust JSON Parsing ---
        try:
            # Clean the response to ensure it's valid JSON
            json_str = response_text.strip().lstrip("```json").rstrip("```")
            analysis_result = json.loads(json_str)
            
            # Ensure the result contains the expected keys
            if "summary" not in analysis_result or "insights" not in analysis_result:
                raise KeyError("Missing 'summary' or 'insights' key in LLM response.")

            print("Analysis Agent: Analysis complete.")
            return analysis_result

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Analysis Agent: Error parsing JSON response - {e}. Returning default structure.")
            # Fallback to a safe, empty structure
            return {
                "summary": ["Failed to generate summary from the transcript."],
                "insights": ["Failed to generate insights from the transcript."]
            }