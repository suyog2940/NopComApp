import logging
import inspect

class LogGen:
    @staticmethod
    # def loggen():
    #     logging.basicConfig(filename=".\\Logs\\automation.log",
    #                         format="%(asctime)s: %(levelname)s: %(message)s",
    #                         datefmt="%m/%d/%Y %I:%M:%S %p"
    #                         )
    #     logger = logging.getLogger()
    #     logger.setLevel(logging.INFO)
    #     return logger

    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(".\\Logs\\automation.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")
        logfile.setFormatter(format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


