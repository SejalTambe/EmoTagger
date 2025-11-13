from emotagger import tag_emotions_multilingual

texts = [
    "Estoy muy feliz hoy",                  # Spanish: I'm very happy today
    "Je suis triste",                       # French: I am sad
    "मैं बहुत गुस्से में हूँ",             # Hindi: I'm very angry
    "Ich bin nervös vor der Prüfung",      # German: I’m nervous before the exam
]

for sentence in texts:
    print(f"\n📝 Input: {sentence}")
    emotions = tag_emotions_multilingual(sentence)
    for emo in emotions:
        print(f"- {emo['label']} ({emo['score']:.2f})")
