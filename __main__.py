# __main__.py

import argparse
import os
from . import tag_emotions_multilingual
from .file_processor import process_csv, process_json

def main():
    parser = argparse.ArgumentParser(description="EmoTagger - Multilingual Emotion Detection")
    parser.add_argument('--text', help="Single sentence input for emotion tagging")
    parser.add_argument('--file', help="Input CSV or JSON file path")
    parser.add_argument('--column', help="Column name for text in CSV or key for JSON")
    parser.add_argument('--output', help="Optional output file path")
    args = parser.parse_args()

    if args.text:
        result = tag_emotions_multilingual(args.text)
        print("🗣️ Original Text:", result['original_text'])
        print("🌐 Language:", result['language'])
        print("🔤 Translated Text:", result['translated_text'])
        print("💬 Emotions:", ', '.join(result['emotions']))
        print("😊 Emojis:", ' '.join(result['emojis']))


    elif args.file and args.column:
     ext = os.path.splitext(args.file)[-1].lower()
    if ext == '.csv':
        df = process_csv(args.file, args.column, args.output)
        print("✅ Processed CSV preview:\n")
        print(df.head().to_string(index=False))  # 👈 Print a few results
    elif ext == '.json':
        results = process_json(args.file, args.column, args.output)
        print("✅ Processed JSON entries:", len(results))
    else:
        print("❌ Unsupported file type. Use .csv or .json")
