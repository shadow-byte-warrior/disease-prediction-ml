# Intelligent Disease Prediction System Using Machine Learning

## 📌 Project Overview

This project implements an **Intelligent Disease Prediction System** that predicts the most probable disease based on user-selected symptoms.  
It uses **Machine Learning classification algorithms** and a **consensus-based prediction approach** to improve reliability.

The system is developed for **academic demonstration purposes** and is not intended to replace professional medical diagnosis.

---

## 🎯 Key Features

- Symptom-based disease prediction  
- Machine Learning models:
  - Decision Tree
  - Random Forest
  - Naive Bayes
- Majority voting (consensus) for final prediction  
- Flask Web Application  
- Streamlit Web Application  
- Tkinter / Jupyter GUI support  
- Model persistence using Pickle  
- GitHub version-controlled source code  

---

## 🧠 Machine Learning Workflow

1. Load Training and Testing datasets  
2. Convert symptoms into binary feature vectors  
3. Train ML classifiers  
4. Save trained models using Pickle  
5. Accept user-selected symptoms  
6. Predict disease using all classifiers  
7. Apply majority voting for final output  

---

## 🗂 Project Structure

disease-prediction-ml/
│
├── Training.csv # Training dataset
├── Testing.csv # Testing dataset
│
├── disease_prediction_model.ipynb # Model training notebook
├── predict_disease.ipynb # Prediction & GUI notebook
├── test_gui.ipynb # GUI testing notebook
│
├── dt_model.pkl # Decision Tree model
├── rf_model.pkl # Random Forest model
├── nb_model.pkl # Naive Bayes model
├── symptom_list.pkl # Symptom feature list
│
├── flask_app.py # Flask Web Application
├── streamlit_app.py # Streamlit Web Application
│
├── templates/
│ └── index.html # Flask UI Template
│
└── README.md

yaml
Copy code

---

## 💻 Technologies Used

- Python  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- Streamlit  
- Pickle  
- HTML / CSS  
- Git & GitHub  

---

## 🚀 How to Run the Project

### 1️⃣ Install Required Libraries

pip install pandas numpy scikit-learn flask streamlit

yaml
Copy code

---

### 2️⃣ Run Flask Web Application

python flask_app.py

r
Copy code

Open in browser:

http://127.0.0.1:5000

yaml
Copy code

---

### 3️⃣ Run Streamlit Web Application

streamlit run streamlit_app.py

yaml
Copy code

---

### 4️⃣ Run Jupyter Notebooks

jupyter notebook

yaml
Copy code

Open:
- `disease_prediction_model.ipynb`
- `predict_disease.ipynb`

---

## 📊 Output

- User selects symptoms  
- System predicts disease  
- Final result shown using majority voting  

---

## ⚠ Disclaimer

This project is developed **strictly for academic purposes**.  
It is **not a medical diagnostic tool**.

---

## 👨‍💻 Author

**Arun Pandian**  
GitHub: https://github.com/shadow-byte-warrior
