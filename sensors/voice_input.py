import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

q = queue.Queue()

def callback(indata, frames, time, status):
    q.put(bytes(indata))

class VoiceInput:
    def __init__(self):
        self.model = Model("models/vosk-model-small-en-us-0.15")
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def listen(self):
        with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=callback
        ):
            while True:
                data = q.get()
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        return text
