# backend/agents/action_item_agent.py

import json
import re
from typing import Tuple, Optional 

from services.llm_services import LLMService
from services.nlp_services import NLPService

class ActionItemAgent:
    """
    Agent responsible for extracting action items.
    Includes a check for NER performance and adjusts its strategy accordingly.
    """
    def __init__(self):
        self.llm_service = LLMService()
        self.nlp_service = NLPService()

    def extract_action_items(self, transcript: str) -> Tuple[list, Optional[str]]:
        """
        Extracts action items from the transcript.

        Args:
            transcript (str): The meeting transcript.

        Returns:
            tuple: A tuple containing:
                - list: A list of action items (dictionaries).
                - str or None: A warning message if NER failed, otherwise None.
        """
        ner_warning = None
        persons = self.nlp_service.extract_entities(transcript, entity_types=["PERSON"])
        
        # --- NEW: NER Performance Check ---
        if not persons:
            ner_warning = "Warning: The NER model did not detect any person names. The LLM will attempt to infer owners, but results may be less accurate. Please verify the assigned owners."
            print(f"Action Item Agent: {ner_warning}")
            # Dynamic prompt modification if NER fails
            prompt_context = "The NER model failed to identify specific names. Please analyze the transcript and infer the owner of each task from the context. The owner should be the name of a person mentioned in the text."
        else:
            # Original prompt if NER succeeds
            prompt_context = f"The people identified in this meeting are: {', '.join(persons)}. The 'owner' for each task MUST be one of these people."

        # Construct the full prompt
        prompt = f"""
        Analyze the following meeting transcript to identify and extract any clear action items.
        An action item is a specific task assigned to a specific person.
        {prompt_context}

        Your response MUST be a valid JSON array of objects.
        Each object in the array must have two keys: "task" and "owner".

        DO NOT include any introductory text, explanations, or markdown formatting like ```json.
        Your entire output must be ONLY the JSON array.

        If no action items are found, you MUST return an empty array: [].

        Transcript:
        ---
        {transcript}
        ---
        """
        
        print("Action Item Agent: Extracting action items...")
        response_text = self.llm_service.generate_text(prompt)
        print(f"Action Item Agent: Raw LLM response:\n---\n{response_text}\n---")
        
        try:
            json_match = re.search(r'\[.*\]', response_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(0)
                action_items = json.loads(json_str)
            else:
                action_items = []
        except json.JSONDecodeError:
            print("Action Item Agent: Failed to decode JSON even after regex extraction.")
            action_items = []
            
        print(f"Action Item Agent: Found {len(action_items)} action items.")
        # Return both the results and the potential warning
        return action_items, ner_warning