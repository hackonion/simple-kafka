from typing import Any
import logging


class Logger:
    def __init__(
        self,
        name,
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    ) -> Any:
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter(format)
        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def debug(self, message) -> str:
        self.logger.debug(message)

    def info(self, message) -> str:
        self.logger.info(message)

    def warning(self, message) -> str:
        self.logger.warning(message)

    def error(self, message) -> str:
        self.logger.error(message)

    def critical(self, message) -> str:
        self.logger.critical(message)
