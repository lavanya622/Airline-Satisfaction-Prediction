# ✈️ Airline Satisfaction Prediction

## 📌 Project Overview

Airline Satisfaction Prediction is an end-to-end Machine Learning project that predicts whether an airline passenger is likely to be satisfied with their overall travel experience.

The project uses passenger details, travel information, service ratings, and flight delay information to train a **Logistic Regression** classification model.

The trained model is saved using **Joblib** and integrated with a **Streamlit** application, allowing users to enter passenger details and receive a satisfaction prediction through an interactive frontend.

---

## 🎯 Objective

The main objective of this project is to build a complete Machine Learning workflow for airline passenger satisfaction prediction.

The project covers the complete process from dataset preparation and preprocessing to model training, evaluation, model saving, and frontend-based prediction.

---

## 📊 Dataset

The dataset contains airline passenger information, travel details, service ratings, and flight delay information.

### Features

* Gender
* Customer Type
* Age
* Type of Travel
* Class
* Flight Distance
* Inflight WiFi Service
* Departure/Arrival Time Convenient
* Ease of Online Booking
* Gate Location
* Food and Drink
* Online Boarding
* Seat Comfort
* Inflight Entertainment
* On-board Service
* Leg Room Service
* Baggage Handling
* Check-in Service
* Cleanliness
* Departure Delay in Minutes
* Arrival Delay in Minutes

### Target

* `satisfaction`

The target represents the passenger's satisfaction with the airline experience.

---

## 🤖 Machine Learning Algorithm

### Logistic Regression

**Logistic Regression** is used as the classification algorithm for predicting airline passenger satisfaction.

The model learns patterns from passenger and flight-related features and predicts the satisfaction class for new passenger inputs.

---

## 🔄 Machine Learning Workflow

The project follows a standard Machine Learning workflow:

```text
Dataset
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Feature & Target Separation
   ↓
Train-Test Split
   ↓
Logistic Regression
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Save Model using Joblib
   ↓
Streamlit Frontend
   ↓
User Input
   ↓
Satisfaction Prediction
```

---

## 🧠 Machine Learning Steps

### 1. Import Libraries

Required Python libraries are imported for data processing, analysis, model training, evaluation, and model saving.

### 2. Load Dataset

The airline passenger satisfaction dataset is loaded using Pandas.

### 3. Data Preprocessing

The dataset is prepared for Machine Learning by converting categorical information into numerical representations.

### 4. Exploratory Data Analysis

The dataset is analyzed to understand passenger characteristics, service ratings, travel information, and satisfaction patterns.

### 5. Feature Engineering

Categorical features are converted into numerical values so that they can be used by the Logistic Regression model.

### 6. Define Features and Target

The input features are separated from the target variable.

```text
X → Passenger and flight features
y → Satisfaction
```

### 7. Train-Test Split

The dataset is divided into training and testing data.

The training data is used to train the model, while the testing data is used to evaluate its performance on unseen data.

### 8. Model Training

A Logistic Regression model is trained using the prepared training dataset.

### 9. Model Evaluation

The trained model is evaluated using classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* Classification Report

### 10. Model Saving

After training, the model is saved using Joblib.

```text
logistics_regression.pkl
```

The saved model can then be loaded by the Streamlit application without retraining the model.

---

## 💾 Model Integration

The saved Logistic Regression model is loaded in `app.py`.

The application collects passenger information from the user and creates the required input features.

The input is then passed to the saved model to generate the prediction.

```text
User Input
    ↓
Streamlit Application
    ↓
Saved Logistic Regression Model
    ↓
Prediction
    ↓
Satisfaction Result
```

The application also displays model confidence when probability information is available.

---

## 🖥️ Streamlit Frontend

The project includes an interactive Streamlit frontend.

Users can enter:

### Passenger Details

* Gender
* Customer Type
* Age

### Travel Details

* Type of Travel
* Class
* Flight Distance

### Service Ratings

* Inflight WiFi Service
* Departure/Arrival Time Convenient
* Ease of Online Booking
* Gate Location
* Food and Drink
* Online Boarding
* Seat Comfort
* Inflight Entertainment
* On-board Service
* Leg Room Service
* Baggage Handling
* Check-in Service
* Cleanliness

### Flight Delay Details

* Departure Delay
* Arrival Delay

After submitting the form, the application generates the passenger satisfaction prediction.

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Logistic Regression

### Data Processing

* Pandas
* NumPy

### Model Saving

* Joblib

### Frontend

* Streamlit

---

## 📂 Project Structure

```text
airline-satisfaction-prediction/
│
├── dataset.csv
│
├── app.py
│
├── logistics_regression.pkl
│
├── requirements.txt
│
└── README.md
```

---

## 📦 Requirements

The project dependencies are maintained in `requirements.txt`.

Main libraries include:

* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Joblib

---

## ▶️ How to Run the Project

### Step 1: Open the Project

Open the project folder in VS Code or your preferred Python environment.

### Step 2: Install Dependencies

Open the terminal inside the project folder and run:

```bash
pip install -r requirements.txt
```

### Step 3: Verify the Saved Model

Make sure the trained model file is available:

```text
logistics_regression.pkl
```

### Step 4: Run the Streamlit Application

Run:

```bash
streamlit run app.py
```

### Step 5: Open the Application

After executing the command, Streamlit will start the application and display a local URL in the terminal.

Open that URL in your browser.

### Step 6: Enter Passenger Information

Fill in the passenger details, travel information, service ratings, and delay information.

### Step 7: Predict Satisfaction

Click:

**Predict Satisfaction**

### Step 8: View the Result

The application displays the predicted passenger satisfaction:

* **Likely satisfied**
* **Likely neutral or dissatisfied**

When supported by the saved model, the application also displays the model confidence.

---

## 🌟 Key Features

* End-to-end Machine Learning workflow
* Logistic Regression classification
* Airline passenger satisfaction prediction
* Data preprocessing
* Feature engineering
* Train-test split
* Model evaluation
* Joblib model serialization
* Interactive Streamlit frontend
* Real-time prediction using the saved model
* Model confidence display

---

## 🔮 Future Enhancements

* Compare multiple classification algorithms
* Perform hyperparameter tuning
* Improve feature engineering
* Add model explainability
* Add model monitoring
* Dockerize the application
* Deploy the application to the cloud
* Add automated model retraining
* Develop an API-based backend

---

## 📌 Conclusion

This project demonstrates an end-to-end Machine Learning application for airline passenger satisfaction prediction.

It covers the complete journey from dataset preparation and preprocessing to Logistic Regression model training, evaluation, model serialization using Joblib, and integration with an interactive Streamlit frontend.

The project provides practical experience in developing and deploying a Machine Learning model as an interactive application.
