from Mail_Address import MailAddress
from Content_Type import ContentType


class RxMailMessage:
    def __init__(self):
        self.From = None
        self.To = list()
        self.Cc = list()
        self.Bcc = list()
        self.ReplyTo = list()
        self.Subject = ""
        self.Body = ""
        self.ContentType = None
        self.Headers = dict()
        self.HeadersEncoding = ""
        self.BodyEncoding = ""
        self.MessageID = ""
        self.IsMultiPart = False
        self.MimeVersion = ""
        self.Date = ""
        self.Parts = list()

    def add_mail_address(self, PropertyName: str, MailAddressValue: str):
        try:
            mail_address = MailAddress()
            mail_address.parse(MailAddressValue)
            if PropertyName == "To":
                self.To.append(mail_address)
            elif PropertyName == "Cc":
                self.Cc.append(mail_address)
            elif PropertyName == "Bcc":
                self.Bcc.append(mail_address)
            elif PropertyName == "ReplyTo":
                self.ReplyTo.append(mail_address)
            else:
                raise Exception(f"{PropertyName} is not of type 'MailAddress'")
        except Exception as ex:
            print(f"An error occurred while adding email address to property '{PropertyName}':", ex)

    def set_content_type(self, ContentTypeValue: str):
        try:
            ContentTypeObj = ContentType()
            if ContentTypeValue.find(";") != -1:
                ContentTypeValues = ContentTypeValue.split(";")
                ContentTypeObj.MediaType = ContentTypeValues[0].strip()
                SecondValue = (ContentTypeValues[1]).split('=')
                if SecondValue[0].strip().lower() == "charset":
                    ContentTypeObj.Charset = SecondValue[1].strip()
                elif SecondValue[0].strip().lower() == "boundary":
                    ContentTypeObj.Boundary = SecondValue[1].strip()
            else:
                ContentTypeObj.MediaType = ContentTypeValue.strip()
            self.ContentType = ContentTypeObj
        except Exception as ex:
            print("An error occurred while settings content type:", ex)
