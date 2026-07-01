# phishing-detection
AI4ALL Group 13B - Phishing Website Detection Project

This project uses machine learning to detect phishing websites.
We train models to classify websites as phishing or legitimate.

## Datasets
We use two datasets to make our model more reliable.

- **Kaggle** (48 features): https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning
- **UCI** (30 features): https://archive.ics.uci.edu/dataset/327/phishing+websites

## Files
- `phishing.ipynb` - main notebook (all steps)
- `Phishing_Legitimate_full.csv` - Kaggle dataset (10,000 sites)
- `uci_raw.csv` - UCI raw data (11,055 rows, with duplicates)
- `uci_phishing.csv` - UCI clean data (5,849 rows, duplicates removed)
- `README.md` - this file

## Models
- Logistic Regression
- Decision Tree
- Random Forest (best)

## Results
Random Forest is the best model on both datasets.

| Model | Kaggle | UCI |
|-------|--------|-----|
| Logistic Regression | 95.20% | 91.28% |
| Decision Tree | 96.40% | 91.71% |
| Random Forest | 98.55% | 94.19% |

## How to Do Your Dataset (Team Template)
Each dataset follows the same 5 steps. Use the Kaggle notebook as your example.

1. **Explore** - load data, check shape, labels, missing values
2. **Clean** - remove duplicates, drop useless columns, save clean CSV
3. **Bias Analysis** - note time, source, feature, and balance bias
4. **Feature Selection + Visualization** - top features, heatmap, compare 3 models
5. **Split + Train** - 80/20 split (stratify), train Random Forest, show accuracy + confusion matrix

**Tips:**
- Clean BEFORE you train
- Check the label (1 = Phishing, 0 = Legitimate; some use -1/1)

## Data Sources (Credit)
- Kaggle Phishing Dataset: https://www.kaggle.com/datasets/shashwatwork/phishing-dataset-for-machine-learning
- UCI Phishing Websites (Mohammad, Thabtah & McCluskey): https://archive.ics.uci.edu/dataset/327/phishing+websites — licensed under CC BY 4.0