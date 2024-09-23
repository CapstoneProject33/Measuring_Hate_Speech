import pandas as pd
import matplotlib.pyplot as plt
import os

# Create an 'images' directory if it doesn't exist
if not os.path.exists('images'):
    os.makedirs('images')

# Load the dataset
df = pd.read_csv('data/Measuring Hate Speech.csv')

# Number of annotators
num_annotators = df['annotator_id'].nunique()

# Number of annotations
num_annotations = len(df)

# Histogram of annotations per annotator
annotations_per_annotator = df['annotator_id'].value_counts()
plt.figure(figsize=(10, 6))
plt.hist(annotations_per_annotator, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Annotations per Annotator')
plt.xlabel('Number of Annotations')
plt.ylabel('Frequency')
plt.savefig('images/annotations_per_annotator.png')
plt.close()

# Distinct labels and their types
label_columns = ['sentiment', 'respect', 'insult', 'humiliate', 'status', 'dehumanize', 'violence', 'genocide', 'attack_defend']
distinct_labels = {col: df[col].nunique() for col in label_columns}

# Histogram of label values
for column in label_columns:
    plt.figure(figsize=(10, 6))
    df[column].hist(bins=20, color='lightgreen', edgecolor='black')
    plt.title(f'Histogram of {column} Values')
    plt.xlabel(f'{column}')
    plt.ylabel('Frequency')
    plt.savefig(f'images/{column}_histogram.png')
    plt.close()

# Demographic features for annotators
demographic_columns = ['annotator_gender', 'annotator_educ', 'annotator_income', 'annotator_ideology']
demographic_stats = {col: df[col].value_counts().to_dict() for col in demographic_columns}

# Save demographic stats to a text file
with open('demographic_stats.txt', 'w') as f:
    for column, stats in demographic_stats.items():
        f.write(f"{column}:\n")
        for category, count in stats.items():
            f.write(f"  {category}: {count}\n")
        f.write("\n")