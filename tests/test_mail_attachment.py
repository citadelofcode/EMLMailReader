import unittest
from EMLMailReader import MailAttachment, ContentType, ContentDisposition


class TestMailAttachment(unittest.TestCase):
    """
    A unit test case to check the methods exposed by 'MailAttachment' class.
    """
    def setUp(self):
        self.mail_attachment = MailAttachment()
        self.content_type = ContentType()
        self.content_disposition = ContentDisposition()

    def test_attachment_name(self):
        """
        Checks if the file name set by parse_values() method matches the expected file name.
        :returns: Does not return a value.
        """
        # Scenario 1 :: When file name is present in Content-Type and not in Content-Disposition.
        self.content_type.parse("application/pdf; name=\"Getting started with OneDrive-CFTS-MKB.pdf\"")
        self.content_disposition.parse("attachment; size=1311269")
        self.mail_attachment.parse_values(bytes(), self.content_type, self.content_disposition, str())
        self.assertEqual(self.mail_attachment.Name, "Getting started with OneDrive-CFTS-MKB.pdf", "Attachment name does not match the Content-Type name.")

        # Scenario 2 :: When file name is present in Content-Disposition and not in Content-Type.
        self.mail_attachment = MailAttachment()
        self.content_type = ContentType()
        self.content_disposition = ContentDisposition()
        self.content_type.parse("application/pdf; charset=utf-8")
        self.content_disposition.parse("attachment; size=1311269; filename=\"Getting started with OneDrive-CFTS-MKB-1.pdf\"")
        self.mail_attachment.parse_values(bytes(), self.content_type, self.content_disposition, str())
        self.assertEqual(self.mail_attachment.Name, "Getting started with OneDrive-CFTS-MKB-1.pdf", "Attachment name does not match the Content-Disposition name.")

        # Scenario 3 :: When file name is present in both Content-Type and in Content-Disposition.
        self.mail_attachment = MailAttachment()
        self.content_type = ContentType()
        self.content_disposition = ContentDisposition()
        self.content_type.parse("application/pdf; charset=utf-8; name=\"Getting started with OneDrive-CFTS-MKB-2.pdf\"")
        self.content_disposition.parse("attachment; size=1311269; filename=\"Getting started with OneDrive-CFTS-MKB-2.pdf\"")
        self.mail_attachment.parse_values(bytes(), self.content_type, self.content_disposition, str())
        self.assertEqual(self.mail_attachment.Name, "Getting started with OneDrive-CFTS-MKB-2.pdf", "Attachment name does not match the Content-Type name.")

        # Scenario 4 :: When file name is neither present in Content-Type nor in Content-Disposition.
        self.mail_attachment = MailAttachment()
        self.content_type = ContentType()
        self.content_disposition = ContentDisposition()
        self.content_type.parse("application/pdf; charset=utf-8")
        self.content_disposition.parse("attachment; size=1311269")
        self.mail_attachment.parse_values(bytes(), self.content_type, self.content_disposition, str())
        self.assertEqual(self.mail_attachment.Name, "", "Attachment name does not match the default value.")


if __name__ == "__main__":
    unittest.main()
