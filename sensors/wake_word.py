from core.config import WAKE_WORD

def heard_wake_word(text):
    return WAKE_WORD.lower() in text.lower()

def strip_wake_word(text):
    return text.lower().replace(WAKE_WORD.lower(), "").strip()
