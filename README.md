
## 📌 Objective
The objective of this task was to build a predictive analytics model using AI tools to classify breast cancer cases as malignant or benign, simulating issue prioritization in a resource allocation context.

## 📊 Dataset
The dataset used was the **Breast Cancer Wisconsin dataset**, accessed via the built-in `sklearn.datasets` module. It contains 569 samples with 30 numerical features describing cell nuclei characteristics from digitized images of fine-needle aspirates.

## 🛠️ Tools & Libraries
- Python 3.x
- Pandas 2.2.2
- Scikit-learn 1.5.0
- Matplotlib 3.9.0
- Seaborn 0.13.2
- Joblib 1.4.2

## 📂 Project Structure
AI_SoftwareEngineering_Assignment/
├── Task1_CodeCompletion/
│   ├── manual_sort.py
│   ├── copilot_sort.py
│   └── analysis.md
├── Task2_AutomatedTesting/
│   ├── login_test.side  (if using Selenium IDE)
        login.html
│   ├── screenshots/
│   │   └── result.png
│   └── summary.md
├── Task3_PredictiveAnalytics/
│   ├── predictive_model.ipynb
│   └── metrics.txt
        app.py
└── Ethical_Reflection/
    └── reflection.md


## ⚙️ Workflow Summary
1. Loaded the Breast Cancer dataset.
2. Performed data preprocessing by splitting features and labels.
3. Split data into training and test sets (70:30 ratio).
4. Trained a **Random Forest Classifier**.
5. Evaluated the model using **Accuracy** and **F1-Score**.
6. Saved the performance metrics and the trained model.

## 📊 Performance Metrics
Sample metrics (from `metrics.txt`):
Accuracy: 0.9710
F1-Score: 0.9707


📝 Notes
The trained model is saved as random_forest_model.pkl for future predictions.

No external dataset files are needed as the dataset is loaded via scikit-learn’s internal API.

Designed for Python virtual environment compatibility.
