import os
import sys
import logging
# defing the logging string format
# level name is information logging
# module is which file is running 
# what message is being logged

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


log_dir = "logs"
# to create the log file
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir,exist_ok=True)

# handlers to log to both file and console
logging.basicConfig(level=logging.INFO, format=logging_str, handlers=[logging.FileHandler(log_filepath),logging.StreamHandler(sys.stdout)])


logger = logging.getLogger("textsummarizerlogger")