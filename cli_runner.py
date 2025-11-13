from emotagger import tag_emotions

# Emotion to emoji mapping
EMOJI_MAP = {
    "joy": "😊",
    "sadness": "😢",
    "anger": "😠",
    "fear": "😨",
    "disgust": "🤢",
    "surprise": "😲",
    "love": "❤️",
    "guilt": "😔",
    "anticipation": "🤞",
    "regret": "😞",
    "relief": "😌",
    "pride": "🏆",
    "shame": "🙈",
    "neutral": "😐",
    "confused": "🤔"
}

def print_emotions_with_emoji(emotions):
    if not emotions:
        print(f"🤖 Detected Emotions: None {EMOJI_MAP['confused']}")
    else:
        print("🤖 Detected Emotions:")
        for emotion in emotions:
            label = emotion['label'].lower()
            emoji = EMOJI_MAP.get(label, "🔍")
            score = emotion['score']
            print(f"- {label} {emoji} ({score:.2f})")


def main():
    print("🧠 EmoTagger CLI - AI-based Emotion Detection")
    print("Type your sentence (or type 'exit' to quit):")

    while True:
        text = input("You: ")
        if text.lower() in ("exit", "quit"):
            print("👋 Exiting. Bye!")
            break

        emotions = tag_emotions(text)
        print_emotions_with_emoji(emotions)

if __name__ == "__main__":
    main()

