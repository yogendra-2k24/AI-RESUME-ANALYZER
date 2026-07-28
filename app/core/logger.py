import logging

logger = logging.getLogger("resume_analyzer")

logger.setLevel(logging.INFO)

handler = logging.StreamHandler()

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setStream(formatter)

logger.addHandler(handler)