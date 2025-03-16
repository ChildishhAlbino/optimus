import logging
from os import listdir
import time
import logging
from watchdog.observers import Observer
# from watchdog.events import LoggingEventHandler
from handler import OptimusFileSystemHandler

jobs_path = "/jobs"
files_path = "/files"

logger_config = logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

logger.info("I am Optimus Prime...")

jobs = listdir(jobs_path)
files = listdir(files_path)

logger.info(f"{jobs}, {files}")

event_handler = OptimusFileSystemHandler()
observer = Observer()
observer.schedule(event_handler, files_path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()