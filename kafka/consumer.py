# kafka/consumer.py
from kafka import KafkaConsumer
import requests
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='fraud-detector'
)

for message in consumer:
    transaction = message.value
    print("Received transaction:", transaction)

    # Send data to FastAPI for prediction
    response = requests.post("http://localhost:8000/predict", json=transaction)
    if response.ok:
        print("Prediction:", response.json())
    else:
        print("Failed to get prediction:", response.status_code)

