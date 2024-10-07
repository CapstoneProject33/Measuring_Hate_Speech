import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Load the CSV dataset
file_path = 'data/Measuring Hate Speech.csv'  # Update with your actual path
df = pd.read_csv(file_path)

# Map the columns as described
df['index'] = df['comment_id']
df['sentence1'] = df['text']
df['sentence2'] = 'Is this hate speech?'
df['label'] = df['hate_speech_score'].apply(lambda x: 1 if x > 0 else 0)

# Select only the columns needed for the TSV files
df_tsv = df[['index', 'sentence1', 'sentence2', 'label']]

# Split the data into train, test, and dev sets (80% train, 10% dev, 10% test)
train, test = train_test_split(df_tsv, test_size=0.2, random_state=42)
dev, test = train_test_split(test, test_size=0.5, random_state=42)

# Create the "data" directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Save the TSV files
train.to_csv('data/train.tsv', sep='\t', index=False)
dev.to_csv('data/dev.tsv', sep='\t', index=False)
test.to_csv('data/test.tsv', sep='\t', index=False)

print("Train, dev, and test TSV files created successfully in the 'data' directory.")
