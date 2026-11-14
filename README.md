# Bangalore Home Price Prediction

A Machine Learning web application that predicts house prices in Bangalore based on property area, number of bedrooms (BHK), bathrooms, and location.

## 🌐 Live Demo

- **Frontend:** [https://bengalore-home-price-prediction-cli.vercel.app/]
- **Backend API:** [https://bengalore-home-price-prediction.onrender.com]

## 📌 Project Overview

The Bangalore Home Price Prediction project uses Machine Learning to estimate residential property prices in Bangalore.
Users can enter the property details, select a location, and get an estimated house price through an interactive web application.
The project demonstrates an end-to-end Machine Learning workflow, from data preprocessing and model training to API development and cloud deployment.

## ✨ Features

- Predicts house prices in Bangalore.
- Accepts property area in square feet.
- Supports different BHK configurations.
- Accepts the number of bathrooms.
- Provides multiple Bangalore location options.
- Displays estimated prices in Lakhs.
- Interactive web-based user interface.
- Deployed frontend and backend.

## 🛠️ Technologies Used

**Programming Language**
- Python
- JavaScript

**Machine Learning**
- Pandas
- NumPy
- Scikit-learn
- Jupyter Notebook

**Backend**
- Flask
- Flask-CORS
- Gunicorn

**Frontend**
- HTML
- CSS
- JavaScript
- jQuery

**Deployment**
- Render (Backend)
- Vercel (Frontend)
- GitHub (Version Control)

## 📂 Project Structure
```text
Bangalore-Home-Price-Prediction/
│
├── client/
│   ├── index.html
│   ├── app.css
│   └── app.js
│
├── model/
│   ├── model.ipynb
│   ├── banglore_home_prices_model.pickle
│   └── columns.json
│
├── server/
│   ├── server.py
│   ├── util.py
│   ├── requirements.txt
│   └── artifacts/
│       ├── banglore_home_prices_model.pickle
│       └── columns.json
│
└── README.md
```

## ⚙️ How It Works

1. The user enters property details such as area, BHK, bathrooms, and location.
2. The frontend sends these details to the Flask backend.
3. The backend processes the input and prepares the features.
4. The trained Machine Learning model predicts the house price.
5. The predicted price is returned to the frontend.
6. The estimated price is displayed to the user.

## 🚀 Run Locally
### 1. Clone the repository

```bash
git clone https://github.com/atul00005/Bengalore-Home-Price-Prediction
```

### 2. Navigate to the project directory

```bash
cd Bangalore-Home-Price-Prediction
```

### 3. Install backend dependencies

```bash
cd server
pip install -r requirements.txt
```

### 4. Run the Flask server

```bash
python server.py
```

### 5. Open the frontend

Open `client/index.html` in your browser.

Make sure the frontend API URL points to your local Flask server if you want to run the complete project locally.

## 🧠 Machine Learning Workflow

- Data Collection
- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Feature Engineering
- Model Training
- Model Evaluation
- Model Serialization using Pickle
- Flask API Integration
- Cloud Deployment

## 📈 Future Improvements

- Improve model accuracy.
- Add more property-related features.
- Compare multiple Machine Learning algorithms.
- Improve frontend design and user experience.
- Add prediction history.

## 👨‍💻 Author

**Atul Dadwal**

GitHub: [https://github.com/atul00005]

---

⭐ If you find this project useful, consider giving it a star!
