import logging
from logging.handlers import RotatingFileHandler
import sys

# Logger principal
logger = logging.getLogger("laudopro")
logger.setLevel(logging.INFO)

# Handler de console
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
console_handler.setFormatter(console_formatter)
logger.addHandler(console_handler)

# Handler de arquivo com rotação
file_handler = RotatingFileHandler("logs/laudopro.log", maxBytes=10_000_000, backupCount=5)
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
