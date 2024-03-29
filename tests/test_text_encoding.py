import unittest
import os
from EMLMailReader import TextEncoding, InvalidEncodingError


class TestTextEncoding(unittest.TestCase):
    """
    A unit test case to check the methods exposed by 'TextEncoding' class.
    """
    def test_quoted_printable_encoded_header(self):
        """
        Checks if a quoted printable encoded header is decoded as expected.
        :returns: Does not return a value.
        """
        encoded_text = "=?utf-8?Q?This string has =3D signs and special characters!?="
        decoded_text = TextEncoding.decode_header(encoded_text)
        self.assertEqual(decoded_text, "This string has = signs and special characters!", "Quoted Printable decoded value does not match the expected value.")

    def test_base64_encoded_header(self):
        """
        Checks if a base64 encoded header is decoded as expected.
        :returns: Does not return a value.
        """
        encoded_text = "=?utf-8?B?RU1MTWFpbFJlYWRlciBpcyBhbiBhbWF6aW5nIGxpYnJhcnkgdGhhdCBvbmUgbXVzdCBkZWZpbml0ZWx5IHVzZS4=?="
        decoded_text = TextEncoding.decode_header(encoded_text)
        self.assertEqual(decoded_text, "EMLMailReader is an amazing library that one must definitely use.", "Base64 decoded value does not match the expected value.")

    def test_invalid_encoding_error(self):
        """
        Checks if InvalidEncoding error is returned in case of unknown encoding formats.
        :returns: Does not return a value.
        """
        encoded_text = "=?utf-8?G?RU1MTWFpbFJlYWRlciBpcyBhbiBhbWF6aW5nIGxpYnJhcnkgdGhhdCBvbmUgbXVzdCBkZWZpbml0ZWx5IHVzZS4=?="
        with self.assertRaises(InvalidEncodingError):
            TextEncoding.decode_header(encoded_text)

    def test_plaintext_header(self):
        """
        Checks if the plaintext value is returned as-is, when passed to the decode_header() function.
        :returns: Does not return a value.
        """
        plaintext_header = "This is a normal test subject to be used for testing."
        self.assertEqual(TextEncoding.decode_header(plaintext_header), plaintext_header, "Value returned does not match the plaintext header provided.")

    def test_base64_encoded_file(self):
        """
        Checks if the base64 decoded file content returned is valid.
        :returns: Does not return a value.
        """
        file_path = os.path.join(os.getcwd(), "tests", "assets", "encoded_file.txt")
        content_string = str()
        with open(file_path, "r") as my_file:
            lines = my_file.readlines()
            for current_line in lines:
                if current_line.endswith("\r\n"):
                    current_line = current_line.replace("\r\n", "")
                elif current_line.endswith("\r"):
                    current_line = current_line.replace("\r", "")
                elif current_line.endswith("\n"):
                    current_line = current_line.replace("\n", "")
                content_string += current_line
        decoded_bytes = TextEncoding.decode_base64_file(content_string)
        self.assertEqual(len(decoded_bytes), 1311269, "Decoded byte length does not match the expected value.")


if __name__ == "__main__":
    unittest.main()
