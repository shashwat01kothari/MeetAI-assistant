# backend/services/nlp_service.py
import spacy
from textblob import TextBlob

class NLPService:
    """
    A service for handling core NLP tasks like NER and sentiment analysis.
    """
    def __init__(self):
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("Downloading 'en_core_web_sm' model...")
            spacy.cli.download("en_core_web_sm")
            self.nlp = spacy.load("en_core_web_sm")

    def extract_entities(self, text: str, entity_types: list = ["PERSON"]) -> list:
        """
        Extracts named entities from text.

        Args:
            text (str): The input text.
            entity_types (list): The types of entities to extract (e.g., ["PERSON", "ORG"]).

        Returns:
            list: A list of extracted entity texts.
        """
        doc = self.nlp(text)
        return [ent.text for ent in doc.ents if ent.label_ in entity_types]

    def analyze_sentiment(self, text: str, polarity_threshold: float = -0.2) -> list:
        """
        Finds sentences with negative sentiment.

        Args:
            text (str): The input text.
            polarity_threshold (float): The sentiment polarity below which a sentence is considered critical.

        Returns:
            list: A list of sentences with negative sentiment.
        """
        blob = TextBlob(text)
        return [str(sentence) for sentence in blob.sentences if sentence.sentiment.polarity < polarity_threshold]