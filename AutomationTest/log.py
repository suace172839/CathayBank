import datetime
import logging
import os


class Log():
    def __init__(self):
        # Create log directory
        logDir = os.path.join(os.getcwd(), "log")
        if not os.path.exists(logDir):
            os.makedirs(logDir)
        
        # Create log with filename named by timestamp.
        currentDateTime = datetime.datetime.now().strftime("%Y_%m_%d_%H%M%S")
        logFileName = "AutomationTest_" + currentDateTime + ".log"
        logging.basicConfig(filename = os.path.join(logDir, logFileName), encoding = "utf-8", level = logging.DEBUG)
        self.log = logging.getLogger()
    
    def info(self, msg):
        self.log.info(msg)

    def warning(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)
