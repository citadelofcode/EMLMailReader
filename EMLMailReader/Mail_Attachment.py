from .Content_Type import ContentType
from .Content_Disposition import ContentDisposition
from copy import deepcopy


class MailAttachment:
    """
        Represents an attachment present in the EML file.
    """
    def __init__(self):
        self.Name = str()
        """Name of the attachment."""
        self.ContentType = ContentType()
        """Content-Type of the attachment."""
        self.ContentDisposition = ContentDisposition()
        """Content-Disposition of the attachment."""
        self.Contents = bytes()
        """Contents of the attachment file as 'bytes'."""
        self.ContentID = str()
        """Content-ID value for the attachment. This value is available in case the attachment is part of the email body."""

    def parse_values(self, contents: bytes, content_type: ContentType, content_disposition: ContentDisposition, content_id: str):
        """
            Creates a 'MailAttachment' from the given parameters.
            :param contents: Attachment file content given as 'bytes'.
            :param content_type: The Content-Type of the attachment.
            :param content_disposition: The Content-Disposition of the attachment.
            :param content_id: The Content-ID value of the attachment.
            :returns: no value(s).
        """
        self.Contents = deepcopy(contents)
        self.ContentType = deepcopy(content_type)
        self.ContentDisposition = deepcopy(content_disposition)
        self.ContentID = deepcopy(content_id)
        if self.ContentType.Name != str():
            self.Name = self.ContentType.Name
        elif self.ContentDisposition.FileName != str():
            self.Name = self.ContentDisposition.FileName
        else:
            self.Name = str()


class MailAttachmentCollection:
    """
    A Collection to hold a list of MailAttachment instance(s).
    """
    def __init__(self):
        self.__attachments = list[MailAttachment]()
        """Iterable to hold the MailAttachment instance(s)."""

    def append(self, attachment: MailAttachment):
        """
            A function to insert a MailAttachment instance to the end of the collection.
            :param attachment: MailAttachment object to be added to the end of the collection.
            :returns: no value(s).
        """
        self.__attachments.append(attachment)

    def length(self) -> int:
        """
        A Function to return the number of 'MailAttachment' items in the collection instance.
        :returns: the number of items in the collection.
        """
        return len(self.__attachments)

    def export_as_list(self) -> list:
        """
        A function to export MailAddressCollection as a list of 'MailAttachment' instances present in the collection.
        :returns: A new list containing all the 'MailAttachment' instance present in the collection.
        """
        return deepcopy(self.__attachments)
