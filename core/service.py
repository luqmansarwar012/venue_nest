from dotenv import load_dotenv
import logging
import os


# Environment Configuration

load_dotenv()


def get_env_variable(key: str, default: str = None) -> str:
    value = os.getenv(key, default)
    if value is None:
        raise EnvironmentError(f"Missing required environment variable: {key}")
    return value


# Logger Configuration

logger = logging.getLogger("APP LOGGER")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(name)10s - %(levelname)s - %(message)s")

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)
