from emotagger import tag_emotions_multilingual, EMOJI_MAP, translate_to_english
from datetime import datetime

print("🌍 EmoTagger CLI - Multilingual Emotion Detection")
print("Type your sentence (or type 'exit' to quit):")
print("🌐 Input can be in any language – automatic translation to English will be applied.\n")

results = []

while True:
    text = input("You: ").strip()
    if text.lower() == 'exit':
        break

    # 🔄 Translate to English first
    translated = translate_to_english(text)
    print(f"📝 Translated to English: {translated}")

    try:
        emotions = tag_emotions_multilingual(translated)
    except Exception as e:
        print(f"⚠️ Emotion detection error: {e}")
        continue

    print("🤖 Detected Emotions:")
    line = f"Original: {text}\nTranslated: {translated}\n"

    for emo in emotions:
        label = emo['label']
        emoji = EMOJI_MAP.get(label, '')
        score = emo['score']
        print(f"- {label} {emoji} ({score:.2f})")
        line += f"- {label} {emoji} ({score:.2f})\n"

    line += "\n"
    results.append(line)

# ✅ Save results to file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"emotions_log_{timestamp}.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.writelines(results)

print(f"\n✅ Results saved to: {filename}")
