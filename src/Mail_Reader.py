import os
from Rx_Mail_Message import RxMailMessage
from Mail_Address import MailAddress


class MailReader:
    def __init__(self):
        self.ParentBoundaryStart = ""
        self.ParentBoundaryEnd = ""
        self.Lines = None
        self.NextLineIndex = 0

    def get_email(self, emlPath: str) -> RxMailMessage:
        message = RxMailMessage()
        try:
            if os.path.exists(emlPath):
                EmlFile = open(emlPath, "r")
                self.Lines = EmlFile.readlines()
                EmlFile.close()
                self.process_mime_entity(message, "")
            else:
                raise Exception(f"File does not exist at path '{emlPath}'.")
        except Exception as ex:
            print("An exception occurred while reading contents from EML file:", ex)
            message = None

        return message

    def process_mime_entity(self, message: RxMailMessage, ParentBoundaryStart: str) -> None:
        try:
            CompletedHeader = str()
            line = self.get_next_line()
            while line is not None:
                if line.startswith(" ") or line.startswith("\t"):
                    if CompletedHeader == "":
                        raise Exception("Incomplete header found in EML file.")
                    else:
                        CompletedHeader = CompletedHeader + "\n" + line
                        CompletedHeader = CompletedHeader.strip("\n")
                elif line == "\n":
                    print("Newline character found indicating the end of header part of MIME entity. So, Breaking out of the loop.")
                    break
                else:
                    if CompletedHeader == "":
                        CompletedHeader = line
                    else:
                        MailReader.process_header(CompletedHeader, message)
                        CompletedHeader = line
                line = self.get_next_line()
            if message.ContentType.Boundary != "":
                message.IsMultiPart = True
                ParentBoundaryStart = "--" + message.ContentType.Boundary

        except Exception as ex1:
            print("An exception occurred while processing the MIME Entity:", ex1)

    @staticmethod
    def process_header(header: str, message: RxMailMessage) -> None:
        try:
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
            elif header.startswith("Cc"):
                rValue = rValue.replace(",", ";")
                emails = rValue.split(";")
                for email in emails:
                    message.add_mail_address("Cc", email)
            elif header.startswith("Bcc"):
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
                message.Subject = rValue
            elif header.startswith("Date"):
                message.Date = rValue
            elif header.startswith("Content-Type"):
                message.set_content_type(rValue)
            else:
                lValue = (header.split(":")[0]).strip()
                message.Headers[lValue] = rValue
        except Exception as ex:
            print(f"An exception occurred while processing header '{header.split(':')[0]}':", ex)

    def get_next_line(self) -> str | None:
        NextLine = None
        try:
            if self.NextLineIndex >= len(self.Lines):
                NextLine = None
            else:
                NextLine = self.Lines[self.NextLineIndex]
                self.NextLineIndex = self.NextLineIndex + 1
        except Exception as ex:
            print("An error occurred while fetching the next line to be processed:", ex)

        return NextLine
