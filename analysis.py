import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Load the dataset
df = pd.read_csv('Measuring Hate Speech.csv')

# Create a directory for saving images
if not os.path.exists('images'):
    os.makedirs('images')

# 1. Number of annotators
num_annotators = df['annotator_id'].nunique()
print(f'Number of annotators: {num_annotators}')

# 2. Number of annotations
num_annotations = len(df)
print(f'Number of annotations: {num_annotations}')

# 3. Histogram of number of annotations per annotator
annotations_per_annotator = df['annotator_id'].value_counts()
plt.figure(figsize=(10, 6))
annotations_per_annotator.plot(kind='bar', color='skyblue')
plt.title('Histogram: Number of Annotations per Annotator')
plt.xlabel('Annotator ID')
plt.ylabel('Number of Annotations')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('images/annotations_per_annotator.png')
plt.close()

# 4. How many distinct labels there are, and classification type
labels = ['sentiment', 'respect', 'insult', 'humiliate', 'status', 'dehumanize', 'violence']
label_types = {}

for label in labels:
    unique_values = df[label].nunique()
    if unique_values == 2:
        label_types[label] = 'Binary'
    elif 2 < unique_values <= 20:
        label_types[label] = 'Categorical'
    else:
        label_types[label] = 'Continuous'

print(f'Distinct labels and classification types: {label_types}')

# 5. Histogram of label values
for label in labels:
    plt.figure(figsize=(10, 6))
    df[label].dropna().plot(kind='hist', bins=20, title=f'Histogram of {label}')
    plt.xlabel(label)
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig(f'images/{label}_histogram.png')
    plt.close()

# 6. Demographic features of annotators
demographic_features = [col for col in df.columns if col.startswith('annotator_') and 'id' not in col]
demographics_summary = {}

for feature in demographic_features:
    demographic_counts = df[feature].value_counts().head(20)  # Limit to top 20
    demographics_summary[feature] = demographic_counts
    # Plot demographic distribution
    plt.figure(figsize=(10, 6))
    demographic_counts.plot(kind='bar', color='lightgreen')
    plt.title(f'{feature.replace("_", " ").capitalize()} Distribution')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(f'images/{feature}_distribution.png')
    plt.close()

# Create a concise README.md with the results
with open('README.md', 'w') as f:
    f.write(f"# Hate Speech Dataset Analysis\n\n")
    f.write(f"### Number of Unique Annotators: {num_annotators}\n")
    f.write(f"### Total Number of Annotations: {num_annotations}\n")
    f.write(f"### Number of Distinct Labels: {len(labels)}\n")
    
    f.write(f"\n### Label Classification Types:\n")
    for label, label_type in label_types.items():
        f.write(f" - {label}: {label_type}\n")
    
    f.write("\n## Visualizations\n")
    f.write("![Annotations per Annotator](images/annotations_per_annotator.png)\n")
    
    for label in labels:
        f.write(f"![{label.capitalize()} Histogram](images/{label}_histogram.png)\n")
    
    f.write("\n## Annotator Demographics (Top 20 per category)\n")
    for feature, counts in demographics_summary.items():
        f.write(f"\n### {feature.replace('_', ' ').capitalize()}\n")
        f.write("| Category | Count |\n|:---------|------:|\n")
        for category, count in counts.items():
            f.write(f"| {category} | {count} |\n")
        f.write(f"![{feature.capitalize()} Distribution](images/{feature}_distribution.png)\n")
