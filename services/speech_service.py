# backend/services/speech_service.py
import speech_recognition as sr

class SpeechToTextService:
    """
    A service to handle speech-to-text conversion using various engines.
    """
    def __init__(self, engine: str = 'google'):
        self.recognizer = sr.Recognizer()
        self.engine = engine

    def convert_audio_to_text(self, audio_path: str) -> str:
        """
        Transcribes an audio file.

        Args:
            audio_path (str): Path to the audio file.

        Returns:
            str: The transcribed text or an error message.
        """
        with sr.AudioFile(audio_path) as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio_data = self.recognizer.record(source)
        
        try:
            if self.engine == 'google':
                return self.recognizer.recognize_google(audio_data)
            elif self.engine == 'sphinx':
                return self.recognizer.recognize_sphinx(audio_data)
            else:
                raise ValueError(f"Unsupported engine: {self.engine}")
        except sr.UnknownValueError:
            return "Transcription failed: Audio could not be understood."
        except sr.RequestError as e:
            return f"Transcription failed: Service request error; {e}"