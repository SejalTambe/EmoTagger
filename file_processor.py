# file_processor.py

import csv
import json
import os
import pandas as pd
from .tagger import tag_emotions_multilingual


def process_csv(file_path, text_column, output_path=None):
    df = pd.read_csv(file_path)

    if text_column not in df.columns:
        raise ValueError(f"Column '{text_column}' not found in CSV.")

    results = []
    for _, row in df.iterrows():
        text = str(row[text_column])
        result = tag_emotions_multilingual(text)
        results.append({
            'original_text': result['original_text'],
            'translated_text': result['translated_text'],
            'language': result['language'],
            'emotions': ', '.join(result['emotions']),
            'emojis': ' '.join(result['emojis'])
        })

    result_df = pd.concat([df, pd.DataFrame(results)], axis=1)

    if output_path:
        result_df.to_csv(output_path, index=False)
        print(f"✅ Results exported to {output_path}")

    return result_df


def process_json(file_path, text_key, output_path=None):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    results = []
    for entry in data:
        text = str(entry.get(text_key, ''))
        result = tag_emotions_multilingual(text)
        entry.update({
            'translated_text': result['translated_text'],
            'language': result['language'],
            'emotions': result['emotions'],
            'emojis': result['emojis']
        })
        results.append(entry)

    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"✅ Results exported to {output_path}")

    return results
