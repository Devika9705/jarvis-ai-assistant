import av
import numpy as np
import streamlit as st
import tempfile
import os
import wave
import speech_recognition as sr


class AudioProcessor:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recv(self, frame: av.AudioFrame):
        # Convert audio frame to numpy array
        audio = frame.to_ndarray()
        audio = np.mean(audio, axis=0).astype(np.int16)  # mono

        # Save as a temporary .wav file using wave module
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            with wave.open(f, 'wb') as wf:
                wf.setnchannels(1)  # mono
                wf.setsampwidth(2)  # 2 bytes = 16 bits
                wf.setframerate(frame.sample_rate)
                wf.writeframes(audio.tobytes())

            try:
                with sr.AudioFile(f.name) as source:
                    data = self.recognizer.record(source)
                    text = self.recognizer.recognize_google(data)
                    st.session_state["transcript"] = text
            except sr.UnknownValueError:
                st.session_state["transcript"] = "Could not understand."
            except sr.RequestError:
                st.session_state["transcript"] = "API unavailable."
            finally:
                os.remove(f.name)

        return frame
