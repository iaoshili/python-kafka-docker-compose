from kafka import KafkaConsumer

consumer = KafkaConsumer('foobar', bootstrap_servers='kafka:9093')
for msg in consumer:
    print(msg)
