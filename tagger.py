# tagger.py

from googletrans import Translator
from emotagger.translator import translate_to_english  # Avoid circular imports
import re

# Define emotions and associated keywords
EMOTION_KEYWORDS = {
    'happy': ['happy', 'joy', 'pleased', 'glad', 'delighted', 'smile'],
    'sad': ['sad', 'unhappy', 'depressed', 'cry', 'tearful', 'miserable'],
    'angry': ['angry', 'mad', 'furious', 'rage', 'irritated', 'annoyed'],
    'fear': ['afraid', 'scared', 'fear', 'terrified', 'anxious', 'nervous'],
    'surprise': ['surprised', 'shocked', 'amazed', 'astonished'],
    'disgust': ['disgusted', 'gross', 'revolted', 'nauseated'],
    'neutral': []
}

# Optional: Add emoji representation
EMOJI_MAP = {
    'happy': '😊',
    'sad': '😢',
    'angry': '😠',
    'fear': '😨',
    'surprise': '😲',
    'disgust': '🤢',
    'neutral': '😐'
}


def tag_emotions(text):
    """
    Tag emotions in plain English text using keyword matching.
    """
    text_lower = text.lower()
    matched_emotions = []

    for emotion, keywords in EMOTION_KEYWORDS.items():
        if any(re.search(r'\b' + re.escape(word) + r'\b', text_lower) for word in keywords):
            matched_emotions.append(emotion)

    if not matched_emotions:
        matched_emotions.append('neutral')

    return matched_emotions


def tag_emotions_multilingual(text):
    """
    Translate non-English text to English and detect emotions.
    """
    print("🌐 Translating and tagging emotions...")

    # Translate to English using Google Translate
    translated_text, detected_lang = translate_to_english(text)

    print(f"🗣️ Original Language: {detected_lang}")
    print(f"🔤 Translated Text: {translated_text}")

    # Tag emotions using the English version
    emotions = tag_emotions(translated_text)

    return {
        'original_text': text,
        'translated_text': translated_text,
        'language': detected_lang,
        'emotions': emotions,
        'emojis': [EMOJI_MAP.get(e, '') for e in emotions]
    }
