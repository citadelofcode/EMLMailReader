import json
import os
from .Mail_Address import MailAddress, MailAddressCollection
from .Mail_Attachment import MailAttachmentCollection
from .Content_Type import ContentType
from .Content_Disposition import ContentDisposition
from .Enumerations import TransferEncoding, EntityType
from .Custom_Exceptions import FolderNotAvailableError


class RxMailMessage:
    """
        A class to represent all the information parsed from the EML file.
    """
    def __init__(self):
        self.From = None
        """Email address in the 'From' header of EML file."""
        self.To = MailAddressCollection()
        """A list of all the emails present in the 'To' header of EML file."""
        self.Cc = MailAddressCollection()
        """A list of all the emails present in the 'Cc' header of EML file."""
        self.Bcc = MailAddressCollection()
        """A list of all the emails present in the 'Bcc' header of EML file."""
        self.ReplyTo = MailAddressCollection()
        """A list of all the emails present in the 'Reply-To' header of EML file."""
        self.Subject = str()
        """Email Subject"""
        self.Body = str()
        """Complete email body."""
        self.ContentType = None
        """Content-Type of MIME part."""
        self.ContentDisposition = None
        """Content-Disposition of MIME part."""
        self.ContentTransferEncoding = TransferEncoding.SEVEN_BIT
        """Content-Transfer-Encoding of MIME part."""
        self.Headers = dict()
        """List of all headers present in the MIME part."""
        self.HeadersEncoding = str()
        """Encoding used in Headers present in the MIME part."""
        self.BodyEncoding = str()
        """Encoding used in body of the MIME part."""
        self.MessageID = str()
        """'Message-ID' header value."""
        self.IsMultiPart = False
        """Denotes if the current part is single part (False) or multi-part (True)."""
        self.MimeVersion = str()
        """'MIME-Version' header value."""
        self.Date = str()
        """'Date' header value."""
        self.Children = list()
        """List of child MIME parts."""
        self.ContentDescription = str()
        """'Content-Description' header value."""
        self.EntityType = EntityType.MIME_PART
        """Denotes the type of the MIME part."""
        self.Attachments = MailAttachmentCollection()
        """Contains all the attachments in the MIME part."""
        self.ContentID = str()
        """'Content-ID' header value."""

    def add_mail_address(self, PropertyName: str, MailAddressValue: str):
        """
            [FOR INTERNAL USE ONLY]
            Adds a MailAddress() to the RxMailMessage object. This function typically parses the To, From, Cc, ReplyTo fields in the EML file.
            :param PropertyName: Name of the property in RxMailMessage object.
            :param MailAddressValue: The value to be parsed as a MailAddress.
            :returns: no value(s).
        """
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

    def set_content_type(self, ContentTypeValue: str):
        """
            [FOR INTERNAL USE ONLY]
            Sets the Content-Type for the current MIME part.
            :param ContentTypeValue: String value to be parsed as ContentType.
            :returns: no value(s).
        """
        self.ContentType = ContentType()
        self.ContentType.parse(ContentTypeValue)

    def set_content_disposition(self, ContentDispositionValue: str):
        """
            [FOR INTERNAL USE ONLY]
            Sets the Content-Disposition for the current MIME part.
            :param ContentDispositionValue: String value to be parsed as ContentDisposition.
            :returns: no value(s).
        """
        self.ContentDisposition = ContentDisposition()
        self.ContentDisposition.parse(ContentDispositionValue)

    def set_content_transfer_encoding(self, ContentTransferEncodingValue: str):
        """
            [FOR INTERNAL USE ONLY]
            Sets the Content-Transfer-Encoding for the current MIME part.
            :param ContentTransferEncodingValue: String value to be parsed as ContentTransferEncoding.
            :returns: no value(s).
        """
        ContentTransferEncodingValue = ContentTransferEncodingValue.lower()
        if ContentTransferEncodingValue == "8bit":
            self.ContentTransferEncoding = TransferEncoding.EIGHT_BIT
        elif ContentTransferEncodingValue == "base64":
            self.ContentTransferEncoding = TransferEncoding.BASE64
        elif ContentTransferEncodingValue == "quoted-printable":
            self.ContentTransferEncoding = TransferEncoding.QUOTED_PRINTABLE
        else:
            self.ContentTransferEncoding = TransferEncoding.SEVEN_BIT

    def set_entity_type(self):
        """
            [FOR INTERNAL USE ONLY]
            This function updates the entity type for the MIME part.
            :returns: no value(s).
        """
        media_type = self.ContentType.MediaType.lower()
        if media_type.startswith("application") or media_type.startswith("image"):
            self.EntityType = EntityType.ATTACHMENT
        elif media_type.startswith("multipart"):
            self.EntityType = EntityType.MIME_PART
        else:
            self.EntityType = EntityType.TEXT

    def export_as_json(self) -> str:
        """
        Function that converts a RxMailMessage object to a JSON string.
        :returns: a JSON string containing all the fields of the RxMailMessage object.
        """
        final_object = dict()
        final_object.update({
            "From": str(self.From),
            "Subject": self.Subject,
            "Headers-Encoding": self.HeadersEncoding,
            "Body-Encoding": self.BodyEncoding,
            "Message-ID": self.MessageID,
            "IsMultiPart": self.IsMultiPart,
            "Mime-Version": self.MimeVersion,
            "Date": self.Date,
            "Content-Description": self.ContentDescription,
            "Entity-Type": self.EntityType.name,
            "Content-ID": self.ContentID,
            "Headers": self.Headers,
            "Content-Type": str(self.ContentType),
            "Content-Disposition": str(self.ContentDisposition),
            "To": str(self.To),
            "Cc": str(self.Cc),
            "Bcc": str(self.Bcc),
            "Reply-To": str(self.ReplyTo),
            "Attachment-Count": self.Attachments.length()
        })

        return json.dumps(final_object)

    def save_attachments(self, TargetFolderPath: str):
        """
        A function to save all the attachments in the RxMailMessage object to the target folder.
        :param TargetFolderPath: Target folder where the attachments will be saved. If target folder does not exist, an exception will be thrown.
        :returns: no value(s).
        """
        if os.path.exists(TargetFolderPath):
            for attachment in self.Attachments.export_as_list():
                TargetFilePath = os.path.join(TargetFolderPath, attachment.Name)
                with open(TargetFilePath, "wb") as my_file:
                    my_file.write(attachment.Contents)
        else:
            raise FolderNotAvailableError(TargetFolderPath)
