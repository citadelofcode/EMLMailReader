## Project Description

A Python library designed to analyze EML files and to extract details and attachments contained within. It captures various information from the email, such as attachments, sender address, recipient address, subject, body, and a comprehensive list of all headers in the EML file. The parsed information is exportable as a JSON object, and attachments can be conveniently downloaded to a specified local directory.

## Table of Contents

- [Example Usage](https://github.com/maheshkumaarbalaji/EMLMailReader#example-usage)
- [Modules Used](https://github.com/maheshkumaarbalaji/EMLMailReader#modules-used)
- [Documentation](https://github.com/maheshkumaarbalaji/EMLMailReader#documentation)

## Example Usage

Here's a sample code to leverage **EMLMailReader** in parsing an EML file and extracting information contained within.

```
from Mail_Reader import MailReader
from Rx_Mail_Message import RxMailMessage
  
reader: MailReader = MailReader()
message: RxMailMessage = reader.get_email("COMPLETE_EML_FILE_PATH")
json_string = message.export_as_json()
print(json_string)
```

In this context, the term "COMPLETE_EML_FILE_PATH" indicates the complete path of the .EML file intended for processing. Running this code will output a JSON string resembling the one provided below.

```
{
    "From": "A Sample Email <sample-email-address@sample-domain.com>",
    "Subject": "This is a test process to generate sample JSON for emlmailreader",
    "Headers-Encoding": "",
    "Body-Encoding": "",
    "Message-ID": "<65c8f7741866_1c7cdb1e649248c@ao3-app09.mail>",
    "IsMultiPart": true,
    "Mime-Version": "1.0",
    "Date": "Sun, 11 Feb 2024 16",
    "Content-Description": "",
    "Entity-Type": "MIME_PART",
    "Content-ID": "",
    "Headers": 
    {
      "Received-SPF": "Pass (protection.outlook.com",
      "X-IncomingTopHeaderMarker": "OriginalChecksum",
      "DKIM-Signature": "v=1; a=rsa-sha256; q=dns/txt; c=relaxed/relaxed;d=archiveofourown.org; s=dkim20210802; h=Content-Transfer-Encoding",
      "X-IncomingHeaderCount": "11",
      "Return-Path": "do-not-reply@archiveofourown.org",
      "X-Message-Delivery": "Vj0xLjE7dXM9MDtsPTA7YT0xO0Q9MTtHRD0xO1NDTD0tMQ=="
    },
    "Content-Type": "{\"Media-Type\": \"multipart/alternative\", \"Character-Set\": \"utf-8\", \"Name\": \"\", \"Boundary\": \"--==_mimepart_65c8f773f2a1b_1c7cdb1e64923ad\"}",
    "Content-Disposition": "None",
    "To": "something@something.com",
    "Cc": "",
    "Bcc": "",
    "Reply-To": "",
    "Attachment-Count": 0
}
```

## Modules Used

Given below are the list of all the modules used in the *EMLMailReader* library.

- **os** - To perform operating system file path manipulations.
- **logging** - To generate logs for EML file processing.
- **quopri** - To decode quoted-printable encoded string.
- **base64** - To decode base64 encoded string.
- **json** - To convert a python object to JSON and vice versa.

All modules mentioned above are present in the Standard Python library and thus, do not require explicit installation or configuration.

## Documentation

This section showcases the key classes employed in the library for handling an EML file and storing the information extracted from it.

| **Class Name** | **Purpose in library**                                                                             |
|----------------|----------------------------------------------------------------------------------------------------|
| MailReader     | Processes an EML file, and returns the extracted information as an object of type *RxMailMessage*. |
| RxMailMessage  | A container to store and process information parsed from the EML file.                             |
| TextEncoding   | Exposes methods to decode header strings and MIME part body in the EML file.                       |
| MailAttachment | Exposes properties and methods to represent a single mail attachment from the EML file.            |


