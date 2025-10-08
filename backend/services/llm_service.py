# backend/services/llm_service.py
import google.generativeai as genai
from config import GEMINI_API_KEY

class LLMService:
    """
    A service to interact with a Large Language Model (Gemini).
    """
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY not found. Please set it in your .env file.")
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel('gemini-2.5-pro')

    def generate_text(self, prompt: str) -> str:
        """
        Generates text based on a given prompt.

        Args:
            prompt (str): The input prompt for the LLM.

        Returns:
            str: The generated text from the LLM.
        """
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Error generating text from LLM: {e}"