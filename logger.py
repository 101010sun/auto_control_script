import logging
from pathlib import Path
from datetime import datetime

only_print = False

class CustomFormatter(logging.Formatter):
    def __init__(self, color: bool):
        super().__init__()
        self.color = color
        
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "[%(asctime)s]: %(message)s"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    FORMATS2 = {
        logging.DEBUG: format,
        logging.INFO: format,
        logging.WARNING: format,
        logging.ERROR: format,
        logging.CRITICAL: format
    }

    def format(self, record):
        if self.color:
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)
        log_fmt = self.FORMATS2.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)
    

class Logger():
    def __init__(self, fileName: str, file: str):
        self.fileName = fileName
        self.file = file
        self.logPath = Path('./' + fileName + '_' + 'log.log')
        
        self.logger = logging.getLogger(file)
        self.logger.setLevel(logging.INFO)
        f = logging.FileHandler(self.logPath, 'a', encoding='utf-8')
        f.setLevel(logging.INFO)
        f.setFormatter(CustomFormatter(False))
        self.logger.addHandler(f)
    

    def logMsg(self, msg: str, level:int = logging.INFO):
        timeStr = datetime.now().strftime('[%H:%M:%S]')
        if level == logging.INFO:
            print(f'{timeStr}: {msg} ({self.file}.py)')
            if not only_print: 
                self.logger.info(f'{msg} ({self.file}.py)')
        elif level == logging.WARNING:
            print(f'{timeStr}: {msg} ({self.file}.py)')
            if not only_print: 
                self.logger.warning(f'{msg} ({self.file}.py)')
        elif level == logging.ERROR:
            print(f'{timeStr}: {msg} ({self.file}.py)')
            if not only_print: 
                self.logger.warning(f'{msg} ({self.file}.py)')
        elif level == logging.CRITICAL:
            print(f'{timeStr}: {msg} ({self.file}.py)')
            if not only_print: 
                self.logger.critical(f'{msg} ({self.file}.py)')
        else:
            if not only_print: 
                self.logger.debug(msg)


    def setGlobalOnlyPrint(self, setting: bool):
        global only_print
        only_print = setting