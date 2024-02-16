from quopri import decodestring
from base64 import b64decode
from .Custom_Exceptions import InvalidEncodingError


class TextEncoding:
    """
        Class to perform character encoding - BASE64 and QUOTED-PRINTABLE on MIME part content. It uses the 'quopri' and 'base64' modules in the Standard Python library to decode the encoded strings.
    """
    @staticmethod
    def decode_quoted_printable_string(encoded_string: str, string_charset: str, is_header: bool) -> str:
        """
            [FOR INTERNAL USE ONLY]
            A static function to convert Quoted-Printable encoded string to human-readable string.
            :param encoded_string: The string to be decoded.
            :param string_charset: Character set of the human-readable string.
            :param is_header: A boolean value to indicate if the encoded string is an email header.
            :returns:  the decoded string.
        """
        if string_charset == str():
            string_charset = "utf-8"
        decoded_value = decodestring(encoded_string, header=is_header)
        decoded_string = decoded_value.decode(string_charset)
        return decoded_string

    @staticmethod
    def decode_base64_string(encoded_string: str, string_charset: str = "utf-8") -> str:
        """
            [FOR INTERNAL USE ONLY]
            A static function to convert BASE64 encoded string to human-readable string.
            :param encoded_string: The string to be decoded.
            :param string_charset: Character set of the human-readable string.
            :returns: the decoded string.
        """
        decoded_bytes = b64decode(encoded_string)
        decoded_string = decoded_bytes.decode(string_charset)
        return decoded_string

    @staticmethod
    def decode_base64_file(file_contents: str) -> bytes:
        """
            A static function to convert BASE64 encoded file back to normal binary file.
            :param file_contents: Base64 encoded string representing the binary file contents.
            :returns: the decoded binary file contents as 'bytes'.
        """
        decoded_file_contents = b64decode(file_contents)
        return decoded_file_contents

    @staticmethod
    def decode_header(encoded_string: str) -> str:
        """
            A static function to decode an encoded header in a MIME part.
            :param encoded_string: The string to be decoded.
            :returns: the decoded string.
        """
        if encoded_string.startswith("=?"):
            string_parts = encoded_string.lstrip("=?").rstrip("?=").split("?")
            if (string_parts[1]).strip().upper() == "Q":
                decoded_string = TextEncoding.decode_quoted_printable_string(string_parts[2], string_parts[0], True)
            elif (string_parts[1]).strip().upper() == "B":
                decoded_string = TextEncoding.decode_base64_string(string_parts[2], string_parts[0])
            else:
                raise InvalidEncodingError(encoded_string)
        else:
            decoded_string = encoded_string

        return decoded_string
