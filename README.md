# python-kafka-docker-compose

## Workflow

- docker-compose up
- docker exec -it demo python consumer.py
- docker exec -it demo python producer.py

## Command line CLI
- `docker exec -it kafka bash`
- `cd $KAFKA_HOME/bin`
- run your command


### Useful CLI commands
Topic:
- Create a topic: `kafka-topics.sh --zookeeper $KAFKA_ZOOKEEPER_CONNECT --topic first_topic --create --partitions 3 --replication-factor 1`
- List all topics: kafka-topics.sh --zookeeper $KAFKA_ZOOKEEPER_CONNECT --list
- Describe the details of a topic: kafka-topics.sh --zookeeper $KAFKA_ZOOKEEPER_CONNECT --topic first_topic --describe

Producer: kafka-console-producer.sh --broker-list kafka:9093 --topic first_topic



Reference:
- https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc
- http://wurstmeister.github.io/kafka-docker/
- https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
