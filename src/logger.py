import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # create .log file
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)  # the path of log file
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(  # This line starts the configuration of the logging module
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

# test the logger
# if __name__ == "__main__":
#     logging.info("Logging has started!")
