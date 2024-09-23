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

# Define the order for each demographic variable
educ_order = ['some_high_school', 'high_school_grad', 'some_college', 'college_grad_aa', 'college_grad_ba', 'professional_degree', 'masters', 'phd']
income_order = ['<10k', '10k-50k', '50k-100k', '100k-200k', '>200k']
ideology_order = ['extremely_liberal', 'liberal', 'slightly_liberal', 'neutral', 'slightly_conservative', 'conservative', 'extremely_conservative', 'no_opinion']

# Histogram of annotations per annotator
annotations_per_annotator = df['annotator_id'].value_counts()
plt.figure(figsize=(10, 6))
counts, bins, patches = plt.hist(annotations_per_annotator, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Annotations per Annotator')
plt.xlabel('Number of Annotations')
plt.ylabel('Frequency')

# Annotate histogram bars
for count, bin_edge in zip(counts, bins[:-1]):
    plt.text(bin_edge, count, f'{int(count)}', ha='center', va='bottom')

plt.savefig('images/annotations_per_annotator.png')
plt.close()

# Distinct labels and their types
label_columns = ['sentiment', 'respect', 'insult', 'humiliate', 'status', 'dehumanize', 'violence', 'genocide', 'attack_defend']
distinct_labels = {col: df[col].nunique() for col in label_columns}

# Histogram of label values
for column in label_columns:
    plt.figure(figsize=(10, 6))
    counts, bins, patches = plt.hist(df[column].dropna(), bins=[-0.5, 0.5, 1.5, 2.5, 3.5, 4.5], color='lightgreen', edgecolor='black')
    plt.title(f'Histogram of {column} Values')
    plt.xlabel(f'{column}')
    plt.ylabel('Frequency')

    # Annotate histogram bars
    for count, bin_edge in zip(counts, bins[:-1]):
        plt.text(bin_edge + 0.5, count, f'{int(count)}', ha='center', va='bottom')

    plt.savefig(f'images/{column}_histogram.png')
    plt.close()

# Demographic features for annotators (unique values)
demographic_columns = ['annotator_gender', 'annotator_educ', 'annotator_income', 'annotator_ideology']
demographic_stats = {col: df.drop_duplicates(subset=['annotator_id'])[col].value_counts().to_dict() for col in demographic_columns}

# Save analysis results to a text file
with open('analysis_results.txt', 'w') as f:
    f.write(f"Number of annotators: {num_annotators}\n")
    f.write(f"Number of annotations: {num_annotations}\n\n")
    
    f.write("Distinct labels per category:\n")
    for label, count in distinct_labels.items():
        f.write(f"  {label}: {count}\n")
    
    f.write("\nDemographic features:\n")
    for column, stats in demographic_stats.items():
        f.write(f"{column}:\n")
        for category, count in stats.items():
            f.write(f"  {category}: {count}\n")
        f.write("\n")

# Plot demographic features with the correct order for the specified categories
for column, stats in demographic_stats.items():
    plt.figure(figsize=(10, 6))
    
    # Sort the bars based on the specific order for each demographic category
    if column == 'annotator_educ':
        ordered_stats = {key: stats.get(key, 0) for key in educ_order}
    elif column == 'annotator_income':
        ordered_stats = {key: stats.get(key, 0) for key in income_order}
    elif column == 'annotator_ideology':
        ordered_stats = {key: stats.get(key, 0) for key in ideology_order}
    else:
        # Default order for other demographic variables
        ordered_stats = stats

    bars = plt.bar(ordered_stats.keys(), ordered_stats.values(), color='skyblue', edgecolor='black')

    # Annotate each bar with its value
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, f'{int(yval)}', ha='center', va='bottom')

    plt.title(f'Demographic Distribution: {column}')
    plt.xlabel(column)
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f'images/{column}_distribution.png')
    plt.close()
