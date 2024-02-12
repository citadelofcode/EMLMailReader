from enum import Enum


class TransferEncoding(Enum):
    """Enumeration to represent the different content encoding methods supported."""
    BASE64 = 1
    SEVEN_BIT = 2
    EIGHT_BIT = 3
    QUOTED_PRINTABLE = 4


class EntityType(Enum):
    """Enumeration to represent the different MIME entity types supported."""
    ATTACHMENT = 1
    TEXT = 2
    MIME_PART = 3


class DispositionType(Enum):
    """Enumeration to represent the different content disposition types supported in MIME."""
    ATTACHMENT = 1
    INLINE = 2


class LoggingLevel(Enum):
    """Enumeration containing the different levels of logging available for a module."""
    DEBUG = 1
    INFO = 2
    ERROR = 3
    CRITICAL = 4


class LoggingMode(Enum):
    """Enumeration containing the different modes of logging available for a module."""
    CONSOLE = 1
    FILE = 2
