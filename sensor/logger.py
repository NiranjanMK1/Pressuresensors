import logging
import os
from datetime import datetime


LOG_FILE_NAME = F"{datetime.now().strftime('%m%d%Y__%H%M%S')}.log"

LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")

#create folder if not available 
os.makedirs(LOG_FILE_DIR, exist_ok= True)
 
 #log file path
logging.basicConfig(
    filename= LOG_FILE_NAME,
    format = "[%(asctime)s] %(lineno)d%(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
 )
