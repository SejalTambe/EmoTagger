from emotagger import tag_emotions

text = "Feeling sad because you are alone."
result = tag_emotions(text)

print("🎯 AI Detected Emotions:")
for emotion in result:
    print(f"- {emotion['label']} ({emotion['score']:.2f})")
