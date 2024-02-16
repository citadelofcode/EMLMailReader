import os
import logging
import datetime
from .Enumerations import LoggingMode, LoggingLevel
from .Custom_Exceptions import FolderNotAvailableError


class Logger:
    """
    A class to manage the configuration and generation of logs during EML file processing.
    """

    @staticmethod
    def set_configuration(logging_mode: LoggingMode, target_folder: str = str()) -> str:
        """
        A function to enable and setup configurations for logging.
        :param logging_mode: Denotes where the generated logs have to be stored or printed.
        :param target_folder: The target folder where the log file must be created. This parameter value must be provided only when 'logging_mode' is 'LoggingMode.FILE'.
        :returns: the complete path to the log file generated. If the 'logging_mode' is 'LoggingMode.CONSOLE', an empty string is returned.
        """
        complete_file_path = str()
        if logging_mode == LoggingMode.CONSOLE:
            logging.basicConfig(level=logging.DEBUG, datefmt="%Y-%m-%d %H-%M-%S", format="%(asctime)s %(name)s %(levelname)s %(lineno)d %(message)s")
        else:
            if target_folder != str() and os.path.exists(target_folder):
                _CurrentDateTime = datetime.datetime.now()
                file_name = f"EMLMailReader_Logs_{_CurrentDateTime.year}{_CurrentDateTime.month}{_CurrentDateTime.day}_{_CurrentDateTime.hour}{_CurrentDateTime.minute}{_CurrentDateTime.second}.log"
                complete_file_path = os.path.join(target_folder, file_name)
                logging.basicConfig(level=logging.DEBUG, datefmt="%Y-%m-%d %H-%M-%S", format="%(asctime)s %(name)s %(levelname)s %(message)s", encoding="utf-8", filename=complete_file_path)
            else:
                raise FolderNotAvailableError(target_folder)
        return complete_file_path

    @staticmethod
    def logentry(message: str, logging_level: LoggingLevel):
        """
        A function to create and print a new log message.
        :param message: Message to be logged.
        :param logging_level: The type of message that is being logged.
        :returns: no value(s).
        """
        if logging_level == LoggingLevel.INFO:
            logging.info(message)
        elif logging_level == LoggingLevel.ERROR:
            logging.error(message)
        elif logging_level == LoggingLevel.CRITICAL:
            logging.critical(message)
        else:
            logging.debug(message)
