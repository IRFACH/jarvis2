import subprocess
import os
import time

AUDIO_FILE = "/data/data/com.termux/files/home/jarvis_input.wav"
WHISPER_BIN = "./whisper.cpp/main"
WHISPER_MODEL = "./whisper.cpp/models/ggml-base.en.bin"

class VoiceInput:
    def init(self, record_seconds=3):
        self.record_seconds = record_seconds

    def listen(self):
        # Remove old audio if exists
        if os.path.exists(AUDIO_FILE):
            os.remove(AUDIO_FILE)

        # Record audio
        subprocess.run([
            "termux-microphone-record",
            "-f", AUDIO_FILE,
            "-l", str(self.record_seconds)
        ], check=True)

        # Small delay to ensure file is saved
        time.sleep(0.3)

        # Run whisper.cpp
        subprocess.run([
            WHISPER_BIN,
            "-m", WHISPER_MODEL,
            "-f", AUDIO_FILE,
            "-otxt",
            "-of", "jarvis_transcript"
        ], check=True)

        # Read output
        txt_file = "jarvis_transcript.txt"
        if os.path.exists(txt_file):
            with open(txt_file, "r", encoding="utf-8") as f:
                return f.read().strip()

        return ""
