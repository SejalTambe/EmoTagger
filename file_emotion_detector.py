import os
import pandas as pd
import json
from docx import Document
from emotagger import tag_emotions  # Make sure this is imported correctly

def read_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.csv':
        df = pd.read_csv(file_path)
        return df['text'].dropna().tolist()
    
    elif ext == '.xlsx':
        df = pd.read_excel(file_path)
        return df['text'].dropna().tolist()
    
    elif ext == '.json':
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [item['text'] for item in data if 'text' in item]
    
    elif ext == '.docx':
        doc = Document(file_path)
        return [para.text for para in doc.paragraphs if para.text.strip()]

    else:
        raise ValueError("Unsupported file type!")

def detect_emotions(texts):
    for i, text in enumerate(texts, start=1):
        result = tag_emotions(text)
        print(f"\n📄 Sentence {i}: {text}")
        print("🤖 Detected Emotions:")
        for emo in result:
            label = emo['label'].lower()
            score = emo['score']
            emoji = EMOJI_MAP.get(label, "❓")
            print(f"- {label} {emoji} ({score:.2f})")

# Optional: Add more if needed
EMOJI_MAP = {
    'joy': '😊', 'sadness': '😢', 'anger': '😠', 'fear': '😨',
    'disgust': '🤢', 'surprise': '😲', 'love': '❤️', 'neutral': '😐'
}

if __name__ == "__main__":
    file_path = input(r"📂 Enter the file path: ").strip()

    try:
        texts = read_file(file_path)
        detect_emotions(texts)
    except Exception as e:
        print("❌ Error:", e)
