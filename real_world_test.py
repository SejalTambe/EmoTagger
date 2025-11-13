# real_world_test.py
from emotagger import tag_emotions

sentences = [
    "I'm so happy to finally graduate!",
    "I can't believe this happened, I'm furious!",
    "She broke my trust. I feel betrayed.",
    "Looking forward to our trip next month!",
    "I regret not taking that opportunity."
]

for sentence in sentences:
    result = tag_emotions(sentence)
    print(f"📝 Input: {sentence}")
    for emo in result:
     emoji = emo.get("emoji", "🤖")  # fallback emoji
     print(f" - {emo['label']} {emoji} ({emo['score']:.2f})")


# real_world_test.py
from emotagger import tag_emotions
with open("C:/Users/Sejal/OneDrive/Documents/Positive feelings in English.docx")as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    if not line:
        continue
    result = tag_emotions(line)
    print(f"📝 Input: {line}")
    for emo in result:
        print(f" - {emo['label']} {emo['emoji']} ({emo['score']:.2f})")
    print()
