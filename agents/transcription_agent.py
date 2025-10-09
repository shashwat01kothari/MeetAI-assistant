# backend/agents/transcription_agent.py

from services.speech_service import SpeechToTextService


class AudioTranscriptionAgent:
    """
    Agent responsible for orchestrating the audio transcription process.
    """
    def __init__(self, engine: str = 'google'):
        self.speech_service = SpeechToTextService(engine=engine)

    def transcribe(self, audio_path: str) -> str:
        """
        Processes an audio file and returns the transcript.

        Args:
            audio_path (str): The path to the audio file.

        Returns:
            str: The transcribed text.
        """
        print(f"Transcription Agent: Transcribing '{audio_path}'...")
        transcript = self.speech_service.convert_audio_to_text(audio_path)
        print("Transcription Agent: Transcription complete.")
        return transcript