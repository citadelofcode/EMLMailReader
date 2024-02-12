## Project Description

A Python library designed to analyze EML files and to extract details and attachments contained within. It captures various information from the email, such as attachments, sender address, recipient address, subject, body, and a comprehensive list of all headers in the EML file. The parsed information is exportable as a JSON object, and attachments can be conveniently downloaded to a specified local directory.

## Table of Contents

- [Properties Exposed](https://github.com/maheshkumaarbalaji/EMLMailReader#properties-exposed)
- [Example Usage](https://github.com/maheshkumaarbalaji/EMLMailReader#example-usage)
- [Modules Used](https://github.com/maheshkumaarbalaji/EMLMailReader#modules-used)
- [API Documentation](https://github.com/maheshkumaarbalaji/EMLMailReader#api-documentation)

## Properties Exposed



## Example Usage

Here's a sample code to leverage **EMLMailReader** in parsing an EML file and extracting information contained within.

> from Mail_Reader import MailReader
> 
> from Rx_Mail_Message import RxMailMessage
> 
> reader: MailReader = MailReader()
> 
> message: RxMailMessage = reader.get_email("COMPLETE_EML_FILE_PATH")
> 
> json_string = message.export_as_json()
>
> print(json_string)

The above code will print a JSON like the one given below.

![The JSON object returned as result.](https://github.com/maheshkumaarbalaji/EMLMailReader/assets/README/json-object.jpeg)

## Modules Used



## API Documentation

