# Measuring Hate Speech Dataset Analysis

## Dataset Overview

This analysis is based on the "Measuring Hate Speech" dataset, represented in the "data/Measuring Hate Speech.csv" file.

## Key Statistics

### Annotators and Annotations

- **Number of annotators:** 7912
- **Total number of annotations:** 135556

### Annotations per Annotator

![Histogram of Annotations per Annotator](images/annotations_per_annotator.png)

The histogram above shows the distribution of annotations per annotator.

### Label Analysis

The dataset contains multiple labels representing different aspects of hate speech. Here are the distinct labels and their possible values:

- **Sentiment:** 1-5
- **Respect:** 1-5
- **Insult:** 1-5
- **Humiliate:** 1-5
- **Status:** 1-5
- **Dehumanize:** 1-5
- **Violence:** 1-5
- **Genocide:** 1-5
- **Attack/Defend:** 1-5

These labels are continuous numerical values. Here are the histograms for each label:

![Sentiment Histogram](images/sentiment_histogram.png)
![Respect Histogram](images/respect_histogram.png)
![Insult Histogram](images/insult_histogram.png)
![Humiliate Histogram](images/humiliate_histogram.png)
![Status Histogram](images/status_histogram.png)
![Dehumanize Histogram](images/dehumanize_histogram.png)
![Violence Histogram](images/violence_histogram.png)
![Genocide Histogram](images/genocide_histogram.png)
![Attack/Defend Histogram](images/attack_defend_histogram.png)

### Annotator Demographics

The dataset includes demographic information for annotators. Below are the counts for each category:

- **Annotator Gender:**
  - Female: 76370
  - Male: 57582
  - Non-binary: 985
  - Prefer not to say: 500
  - Self-describe: 119

- **Annotator Education:**
  - College Grad (BA): 50206
  - Some College: 35115
  - College Grad (AA): 18011
  - High School Grad: 14138
  - Masters: 12593
  - Professional Degree: 3042
  - PhD: 1562
  - Some High School: 872

- **Annotator Income:**
  - $10k-$50k: 56668
  - $50k-$100k: 52803
  - $100k-$200k: 17415
  - <$10k: 6429
  - \>$200k: 2138

- **Annotator Ideology:**
  - Liberal: 33812
  - Neutral: 23112
  - Slightly Liberal: 21333
  - Extremely Liberal: 17944
  - Conservative: 15628
  - Slightly Conservative: 15101
  - Extremely Conservative: 4544
  - No Opinion: 4055

Please refer to `analysis_results.txt` for more detailed demographic statistics.