# 🚨 Real-Time Fraud Detection API using Kafka & Machine Learning

This project demonstrates a **real-time fraud detection system** using machine learning and **Kafka** for data streaming. It's designed to simulate a financial transaction pipeline, detecting potential credit card fraud on the fly.

## 📦 Project Structure

Fraud_dectection_project/
│
├── app/ # (Optional) Backend or API endpoints
├── kafka/
│ ├── producer.py # Simulates streaming transaction data into Kafka
│ └── consumer.py # Consumes the data and makes predictions
│
├── models/ # Trained machine learning model (if serialized)
├── notebooks/
│ └── dataset/
│ └── creditcard.csv # (Large file, excluded from GitHub)
├── Dockerfile # Docker configuration (optional)
├── docker-compose.yml # Kafka & Zookeeper setup
├── requirements.txt # Python dependencies
└── README.md 


---

## 🚀 Key Features

- 💡 **Streamed Data Simulation** using Kafka producers
- 🧠 **Machine Learning Model** (e.g., Logistic Regression / RandomForest) for fraud detection
- ⚙️ **Kafka Consumer** that performs real-time predictions
- 📊 Cleaned and preprocessed **credit card dataset**
- 🐳 Dockerized setup (optional)

---

## 📊 Dataset

We used the **[Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)**. It contains transactions made by European cardholders in September 2013.

> ❗ The dataset is not included in this repo due to GitHub's 100MB limit. You can download it from Kaggle and place it in:
>
> `notebooks/dataset/creditcard.csv`

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/EddiesEdit/Fraud-detection-api.git
cd Fraud-detection-api

