import unittest
import os
import json
from EMLMailReader import MailReader, FolderNotAvailableError
from unittest.mock import patch


class TestEmailParsing(unittest.TestCase):
    """
    A class to test the email parsing process and validate the data returned by MailReader instance.
    """
    @classmethod
    def setUp(cls):
        test_cases_file_path = os.path.join(os.getcwd(), "tests", "assets", "test-cases.json")
        cls.eml_files_directory = os.path.join(os.getcwd(), "tests", "assets", "eml-files")
        cls.negative_case_folder_path = os.path.join(os.getcwd(), "tests", "assets", "neg-files")
        with open(test_cases_file_path, "r") as fp:
            cls.test_cases = json.load(fp)

    def test_email_parsing(self):
        """
        Checks if an input email is parsed correctly and valid data is exported via export_as_json() of RxMailMessage.
        :returns: Does not return a value.
        """
        file_list = list(self.test_cases.keys())
        for file in file_list:
            with self.subTest(f"{file} :: Validate function export_as_json()", input=file):
                complete_file_path = os.path.join(self.eml_files_directory, f"{file}.eml")
                reader = MailReader()
                message = reader.get_email(complete_file_path)
                self.assertIsNotNone(message, "RxMailMessage object returned by parser cannot be 'None'.")
                json_contents = message.export_as_json()
                json_obj = json.loads(json_contents)
                expected_results = self.test_cases[file]
                for key, value in expected_results.items():
                    with self.subTest(f"{file} :: Validate value for property '{key}'", input=key):
                        self.assertEqual(json_obj[key], value, f"Value returned by parser for {key} does not match expected value.")

    def test_save_attachments(self):
        """
        Checks if attachments present in an email file are saved successfully to the target folder location.
        :returns: Does not return a value.
        """
        file_list = list(self.test_cases.keys())
        for file in file_list:
            expected_results = self.test_cases[file]
            if expected_results["Attachment-Count"] > 0:
                with self.subTest(f"{file} :: Validate function save_attachments()", input=file):
                    complete_file_path = os.path.join(self.eml_files_directory, f"{file}.eml")
                    reader = MailReader()
                    message = reader.get_email(complete_file_path)
                    with patch('builtins.open') as mock_open:
                        message.save_attachments(self.eml_files_directory)
                        for attachment in message.Attachments.export_as_list():
                            target_file = os.path.join(self.eml_files_directory, attachment.Name)
                            mock_open.assert_any_call(target_file, "wb")

    def test_save_attachments_folder_not_available(self):
        """
        Checks if save_attachments() of RxMailMessage throws a FolderNotAvailableError when the target folder path does not exist.
        :returns: Does not return a value.
        """
        file_list = list(self.test_cases.keys())
        file_name = str()
        for file in file_list:
            expected_results = self.test_cases[file]
            if expected_results["Attachment-Count"] > 0:
                file_name = file
                break
        complete_file_path = os.path.join(self.eml_files_directory, f"{file_name}.eml")
        reader = MailReader()
        message = reader.get_email(complete_file_path)
        with self.assertRaises(FolderNotAvailableError):
            message.save_attachments(self.negative_case_folder_path)


if __name__ == "__main__":
    unittest.main()
