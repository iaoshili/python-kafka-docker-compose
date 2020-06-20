# python-kafka-docker-compose

## Workflow

- docker-compose up
- docker exec -it demo python consumer.py
- docker exec -it demo python producer.py

## Command line CLI
- `docker exec -it kafka bash`
- `cd $KAFKA_HOME/bin`
- run your command (e.x. kafka-topics.sh --describe --topic topic --zookeeper $ZK)

Reference:
- https://medium.com/big-data-engineering/hello-kafka-world-the-complete-guide-to-kafka-with-docker-and-python-f788e2588cfc
- http://wurstmeister.github.io/kafka-docker/
- https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html
