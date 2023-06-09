from message_producer.message_producer import message_maker_user
from confluent_kafka import Producer, KafkaError
import time
from logger.logger import Logger
from typing import Dict, Any
from dotenv import load_dotenv
import os

load_dotenv()
logger = Logger(name=__name__, format="%(asctime)s - %(levelname)s - %(message)s")


def receipt_callback(err, msg):
    if err is not None:
        logger.error(f"Error: {err}")
    else:
        logger.info(
            f'Produced message on topic {msg.topic()} with value of {msg.value().decode("utf-8")}'
        )


def producer_maker(message: Dict[str, Any]):
    try:
        producer = Producer({"bootstrap.servers": os.environ.get("SERVER")})
        logger.info("Kafka Producer has been initiated...")
        producer.poll(1)
        producer.produce(
            os.environ.get("PRODUCER_NAME"),
            message.encode("utf-8"),
            callback=receipt_callback,
        )
        producer.flush()
        time.sleep(5)
    except KafkaError as e:
        logger.error(e)


if __name__ == "__main__":
    for i in range(int(os.environ.get("MESSAGE_NUMBER"))):
        producer_maker(message_maker_user())
