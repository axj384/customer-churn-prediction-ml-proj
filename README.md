# Customer Churn Prediction & Retention Analytics
**Target:** Data Science / Analytics Intern | **Stack:** Python, scikit-learn, SQL, Excel, Power BI

## Business question
Which customers are at higher risk of leaving, and how well can we predict churn using information available before the outcome?

## How to run
```bash
pip install -r requirements.txt
python analysis.py
```
Outputs: `outputs/model_metrics.csv`, `outputs/test_predictions.csv`, `figures/confusion_matrix.png`, `outputs/churn.db`.

## Modeling approach
Stratified 80/20 train-test split, preprocessing pipeline with one-hot encoding, logistic regression and random forest; report accuracy, precision, recall, F1 and ROC-AUC. Compare against a majority-class baseline. No customer ID used as a predictor.

## Power BI layout
Cards: Churn Rate, Customers, High-Risk Customers. Visuals: Churn by Contract, Tenure Band, Support Tickets, and Model Score Distribution.

**Limitations:** Synthetic labels are generated from a known formula, so performance is not evidence of real-world churn prediction. Predictions are associations, not causal retention uplift.
