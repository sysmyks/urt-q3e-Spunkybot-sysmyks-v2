from deep_translator import GoogleTranslator


def translate_text(text, target_lang):
    """Translate text to target_lang using Google Translate (no API key needed)."""
    translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
    return translated if translated else text
