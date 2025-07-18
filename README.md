🚀 Fraud Detection API with Real-Time Streaming

An end-to-end machine learning deployment project that exposes a fraud detection model via a FastAPI REST API, containerizes the service using Docker, and integrates real-time streaming using Apache Kafka.

📌 Project Overview
You're a machine learning engineer at a fintech startup. Your team has built a fraud detection model and needs to:

✅ Serve it through a REST API (FastAPI)
✅ Containerize it for scalability (Docker)
✅ Stream real-time transaction data (Kafka)
✅ Make live fraud predictions and return results
✅ Monitor the system and scale it in production

This project demonstrates a modern MLOps workflow, from model training to real-time serving and streaming.

📁 Project Structure

Fraud-detection-api/
│
├── app/                 # FastAPI application code
├── kafka/               # Kafka producer/consumer scripts
├── models/              # Serialized ML model (.pkl)
├── notebooks/           # Data exploration & training notebooks
│
├── Dockerfile           # Docker container definition
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
