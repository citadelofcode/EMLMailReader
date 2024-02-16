class InvalidEncodingError(Exception):
    """A custom exception class to report Invalid Encoding errors."""
    def __init__(self, EncodedValue: str = str()):
        self.EncodedValue = EncodedValue
        self.Message = "Invalid encoding used"

    def __str__(self):
        if self.EncodedValue == str():
            return f"Error occurred on line {self.__traceback__.tb_lineno}:> {self.Message}."
        else:
            return f"Error occurred on line {self.__traceback__.tb_lineno}:> {self.Message}.\nEncoded string causing the error: {self.EncodedValue}."


class FileMissingError(Exception):
    """A custom exception class to report when file is missing at the specified location."""
    def __init__(self, filePath: str):
        self.filePath = filePath

    def __str__(self):
        return f"Error occurred on line {self.__traceback__.tb_lineno}:> File - '{self.filePath}' is either not available at location or not accessible."


class IncompleteHeaderError(Exception):
    """A custom exception to report incomplete headers present in the EML file."""
    def __init__(self, HeaderValue: str, LineInFile: int):
        self.InvalidHeaderValue = HeaderValue
        self.LineInFile = LineInFile

    def __str__(self):
        return f"Error occurred on line {self.__traceback__.tb_lineno}:> Incomplete header found on line {self.LineInFile} of EML File."


class FolderNotAvailableError(Exception):
    """A custom exception class to report when folder is not available at the specified location."""
    def __init__(self, folderPath: str):
        self.folderPath = folderPath

    def __str__(self):
        return f"Error occurred on line {self.__traceback__.tb_lineno}:> Folder - '{self.folderPath}' is either not accessible or does not exist.."
