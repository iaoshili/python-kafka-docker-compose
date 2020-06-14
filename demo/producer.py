from kafka import KafkaProducer


def main():
    producer = KafkaProducer(bootstrap_servers='kafka:9093')
    producer.send('foobar', b'random string')
    producer.flush()

if __name__ == '__main__':
    main()
