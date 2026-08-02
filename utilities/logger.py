import logging
import os


class Logger:

    LOG_DIR = "reports/logs"
    LOG_FILE = "automation.log"

    @staticmethod
    def get_logger():

        # Create logs directory if it doesn't exist
        os.makedirs(Logger.LOG_DIR, exist_ok=True)

        # Get logger
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        # Prevent adding duplicate handlers
        if not logger.handlers:

            # File Handler
            file_handler = logging.FileHandler(
                Logger.get_log_file(),
                mode="a"
            )
            file_handler.setLevel(logging.INFO)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setLevel(logging.INFO)

            # Formatter
            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            # Apply formatter
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger

    @staticmethod
    def get_log_file():
        return os.path.join(Logger.LOG_DIR, Logger.LOG_FILE)