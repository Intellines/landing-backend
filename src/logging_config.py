import logging
import os
from logging import Logger

import logfire
from dotenv import load_dotenv

load_dotenv()
LOGFIRE_TOKEN: str = os.getenv("LOGFIRE_TOKEN", "")

logger: Logger = logging.getLogger("backend")
logger.setLevel(logging.DEBUG)
logfire.configure(
    token=LOGFIRE_TOKEN,
    service_name="backend",
    send_to_logfire=True,
    console=logfire.ConsoleOptions(min_log_level="debug"),
    distributed_tracing=False,  # Disable trace propagation
)

logger.addHandler(logfire.LogfireLoggingHandler(level="DEBUG"))

if __name__ == "__main__":
    # logfire.info("Hello, {place}!", place="World")
    logger.info("Hello there!")
