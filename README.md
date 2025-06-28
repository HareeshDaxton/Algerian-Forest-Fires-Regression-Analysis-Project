# Algerian Forest Fires – Regression Analysis Project

This project presents a complete **Machine Learning Regression pipeline** to analyze and predict forest fire behavior using weather and fire index data from Algeria. From **data preprocessing and EDA** to **model training with Ridge Regression** and **deployment readiness via Flask and AWS Elastic Beanstalk**, this solution follows a professional and production-oriented workflow.

---

## 🗂️ Project Directory Structure

├── .ebextensions/ # AWS deployment configs (Elastic Beanstalk)  
├── model/  
│   ├── ridge.pkl               # Serialized Ridge Regression model  
│   └── scaler.pkl              # StandardScaler object used during training  
│  
├── NotBooks/  
│   ├── raw_dataset/  
│   │   └── Raw_Algerian_forest_fires_dataset_UPDATE.csv  
│   ├── cleaned_dataset/  
│   │   └── Cleaned_Algerian_forest_fires_dataset.csv  
│   ├── ridge_EDA_FE.ipynb      # Exploratory Data Analysis & Feature Engineering  
│   └── ridge_MAIN.ipynb        # Model training and evaluation  
│  
├── application.py              # Flask app for inference  

---

## 📚 Dataset Overview

- **Source**: [UCI ML Repository – Algerian Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset)  
- **Context**: This dataset provides weather and fire index data collected from two Algerian regions during June–September.  
- **Files Included**:  
  - Raw_Algerian_forest_fires_dataset_UPDATE.csv – Original dataset  
  - Cleaned_Algerian_forest_fires_dataset.csv – Cleaned, preprocessed version used for modeling  

### 🔑 Features Used

- **Environmental**: Temperature, Relative Humidity (RH), Wind, Rain  
- **Fire Weather Indices**: FFMC, DMC, DC, ISI  
- **Target**: Classes → encoded to binary: 1 (fire), 0 (not fire)  

---

## 🔄 End-to-End Workflow

### 📥 1. Data Loading & Cleaning  
- Combined datasets from both regions  
- Removed null values and fixed inconsistent entries  
- Cleaned labels and standardized formatting  

### 📊 2. EDA & Feature Engineering  
- **Visualized** distributions, pairplots, and correlation matrices  
- **Detected and handled** outliers  
- Applied **feature scaling** using StandardScaler  

### 🔍 3. Model Development  
- Applied **Ridge Regression** to address multicollinearity and control overfitting  
- Model tuned and trained on scaled features  
- Serialized artifacts:  
  - ridge.pkl → Final trained model  
  - scaler.pkl → Scaler object used during preprocessing  

### 🧪 4. Evaluation Metrics

| Metric | Value     |  
|--------|-----------|  
| R²     | ~0.87     |  
| RMSE   | Low       |  
| Regularization | Reduces overfitting |  

---

## 🖥️ API Deployment  
A lightweight **Flask API** has been created to serve the model.  

---

## 📡 API Endpoint  
**POST** `/predictdata`  

**Request Format (JSON):**  
```json
{
  "temperature": 29.6,
  "RH": 57,
  "wind": 18.0,
  "rain": 0.0,
  "ISI": 8.4
}
```

**Response:**  
```json
{
  "predicted_fire_occurrence": 0.85
}
```

---

## ☁️ AWS Deployment – Elastic Beanstalk

Deployment-ready via `.ebextensions/`.

### 🚀 Steps 

1. **Zip the entire `Project_Regressio/` folder**  
2. **Exclude unwanted system files and folders** such as:    
3. **Deploy using AWS Elastic Beanstalk Console or EB CLI**



 

