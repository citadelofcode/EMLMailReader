import unittest
from EMLMailReader import MailAddress, MailAddressCollection


class TestMailAddress(unittest.TestCase):
    """
        A unit test case to check the methods exposed by 'MailAddress' class.
    """
    def setUp(self):
        self.mail_address = MailAddress()
        self.collection = MailAddressCollection()

    def test_display_name(self):
        """
        Checks if the display name returned by parse() matches the expected value.
        :returns: Does not return a value.
        """
        self.mail_address.parse("\"Mahesh Kumaar Balaji\" <mk.balaji@gmail.com>")
        self.assertEqual(self.mail_address.DisplayName, "Mahesh Kumaar Balaji", "Display name parsed does not match the expected value.")
        self.mail_address = MailAddress()
        self.mail_address.parse("mk.balaji@gmail.com")
        self.assertEqual(self.mail_address.DisplayName, "", "Display name parsed does not match the default value.")

    def test_email_address(self):
        """
        Checks if the email address returned by parse() matches the expected value.
        :returns: Does not return a value.
        """
        self.mail_address.parse("\"Mahesh Kumaar Balaji\" <mk.balaji@gmail.com>")
        self.assertEqual(self.mail_address.Email, "mk.balaji@gmail.com", "Email address parsed does not match the expected value.")
        self.mail_address = MailAddress()
        self.mail_address.parse("mk.balaji@gmail.com")
        self.assertEqual(self.mail_address.Email, "mk.balaji@gmail.com", "Email address parsed does not match the expected value.")

    def test_mail_address_stringify(self):
        """
        Checks if the stringified version od Mail Address instance matches the expected value.
        :returns: Does not return a value.
        """
        self.mail_address.parse("\"Mahesh Kumaar Balaji\" <mk.balaji@gmail.com>")
        self.assertEqual(str(self.mail_address), "Mahesh Kumaar Balaji <mk.balaji@gmail.com>", "Stringified email address returned does not match the expected value.")
        self.mail_address = MailAddress()
        self.mail_address.parse("mk.balaji@gmail.com")
        self.assertEqual(str(self.mail_address), "mk.balaji@gmail.com", "Stringified email address returned does not match the expected value.")

    def test_mail_address_collection(self):
        """
        Checks if a MailAddress instance is correctly appended to a MailAddressCollection object.
        :returns: Does not return a value.
        """
        self.mail_address.parse("\"Mahesh Kumaar Balaji\" <mk.balaji@gmail.com>")
        self.collection.append(self.mail_address)
        mail_address_one = MailAddress()
        mail_address_one.parse("mk.balaji@gmail.com")
        self.collection.append(mail_address_one)
        self.assertEqual(self.collection.length(), 2, "Length of the MailAddress collection does not match the expected value.")
        self.assertEqual(str(self.collection), "Mahesh Kumaar Balaji <mk.balaji@gmail.com>;mk.balaji@gmail.com", "Stringified email address returned does not match the expected value.")


if __name__ == "__main__":
    unittest.main()
