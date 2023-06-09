from faker import Faker
from random import choice
from typing import Dict, Any
import json
from logger.logger import Logger


logger = Logger(name=__name__, format="%(asctime)s - %(levelname)s - %(message)s")


def message_maker_user() -> Dict[str, Any]:
    """
    Return a simulate message

    Returns:
        Dict[str,Any]: Return a diccionary with dummy values
    """
    fake = Faker()

    street = fake.street_address()
    city = fake.city()
    country_code = fake.country_code()

    data = {
        "user_id": fake.random_int(),
        "user_name": fake.name(),
        "user_address": f"{street} | {city} | {country_code}",
        "platform": choice(["Mobile", "Laptop", "Tablet"]),
        "signup_at": str(fake.date_time_this_month()),
    }
    json_data = json.dumps(data)
    logger.info(f"Element generated **** {json_data} ****")
    return json_data
