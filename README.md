# EmoTagger

**EmoTagger** is a simple Python library that detects emotions in text using a pre-trained AI model from Hugging Face.

---

### 🚀 Features
- Detects multiple emotions in one sentence
- Uses state-of-the-art transformer model (`distilroberta-base`)
- Easy to use with just a single function

---

### 📦 Installation

```bash
pip install transformers torch

# Example
from emotagger import tag_emotions_ai

text = "I feel nervous but excited about the result!"

result = tag_emotions_ai(text)

print("🎯 AI Detected Emotions:")
for emotion in result:
    print(f"- {emotion['label']} ({emotion['score']:.2f})")

# Output (example):
# - fear (0.65)
# - joy (0.30)
# - neutral (0.05)
