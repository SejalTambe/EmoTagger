# translator.py

from googletrans import Translator

translator = Translator()

def translate_to_english(text):
    """
    Translate any text to English using Google Translate API.
    Returns translated text and detected language.
    """
    try:
        detected = translator.detect(text)
        detected_lang = detected.lang

        # Translate only if not English
        if detected_lang != "en":
            translated = translator.translate(text, dest="en")
            return translated.text, detected_lang
        else:
            return text, 'en'

    except Exception as e:
        print(f"⚠️ Translation error: {e}")
        return text, 'unknown'
