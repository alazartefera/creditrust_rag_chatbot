# src/preprocessing.py

import pandas as pd
import re
from tqdm import tqdm

tqdm.pandas()

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def load_and_preprocess(path_to_csv, output_path):
    df = pd.read_csv(path_to_csv)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    target_products = [
        "Credit card", 
        "Personal loan", 
        "Buy Now, Pay Later (BNPL)", 
        "Savings account", 
        "Money transfers"
    ]

    df = df[df["product"].isin(target_products)]
    df = df[df["consumer_complaint_narrative"].notna()]
    df["cleaned_narrative"] = df["consumer_complaint_narrative"].progress_apply(clean_text)
    df["word_count"] = df["cleaned_narrative"].apply(lambda x: len(x.split()))
    
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to: {output_path}")

if __name__ == "__main__":
    load_and_preprocess("data/raw/complaints.csv", "data/processed/filtered_complaints.csv")
