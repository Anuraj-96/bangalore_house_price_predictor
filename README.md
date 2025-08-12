# 🏠 Bangalore House Price Predictor

An **end-to-end Machine Learning project** that predicts house prices in Bangalore using advanced regression techniques, deployed as an interactive **Streamlit web app**.  
This project demonstrates **data preprocessing, feature engineering, model tuning, and deployment**
---
## 📊 Project Highlights
- **Algorithm:** XGBoost Regressor with hyperparameter tuning (Randomized Search CV)
- **Feature Engineering:**
  - Smoothed Mean Encoding on **location** feature
  - Log transformation of **price** to normalize skew
- **Model Validation:** 5-fold cross-validation
- **Evaluation Metrics (Average across folds):**
  - **MAE:** 9.40
  - **MSE:** 222.11
  - **R² Score:** 0.918 (Strong predictive performance)
- **Dataset:** Real Bangalore housing data with features such as `location`, `total_sqft`, `bathrooms`, and `BHK`.

[🔗 Live Streamlit App](https://bangalorehousepricepredictor-qjoyzfngehevb2tddedfa9.streamlit.app/)

  
## 🛠 Tech Stack
- **Python**
- **Pandas**, **NumPy**, **Scikit-learn**
- **XGBoost**
- **Streamlit** for the web app

## 📌 Features
- Predict house prices instantly
- Simple, interactive Streamlit interface
- Trained on real Bangalore housing data
- Model: **XGBoost Regressor**
- Deployment ready

## 📈 Cross-Validation Results
| Fold | MAE   | MSE     | R²     |
|------|-------|---------|--------|
| 1    | 9.42  | 224.11  | 0.9211 |
| 2    | 9.03  | 221.92  | 0.9210 |
| 3    | 9.53  | 209.97  | 0.9227 |
| 4    | 9.55  | 219.34  | 0.9043 |
| 5    | 9.47  | 235.22  | 0.9222 |
**Average** | **9.40** | **222.11** | **0.9183** |

