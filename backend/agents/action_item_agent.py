# backend/agents/action_item_agent.py
from backend.services.llm_service import LLMService
from backend.services.nlp_service import NLPService
import json

class ActionItemAgent:
    """
    Agent responsible for extracting action items and assigning owners.
    """
    def __init__(self):
        self.llm_service = LLMService()
        self.nlp_service = NLPService()

    def extract_action_items(self, transcript: str) -> list:
        """
        Extracts action items from the transcript.

        Args:
            transcript (str): The meeting transcript.

        Returns:
            list: A list of action items, where each item is a dictionary.
        """
        persons = self.nlp_service.extract_entities(transcript, entity_types=["PERSON"])
        
        prompt = f"""
        Given the following meeting transcript and the identified persons ({', '.join(persons)}),
        extract the action items.
        An action item must be a clear task assigned to one of the identified persons.
        Return the output as a valid JSON array of objects, where each object has a "task" and an "owner".
        If no action items are found, return an empty array [].

        Transcript:
        ---
        {transcript}
        ---
        """
        print("Action Item Agent: Extracting action items...")
        response_text = self.llm_service.generate_text(prompt)
        
        try:
            # Clean the response to ensure it's valid JSON
            json_str = response_text.strip().lstrip("```json").rstrip("```")
            action_items = json.loads(json_str)
        except json.JSONDecodeError:
            print("Action Item Agent: Failed to decode JSON from LLM response.")
            action_items = []
            
        print(f"Action Item Agent: Found {len(action_items)} action items.")
        return action_items