from .test_content_disposition import TestContentDisposition
from .test_content_type import TestContentType
from .test_mail_address import TestMailAddress
from .test_mail_attachment import TestMailAttachment
from .test_text_encoding import TestTextEncoding
from .test_email_parsing import TestEmailParsing
import unittest


test_cases = [TestContentDisposition, TestContentType, TestMailAddress, TestMailAttachment, TestTextEncoding, TestEmailParsing]


def load_tests(loader, tests, pattern):
    suite = unittest.TestSuite()
    for test_case_class in test_cases:
        tests = loader.loadTestsFromTestCase(test_case_class)
        suite.addTests(tests)
    return suite
