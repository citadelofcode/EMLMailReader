# Documentation

This section showcases the key classes employed in the library for handling an EML file and storing the information extracted from it.

| **Class Name**                            | **Purpose in library**                                                                             |
|-------------------------------------------|----------------------------------------------------------------------------------------------------|
| [MailReader](#mailreader)                 | Processes an EML file, and returns the extracted information as an object of type *RxMailMessage*. |
| [RxMailMessage](#rxmailmessage)           | A container to store and process information parsed from the EML file.                             |
| [TextEncoding](#textencoding)             | Exposes methods to decode header strings and MIME part body in the EML file.                       |
| [MailAttachment](#mailattachment)         | Exposes properties and methods to represent a single mail attachment from the EML file.            |
| [MailAddress](#mailaddress)               | A class to represent an email address.                                                             |
| [ContentType](#contenttype)               | A class to represent the Content-Type header of a MIME entity.                                     |
| [ContentDisposition](#contentdisposition) | A class to represent the Content-Disposition header of a MIME entity.                              |
| [Logger](#logger)                         | A class to manage the configuration and generation of logs during EML file processing.             |

This section also elaborates other custom entities exposed by the library.

| **Name**                                    | **Purpose in library**                                                   |
|---------------------------------------------|--------------------------------------------------------------------------|
| [Custom Enumerations](#custom-enumerations) | Enumerations to record different options available for processing.       |
| [Custom Exceptions](#custom-exceptions)     | Exceptions to report error scenarios that might occur during processing. |
| [Custom Collections](#custom-collections)   | Collections to hold a list of items of a composite type.                 |


## MailReader

Exposes a single instance method, to process an EML file and return all the information extracted (headers, email body and attachments) as an RxMailMessage object.

### Instance Method(s)

| **Method** | **Parameter(s)**                                                         | **Return(s)**                                                                           |
|------------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| get_email  | emlPath [string] - The complete file path where the EML file is located. | a RxMailMessage object in case of successful parsing, 'NoneType' in case of any errors. |

## RxMailMessage

A class to represent all the information extracted from an EML file.

### Properties

| **Property**            | **Type**                 | **Purpose**                                                        |
|-------------------------|--------------------------|--------------------------------------------------------------------|
| From                    | MailAddress              | Email address in the 'From' header of EML file.                    |
| To                      | MailAddressCollection    | A list of all the emails present in 'To' header of EML file.       |
| Cc                      | MailAddressCollection    | A list of all the emails present in 'Cc' header of EML file.       |
| Bcc                     | MailAddressCollection    | A list of all the emails present in 'Bcc' header of EML file.      |
| ReplyTo                 | MailAddressCollection    | A list of all the emails present in 'Reply-To' header of EML file. |
| Subject                 | string                   | Subject of the email                                               |
| Body                    | string                   | Body of the email                                                  |
| ContentType             | ContentType              | Value in the 'Content-Type' header of EML file.                    |
| ContentDisposition      | ContentDisposition       | Value in the 'Content-Disposition' header of EML file.             |
| ContentTransferEncoding | TransferEncoding         | Value in the 'Content-Transfer-Encoding' header of EML file.       |
| Headers                 | dictionary               | A dictionary value containing all other headers.                   |
| MessageID               | string                   | 'Message-ID' header value.                                         |
| MimeVersion             | string                   | 'MIME-Version' header value.                                       |
| ContentID               | string                   | 'Content-ID' header value.                                         |
| Attachments             | MailAttachmentCollection | List of all the attachments present in the EML file.               |

### Instance Method(s)

| **Method**       | **Parameter(s)**                                                             | **Return(s)**                                                        |
|------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------|
| export_as_json   | No parameters needed                                                         | a JSON string containing all the fields of the RxMailMessage object. |
| save_attachments | TargetFolderPath [string] - Folder where the attachments will be downloaded. | does not return a value                                              |

## TextEncoding

A class to perform character encoding - BASE64 and QUOTED-PRINTABLE on MIME part content. It uses the 'quopri' and 'base64' modules in the Standard Python library to decode the encoded strings.

### Static Method(s)

| **Method**         | **Parameter(s)**                                                       | **Return(s)**                         |
|--------------------|------------------------------------------------------------------------|---------------------------------------|
| decode_header      | encoded_string [string] - The encoded MIME header value to be decoded. | the decoded string.                   |
| decode_base64_file | file_contents [string] - The file contents encoded as a base64 string. | The decoded file contents as 'bytes'. |

## MailAttachment

A class to represent an attachment present in the EML file.

### Properties

| **Property**       | **Type**           | **Purpose**                                            |
|--------------------|--------------------|--------------------------------------------------------|
| Name               | string             | Gets/Sets the name of the attachment.                  |
| ContentType        | ContentType        | Gets/Sets the "Content-Type" of the attachment.        |
| ContentDisposition | ContentDisposition | Gets/Sets the "Content-Disposition" of the attachment. |
| Contents           | bytes              | Gets/Sets the contents of the attachment.              |
| ContentID          | string             | Gets/Sets the "Content-ID" of the attachment.          |

### Instance Method(s)

| **Method**   | **Parameter(s)**                                                                                                                                                                                                                                               | **Return(s)**            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| parse_values | contents [bytes] - Contents of the MailAttachment.<br>content_type [ContentType] - Content-Type of the attachment.<br>content_disposition [ContentDisposition] - Content-Disposition of the attachment.<br>content_id [string] - Content-ID of the attachment. | does not return a value. |

## MailAddress

A class to represent an email address.

### Properties

| **Property** | **Type** | **Purpose**                                     |
|--------------|----------|-------------------------------------------------|
| DisplayName  | string   | Gets/Sets the display name of the mail address. |
| Email        | string   | Gets/Sets the email part of the mail address.   |

### Instance Method(s)

| **Method** | **Parameter(s)**                                                                | **Return(s)**            |
|------------|---------------------------------------------------------------------------------|--------------------------|
| parse      | MailAddressString [string] - The string to be parsed into a MailAddress object. | does not return a value. |

## ContentType

A class to represent the Content-Type header of a MIME entity.
 
### Properties

| **Property** | **Type** | **Purpose**                                   |
|--------------|----------|-----------------------------------------------|
| MediaType    | string   | Media type and sub-type of the MIME entity.   |
| Charset      | string   | Character set of the MIME entity.             |
| Boundary     | string   | Boundary value for 'multipart' MIME entities. |
| Name         | string   | Name of the MIME entity.                      |

### Instance Method(s)

| **Method** | **Parameter(s)**                                                                | **Return(s)**            |
|------------|---------------------------------------------------------------------------------|--------------------------|
| parse      | ContentTypeString [string] - The string to be parsed into a ContentType object. | does not return a value. |

## ContentDisposition

A class to represent the Content-Disposition header of a MIME entity.

### Properties

| **Property**     | **Type**        | **Purpose**                                  |
|------------------|-----------------|----------------------------------------------|
| DispositionType  | DispositionType | Disposition type of the MIME entity.         |
| FileName         | string          | File name of the MIME entity.                |
| CreationDate     | string          | Date when the MIME entity was created.       |
| ModificationDate | string          | Date when the MIME entity was last modified. |
| Size             | integer         | Size of the MIME entity.                     |

### Instance Method(s)

| **Method** | **Parameter(s)**                                                                              | **Return(s)**            |
|------------|-----------------------------------------------------------------------------------------------|--------------------------|
| parse      | ContentDispositionString [string] - The string to be parsed into a ContentDisposition object. | does not return a value. |

## Logger

A class to manage the configuration and generation of logs during EML file processing.

### Static Method(s)

| **Method**        | **Parameter(s)**                                                                                                                                                                                                                                           | **Return(s)**                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| set_configuration | logging_mode [LoggingMode] - Denotes where the generated logs have to be stored or printed.<br>target_folder [string] - The target folder where the log file must be created. If the 'logging_mode' is 'LoggingMode.CONSOLE', an empty string is returned. | the complete path to the log file generated. |
| log_entry         | message [string] - message to be logged<br>logging_level [LoggingLevel] - Type of message being logged.                                                                                                                                                    | does not return a value                      |


## Custom Enumerations

Given below are the custom enumerations exposed by the library.

### TransferEncoding

Enumeration to represent the different content encoding methods supported.

| **Name**         | **Value** |
|------------------|-----------|
| BASE64           | 1         |
| SEVEN_BIT        | 2         |
| EIGHT_BIT        | 3         |
| QUOTED_PRINTABLE | 4         |

### EntityType

Enumeration to represent the different MIME entity types supported.

| **Name**   | **Value** |
|------------|-----------|
| ATTACHMENT | 1         |
| TEXT       | 2         |
| MIME_PART  | 3         |

### DispositionType

Enumeration to represent the different content disposition types supported in MIME.

| **Name**   | **Value** |
|------------|-----------|
| ATTACHMENT | 1         |
| INLINE     | 2         |

### LoggingLevel

Enumeration containing the different levels of logging available for a module.

| **Name** | **Value** |
|----------|-----------|
| DEBUG    | 1         |
| INFO     | 2         |
| ERROR    | 3         |
| CRITICAL | 4         |

### LoggingMode

Enumeration containing the different modes of logging available for a module.

| **Name** | **Value** |
|----------|-----------|
| CONSOLE  | 1         |
| FILE     | 2         |
| NONE     | 3         |

## Custom Exceptions

Given below are the list of custom exceptions exposed by the library.

| **Exception**           | **Purpose**                                                               |
|-------------------------|---------------------------------------------------------------------------|
| InvalidEncodingError    | To report Invalid Encoding errors.                                        |
| FileMissingError        | To report when file is missing at the specified location.                 |
| IncompleteHeaderError   | To report when an incomplete header line is found in the EML file.        |
| FolderNotAvailableError | To report when a given folder is not available at the specified location. |

## Custom Collections

The library exposes the following custom collection classes.

| **Collection**           | **Purpose**                                                |
|--------------------------|------------------------------------------------------------|
| MailAddressCollection    | A Collection to hold a list of MailAddress instance(s).    |
| MailAttachmentCollection | A Collection to hold a list of MailAttachment instance(s). |

### Instance Method(s)

| **Method**     | **Parameter(s)**                                                                            | **Return(s)**                              |
|----------------|---------------------------------------------------------------------------------------------|--------------------------------------------|
| append         | item[MailAddress or MailAttachment] - the item to be appended to the end of the collection. | does not return a value.                   |
| length         | no parameter(s).                                                                            | number of items in the collection.         |
| export_as_list | no parameter(s).                                                                            | the items in the collection as a new list. |
