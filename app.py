# app.py

from emotagger import tag_emotions_multilingual, EMOJI_MAP, translate_to_english

def main():
    print("🌍 EmoTagger CLI - Multilingual Emotion Detection")
    print("Type your sentence (or type 'exit' to quit):\n")

    while True:
        text = input("📝 Your Input: ")
        if text.strip().lower() == "exit":
            print("👋 Exiting EmoTagger.")
            break

        if not text.strip():
            print("⚠️ Please enter some text.")
            continue

        result = tag_emotions_multilingual(text)

        print("\n🗣️ Original Text:", result['original_text'])
        print("🌐 Detected Language:", result['language'])
        print("🔤 Translated Text:", result['translated_text'])
        print("💬 Emotions Detected:", ', '.join(result['emotions']))
        print("😊 Emojis:", ' '.join(result['emojis']))
        print("-" * 40)

if __name__ == "__main__":
    main()
