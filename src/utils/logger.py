import logging


logging.basicConfig(
    filename="../output/logs/rag.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


class Logger:

    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)