from confluent_kafka import Consumer
from dotenv import load_dotenv
from logger.logger import Logger
import os

load_dotenv()
logger = Logger(name=__name__, format="%(asctime)s - %(levelname)s - %(message)s")


def main():
    consumer_kafka = Consumer(
        {
            "bootstrap.servers": os.environ.get("SERVER"),
            "group.id": "python-consumer",
            "auto.offset.reset": "earliest",
        }
    )
    logger.info("Kafka Consumer has been initiated...")
    logger.info(f"Available topics to consume: {consumer_kafka.list_topics().topics}")
    consumer_kafka.subscribe([os.environ.get("PRODUCER_NAME")])

    while True:
        msg = consumer_kafka.poll(1)
        if msg is None:
            continue
        if msg.error():
            logger.error(f"Error: {msg.error()}")
            continue
        data = msg.value().decode("utf-8")
        logger.info(data)
    consumer_kafka.close()


if __name__ == "__main__":
    main()
