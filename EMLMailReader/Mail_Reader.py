import os
from .Mail_Address import MailAddress
from .Mail_Attachment import MailAttachment
from .Text_Encoding import TextEncoding
from .Enumerations import TransferEncoding, EntityType, LoggingMode, LoggingLevel
from .Custom_Exceptions import InvalidEncodingError, FileMissingError, IncompleteHeaderError
from .Processing_Logs import Logger
from .Rx_Mail_Message import RxMailMessage


class MailReader:
    """
        MailReader class reads the contents of an EML file, extracts all the information present in the file and stores them as a Python class object.
    """
    def __init__(self, TargetLoggingFolder: str = str()):
        self.__Lines = list()
        """List of all lines read from the EML file."""
        self.__NextLineIndex = 0
        """Index of the next line to be processed in the EML file."""
        self.__NewLineCharacter = str()
        """Newline character used in the EML file to distinguish one line from another."""
        if TargetLoggingFolder == str():
            Logger.set_configuration(LoggingMode.CONSOLE)
        else:
            Logger.set_configuration(LoggingMode.FILE, TargetLoggingFolder)

    def __set_newline_value(self):
        """
            This function extracts the newline value used as a separator between one or more lines in the EML file. The newline character varies based on the operating system running the code so this function retrieves the appropriate newline character for the operating system.
            :returns: no value(s).

        """
        first_line = self.__Lines[0]
        if first_line.endswith("\r\n"):
            self.__NewLineCharacter = "\r\n"
        elif first_line.endswith("\r"):
            self.__NewLineCharacter = "\r"
        else:
            self.__NewLineCharacter = "\n"

    def get_email(self, emlPath: str) -> RxMailMessage | None:
        """
            This function parses the EML file present at the given path and returns the parsed information as a 'RxMailMessage' object.
            :param emlPath: The complete file path where the EML file is located.
            :returns: a RxMailMessage object containing all the information parsed from the EML file. If there were any errors encountered while parsing, 'NoneType' is returned.
        """
        message = RxMailMessage()
        EmlFile = None
        try:
            if os.path.exists(emlPath):
                EmlFile = open(emlPath, "r")
                self.__Lines = EmlFile.readlines()
                EmlFile.close()
                self.__set_newline_value()
                self.__NextLineIndex = 0
                message = self.__process_mime_entity(message, str())
            else:
                raise FileMissingError(emlPath)
        except Exception as ex:
            Logger.logentry(f"An exception occurred while reading contents from EML file: {ex}", LoggingLevel.ERROR)
            message = None
        finally:
            if EmlFile is not None:
                EmlFile.close()

        return message

    def __process_mime_entity(self, message: RxMailMessage, ParentBoundary: str) -> RxMailMessage:
        """
            A recursive function that processes the MIME parts present in the EML file and represents each of these parts as a RxMailMessage object.
            :param message: The message object where information parsed from the MIME part will be stored.
            :param ParentBoundary: Parent boundary value for the MIME part being processed.
            :returns: a RxMailMessage object with all the parsed MIME part information.
        """
        try:
            CompletedHeader = str()
            ParentBoundaryStart = "--" + ParentBoundary
            ParentBoundaryEnd = ParentBoundaryStart + "--"
            while True:
                line = self.__get_next_line()
                if line.startswith(" ") or line.startswith("\t"):
                    if CompletedHeader == str():
                        raise IncompleteHeaderError(line, self.__NextLineIndex)
                    else:
                        CompletedHeader = CompletedHeader + TextEncoding.decode_header(line.strip())
                elif line == str():
                    if CompletedHeader is not str():
                        self.__process_header(CompletedHeader, message)
                    Logger.logentry(f"Empty line found on row {self.__NextLineIndex} of EML File. Header processing completed for the current MIME entity.", LoggingLevel.INFO)
                    break
                else:
                    if CompletedHeader == str():
                        CompletedHeader = TextEncoding.decode_header(line.strip())
                    else:
                        self.__process_header(CompletedHeader, message)
                        CompletedHeader = TextEncoding.decode_header(line.strip())

            message.set_entity_type()
            if ParentBoundary == str() and message.ContentType.Boundary == str():
                message.IsMultiPart = False
                complete_body = str()
                line = self.__get_next_line()
                while line is not str():
                    if complete_body == str():
                        complete_body = line
                    else:
                        complete_body = complete_body + self.__NewLineCharacter + line
                    line = self.__get_next_line()
                self.__parse_entity_body(message, complete_body)
            else:
                complete_body = str()
                message.IsMultiPart = True
                if message.ContentType.Boundary != str():
                    BoundaryFound = True
                    BoundaryStart = "--" + message.ContentType.Boundary
                    BoundaryEnd = BoundaryStart + "--"
                else:
                    BoundaryFound = False
                    BoundaryStart = str()
                    BoundaryEnd = str()
                while True:
                    line = self.__get_next_line()
                    if BoundaryFound and line == BoundaryStart:
                        message_child = self.__process_mime_entity(RxMailMessage(), message.ContentType.Boundary)
                        message.Children.append(message_child)
                        for attachment in message_child.Attachments.export_as_list():
                            message.Attachments.append(attachment)
                        message.Body = message_child.Body
                        if self.__get_last_line() == BoundaryStart:
                            self.__NextLineIndex = self.__NextLineIndex - 1
                    elif line == ParentBoundaryStart or line == ParentBoundaryEnd:
                        if not BoundaryFound:
                            self.__parse_entity_body(message, complete_body)
                        break
                    elif (BoundaryFound and line == BoundaryEnd) or line == "EOF":
                        break
                    else:
                        if complete_body == str():
                            complete_body = line
                        else:
                            complete_body = complete_body + self.__NewLineCharacter + line
        except Exception as ex1:
            Logger.logentry(f"An exception occurred while processing the MIME Entity:{ex1}", LoggingLevel.ERROR)

        return message

    def __process_header(self, header: str, message: RxMailMessage) -> None:
        """
            A function to process a header string and store it in the RxMailMessage object.
            :param header: The Header string to be processed.
            :param message: The MIME Entity object where the processed header will be stored.
            :returns: no value(s).
        """
        try:
            header = header.strip()
            if header.strip().find(":") == -1:
                raise IncompleteHeaderError(header, self.__NextLineIndex)
            rValue = (header.split(":")[1]).strip()
            if header.startswith("From"):
                mail_address = MailAddress()
                mail_address.parse(rValue)
                message.From = mail_address
            elif header.startswith("To"):
                rValue = rValue.replace(",", ";")
                emails = rValue.split(";")
                for email in emails:
                    message.add_mail_address("To", email)
            elif header.startswith("CC"):
                rValue = rValue.replace(",", ";")
                emails = rValue.split(";")
                for email in emails:
                    message.add_mail_address("Cc", email)
            elif header.startswith("BCC"):
                rValue = rValue.replace(",", ";")
                emails = rValue.split(";")
                for email in emails:
                    message.add_mail_address("Bcc", email)
            elif header.startswith("Reply-To"):
                rValue = rValue.replace(",", ";")
                emails = rValue.split(";")
                for email in emails:
                    message.add_mail_address("ReplyTo", email)
            elif header.startswith("Message-ID"):
                message.MessageID = rValue
            elif header.startswith("MIME-Version"):
                message.MimeVersion = rValue
            elif header.startswith("Subject"):
                message.Subject = TextEncoding.decode_header(rValue)
            elif header.startswith("Date"):
                message.Date = rValue
            elif header.startswith("Content-Type"):
                message.set_content_type(rValue)
            elif header.startswith("Content-Transfer-Encoding"):
                message.set_content_transfer_encoding(rValue)
            elif header.startswith("Content-Description"):
                message.ContentDescription = rValue
            elif header.startswith("Content-Disposition"):
                message.set_content_disposition(rValue)
            elif header.startswith("Content-ID"):
                message.ContentID = rValue.lstrip("<").rstrip(">")
            else:
                lValue = (header.split(":")[0]).strip()
                message.Headers.update({lValue: rValue})
        except Exception as ex:
            Logger.logentry(f"An exception occurred while processing header '{header}': {ex}", LoggingLevel.ERROR)

    def __get_next_line(self) -> str:
        """
            This function gets the next line to be processed from the EML file. If End of file has been reached, the function returns the 'EOF' value as the next line.
            :returns: the next line to be processed.
        """
        NextLine = str()
        try:
            if self.__NextLineIndex < len(self.__Lines):
                NextLine = self.__Lines[self.__NextLineIndex]
                NextLine = NextLine.strip(self.__NewLineCharacter)
                self.__NextLineIndex = self.__NextLineIndex + 1
            else:
                NextLine = "EOF"
        except Exception as ex:
            Logger.logentry(f"An error occurred while fetching the next line to be processed: {ex}", LoggingLevel.ERROR)

        return NextLine

    def __get_last_line(self) -> str:
        """
            This function gets the last line that was processed from the EML file.
            :returns: a string containing the last line processed.
        """
        LastLine = str()
        try:
            LastLine = self.__Lines[self.__NextLineIndex - 1]
            LastLine = LastLine.strip(self.__NewLineCharacter)
        except Exception as ex:
            Logger.logentry(f"Exception occurred in get_last_line():> {ex}", LoggingLevel.ERROR)

        return LastLine

    def __parse_entity_body(self, message: RxMailMessage, complete_body: str):
        """
            This function parses the MIME part body and stores the parsed content in the appropriate 'RxMailMessage' object.

            :param message: The Entity object where the processed content is to be stored.
            :param complete_body: The encoded string to be decoded and stored as MIME entity body.
            :returns: no value(s).
        """
        try:
            if message.ContentTransferEncoding == TransferEncoding.BASE64:
                complete_body = complete_body.replace(self.__NewLineCharacter, "")
                mail_attachment = MailAttachment()
                mail_attachment.parse_values(TextEncoding.decode_base64_file(complete_body), message.ContentType, message.ContentDisposition, message.ContentID)
                message.Attachments.append(mail_attachment)
                message.Body = str()
            elif message.ContentTransferEncoding == TransferEncoding.QUOTED_PRINTABLE:
                if message.EntityType == EntityType.TEXT:
                    message.Body = TextEncoding.decode_quoted_printable_string(complete_body, message.ContentType.Charset, False)
            elif message.ContentTransferEncoding == TransferEncoding.SEVEN_BIT:
                message.Body = complete_body
            elif message.ContentTransferEncoding == TransferEncoding.EIGHT_BIT:
                message.Body = complete_body
            else:
                raise InvalidEncodingError()
        except Exception as ex:
            Logger.logentry(f"An error occurred while parsing entity body: {ex}", LoggingLevel.ERROR)
