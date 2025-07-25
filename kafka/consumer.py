from kafka import KafkaConsumer
consumer = KafkaConsumer('voice_data', bootstrap_servers='localhost:9092')
for msg in consumer:
    print(msg.value.decode())
