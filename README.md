# EMLMailReader

This Python library streamlines the process of working with EML files. Effortlessly extract crucial details like sender and recipient information, subject lines, email bodies, and a complete list of headers. For in-depth analysis, export the parsed data in the widely-used JSON format. Additionally, the library provides the convenience of downloading any associated attachments directly to your local machine for further processing.

## Table of Contents

- [Installation](#installation)
- [Example Usage](#example-usage)
- [Modules Used](#modules-used)
- [Documentation](#documentation)

## Installation

To install the library locally, make sure you have *python* and *pip* installed in your system, and then run the below command.

```
pip install emlmailreader
```

## Example Usage

Here's a sample code to leverage **EMLMailReader** in parsing an EML file and extract information contained within.

```
from EMLMailReader import MailReader, RxMailMessage
  
reader: MailReader = MailReader()
message = reader.get_email("COMPLETE_EML_FILE_PATH")
if isinstance(message, RxMailMessage):
    json_string = message.export_as_json()
    print(json_string)
```

In this context, the term "COMPLETE_EML_FILE_PATH" indicates the complete path of the .EML file intended for processing. Running this code will output a JSON string resembling the one provided below.

```
{
    "From": "Mahesh Kumaar Balaji <maheshkumaar.balaji@outlook.com>",
    "Subject": "Test-Email-5",
    "Message-ID": "<TY3P286MB27238431EA4EE3F05821CDD7E4312@TY3P286MB2723.JPNP286.PROD.OUTLOOK.COM>",
    "IsMultiPart": true,
    "Mime-Version": "1.0",
    "Date": "Fri, 22 Mar 2024 22:52:24 +0000",
    "Headers": {
        "Received": "from TY3P286MB2723.JPNP286.PROD.OUTLOOK.COM([fe80::9b2e:a11f:e0f1:779c]) by TY3P286MB2723.JPNP286.PROD.OUTLOOK.COM([fe80::9b2e:a11f:e0f1:779c%4]) with mapi id 15.20.7409.023; Fri, 22 Mar 202422:52:24 +0000",
        "ARC-Seal": "i=1; a=rsa-sha256; s=arcselector9901; d=microsoft.com; cv=none;b=R7Ad8lvJlkvb3ov//iWvUp0UNJBNSuPikhA9JmxzD+mzmKSZBG2O9N6DS3zgrY3FuysknY3gVzCwODU1D5toiiJDJrWOGACizAmxZ6PwB3oCyA6BOGS3c4XIoO9PoN5iibHVgaDYFB+ktslKH0ydWevOFfPH7IQ9jj4yh8hJRm3HlostxLmYufsWtVm6VV16AN222F/31GnJn+ka8Xw5HiEeTooZw1xApc8FF+2ZFgpQWXwQF188LxgPawMRWtsrAxlcGfQ0lZKvOH2xNbyMOwKDwYRiOfjCtIO9jmuhlU+dFOXm5Xsanu9R9WSe8r/s40EU+ym78ZF+id59f4SKfg==",
        "ARC-Message-Signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=microsoft.com;s=arcselector9901;h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-AntiSpam-MessageData-ChunkCount:X-MS-Exchange-AntiSpam-MessageData-0:X-MS-Exchange-AntiSpam-MessageData-1;bh=GZNu+uY4tmf+Dg5UG62PQ4Lx0mkpwlqJV6YZapikb3Y=;b=BPZcx+/mDa/IsQohNF/q8w/Bwdf/xOyrOetQAAgq8WbY8I/0pwd4yuCdEyR5yOShyEyiQZYQdTCLGSXUO6e4ALY7/eu2XUyY6BOmbk7piCMkfWHDCh0dr0dbVHLHV7aAOm+FrNY+id5+6FTu8oTwFLF2gOS5Zdm92VYUgOWJseyZBslgVZGI6lLrgX3zyvEO5YdsZW1rUDuoK1m7h6sZcaYWGdhaZmOZxhGADLQjGKiSxuqXa6gj219qiOshbuYAwUbBrZUlwe//M0wqU7qMpD5HFRZGTnrtFHALX5TW6Aak584tV7SctKIclQNcqiyPXZkPEwYcx35v9EZmBlO/Xg==",
        "ARC-Authentication-Results": "i=1; mx.microsoft.com 1; spf=none; dmarc=none;dkim=none; arc=none",
        "Authentication-Results": "spf=pass (sender IP is 52.103.66.3)smtp.mailfrom=outlook.com; dkim=pass (signature was verified)header.d=outlook.com;dmarc=pass action=noneheader.from=outlook.com;compauth=pass reason=100",
        "Received-SPF": "Pass (protection.outlook.com: domain of outlook.com designates52.103.66.3 as permitted sender) receiver=protection.outlook.com;client-ip=52.103.66.3; helo=OS0P286CU011.outbound.protection.outlook.com;pr=C",
        "DKIM-Signature": "v=1; a=rsa-sha256; c=relaxed/relaxed; d=outlook.com;s=selector1;h=From:Date:Subject:Message-ID:Content-Type:MIME-Version:X-MS-Exchange-SenderADCheck;bh=GZNu+uY4tmf+Dg5UG62PQ4Lx0mkpwlqJV6YZapikb3Y=;b=bdqw84toCecsyc1+gQcqkfjw0blT4jfKHQMqmrRiVodhnIU9OcGUzYxsjPjB0w8scHu89+AL12fp4/a/7uLPI9HfoV+VQfWLfkPAJIjrq4dB/RC/pTrXvX7W1ROmQt1Toj5SRss1fXQHYjONBaAOmmHrNstjB3g9gIumNor+fussHVY7lhrj37bg1EjGUrQL5PQ1o4y+29U6Q4UMI3V+ESNgbyRMfqW8BXAaCy6iDHOZuFWS1562hjtDTYHqN9cx+e4X3sY+Z2q+ac3TvxDt5fjbd8ji/hNzAPgIW6ml4XZExyVdWZdNvfY95yvitpO7mfdOAAH8ac5XrYEDJEP/5A==",
        "Thread-Topic": "Test-Email-5",
        "Thread-Index": "AQHafKt91GiqauDZ2k6oNt2I9lOJUQ==",
        "Accept-Language": "en-US",
        "Content-Language": "en-US",
        "X-MS-Has-Attach": "yes",
        "X-MS-TNEF-Correlator": "",
        "x-ms-exchange-messagesentrepresentingtype": "1",
        "x-tmn": "[l/1bKlKzlZ0E7EbjcS9hwa/2cgrHB+/VlSZ7iyZk781u/HP4Jnoh9YgOyrgwIhqi]",
        "x-ms-traffictypediagnostic": "TY3P286MB2723:EE_|TYVP286MB3117:EE_|CY4PEPF0000EE38:EE_|DM6PR14MB3821:EE_|DS0PR14MB6759:EE_",
        "X-MS-Office365-Filtering-Correlation-Id": "c7b6508a-41fb-42f2-64e0-08dc4ac2c003",
        "x-ms-exchange-slblob-mailprops": "vQx3cGk1+xyRxwYZil1vsotul+JhzeXjOetMehWWNQc3RBwDUMnxMyMQdXovrsbBYoN2ilpDRYa8EJmdvNygc9d+iQFfmttE/VEs+ZXSjO/MwuDUAtE6U598HgyVcDNsFvH2J+hFRm/M9GR/UEL1t0UIu6z6SWsHdN8TgbYY/C6yKdJUUYZFbDII9tA44eBoctrq2RxnGJOfHF/cj0LTHbfbdfbggvYScilDgqQnIdpYk0ATid2r3orVfRpssLeNOZs9E+lu1AfBz+RA+Q4Mvdaxo6FNLqum7V1FQ0KlisRCHwup0c3Mzo+gcT2NF29JmgLHxJTl1F5kwglKSaF/CECZGmSjANB6dYn5oXxvVD6llBR4+uRQKAJq7LPCzSIiBExqlcW44Tzax4/u3FFYB8Jl4vlvQBfvpEVUItVbsCj/1UueHEcSoFIjKI+/jymWUFZFxNhd03hPR+mZDS9Yo0XYWFk4r2pD16JwjrxLURQknhVQxCMi5ZUsmQNSq7B8ch+iMI3Qij3WEliUDGYz5B5ZG1ml96tPozMoLriT+yX9W7OSt165CMHOG/Ieodk/okOCpJ9DU/J06xydLKc6jFcQxqCVXK5ocadafbXtuCo=",
        "X-Microsoft-Antispam-Untrusted": "BCL:0;",
        "X-Microsoft-Antispam-Message-Info-Original": "WJhbZQS//9SLbKoUNFTVyepPwz5uiIVDkkWoJgOXtJj24Og/4MniQA8ZtaRIMh7cSWdcWvMq/KxY3cLO/R0j3MKrpQtAe8mLgb3Q0+pt5gF1hafS0sz6c+lIRjUqFF2JrwBLJupwy/FtnhBB3C+THuv1uG3OPEjIt1yOkpuHtFrhRQz5T6iDwwDzZYumH/bUhoPZoWzQ2tKLXJqPj0eiyW1Lp8Sdra3vQXd/93VED4cYy/7SLHNpw6Bp8H6PTbCyfuTPPEMMsz417pQsX744kL35fEwSHPsVZYArsnBgFuo8BDyq5c1mixC9hCisAttjpBVdOxDq/yDssriZthFJ7rNl1eOsx1VfrDeEq+UNMCcWCXaNLGr1ZM4T7p2BpYYikXgssEvIk/i6+hfr9vhmQNAmwWvJqx6XHd6UeOvHmg7x8oJjuaj9IA9PxvChxiIewidRWTuaAfpqJhVC/R3ipwWjyLDxrxFhb+jHRGcoiD/hWZpV0U4Yt4nf+HsayTlcdFDmqLQOsnfrXaCJLAPPCrJDwqwAumQgPPdG8p+TOKOxd1rtfGKmZa9Z3HSedmsS6pWU6XgPSVWA8R++2muzrycQ6k/4fp0HSNurI20/IpWwQudZUa9hOxjxzJoAjqAQ/uRb1kG0JfWTdl5AmC3nutlPy25zK+zr3pvicwvcCYQ=",
        "X-MS-Exchange-AntiSpam-MessageData-Original-ChunkCount": "1",
        "X-MS-Exchange-AntiSpam-MessageData-Original-0": "TbEsuTxprCNx7VztYnj6L5JwTs3JG7TjZ520Vm77MRkVCIvgUwK5WVzu4XUwmulHeQSSsDdt74KwaDY1Nn9F4C8MF/B/v0MtA3QIKPIhIZwO0Y+u8NVrb/A03fpIhCKiU6DvPZXos0kb5ZydFwgwc5GP+WrRcEtmsMFpgpIVkqdJqBDwcqzf0Qac5cy0ojn9K6PzW2RhGTGTYdh8M/86azL/dHwUa+QKLDH35OjtkcDYTwKETWzQaZK5skNLZl/D+clx0qsB1AYEm2i23s5lV4WSonwjV3+bksjmg5YEQDZDrrI6c789IJYL0LO6BB8OYPA1FMkpLnW3vv6YH48UpphjrOJo3KoYnl1vi8Hrb+ZR3NblFfgDNE6a+OoluTLg/kL24dsNSxP0mDDkd1selUlDUmASDkrzgOvF9T4VwUirtTlLbxVVCZWGHeQjL71BC8zW6AG0lcX5yyf/8nFp2YzTJxg78I1PUr3bLF7L9JD3BNfCCYWJUexGAF7HNl3mRRkLjC8ksBqbbEleQSNKSS/86QkOu0EbWJLkL/RYhseO61OlrOpi4p2k2NDwW/2tgqaV8QAg7W++mdxDmwe21a6fWAA36vIMwPJxzkDsNL8/0wEvlr77PKtYZ23wamBvLJZpYM7zWasmimLHu93curq2tKne9Xvob/IpRodeke9AXaPDmZUeV4nyEb2ur9Gj5tggIsv1/I/qAakPzzFtBKmyRZ/jWBeOQIUarVViEJEPaCH8VuJk2M664uwbIsdhZixBMd93FB7BpuIMVQtylBhb9VxwEa0Yuiq1uUd/cv5sqL6wZtBcKXiF1jRirkfShNO+gC31Q6ne0Gl+1dem6jXGk85fz7X2ZcpTMgd3Cv06wY9Qly4lLyLJETSs8Zk0ry/1s0GfrweD/AZEsufFGJv8aTjW3P5kAsFypVKdqSuaFZPFBJ+agsvUjqRuPKu4UNCimLJ+R/Kj3YxY22mza465+zw1K9/LC9H5ked+J17zDTp/fDEHyJD1m4HIwDOvTBNl/SN51/2Q5Jx1yPY0nkubfHpAVOSnIDaHfoQt0rbW67wesFy+cp6YK1YW8ZNt72yPYelCu8PorX2PGeEiscnQS2mL4iOEIQ5jNEJcX7Vz3JbqWaIsr64EiuvO/Ce0mZJuFrLhTG0kMb+L0DI7RhUiKSsb1q2OMNawWtb1m9z5B/5fSFoETsgX0FYXdZcQq0EtwPkJJrDW8mn3fNiZM+f1yvzLFNenUSRoAII0rSUBTkj1Q/Q47SaASEQS++7z6kSRgKsk+6VUuWIo2m5eFdwvbs0ZFI74iY3ekWdYc2UV4521u4u3rdkwB/YUcONQ3MrwuBVLS+YojdadDc+VPQ==",
        "X-MS-Exchange-Transport-CrossTenantHeadersStamped": "DM6PR14MB3821",
        "Return-Path": "maheshkumaar.balaji@outlook.com",
        "X-MS-Exchange-Organization-ExpirationStartTime": "22 Mar 2024 22:52:28.5326(UTC)",
        "X-MS-Exchange-Organization-ExpirationStartTimeReason": "OriginalSubmit",
        "X-MS-Exchange-Organization-ExpirationInterval": "1:00:00:00.0000000",
        "X-MS-Exchange-Organization-ExpirationIntervalReason": "OriginalSubmit",
        "X-MS-Exchange-Organization-Network-Message-Id": "c7b6508a-41fb-42f2-64e0-08dc4ac2c003",
        "X-EOPAttributedMessage": "0",
        "X-EOPTenantAttributedMessage": "c09486f1-4e60-48d9-a3ca-1af438ae8849:0",
        "X-MS-Exchange-Organization-MessageDirectionality": "Incoming",
        "X-MS-Exchange-Transport-CrossTenantHeadersStripped": "CY4PEPF0000EE38.namprd03.prod.outlook.com",
        "X-MS-Exchange-Transport-CrossTenantHeadersPromoted": "CY4PEPF0000EE38.namprd03.prod.outlook.com",
        "X-MS-PublicTrafficType": "Email",
        "X-MS-Exchange-Organization-AuthSource": "CY4PEPF0000EE38.namprd03.prod.outlook.com",
        "X-MS-Exchange-Organization-AuthAs": "Anonymous",
        "X-MS-Office365-Filtering-Correlation-Id-Prvs": "5468b413-76b6-41ff-6b43-08dc4ac2bdc0",
        "X-MS-Exchange-Organization-SCL": "-1",
        "X-Microsoft-Antispam": "BCL:0;",
        "X-Forefront-Antispam-Report": "CIP:52.103.66.3;CTRY:JP;LANG:en;SCL:-1;SRV:;IPV:NLI;SFV:SFE;H:OS0P286CU011.outbound.protection.outlook.com;PTR:mail-japanwestazolkn19011003.outbound.protection.outlook.com;CAT:NONE;SFS:(13230031);DIR:INB;",
        "X-MS-Exchange-CrossTenant-OriginalArrivalTime": "22 Mar 2024 22:52:28.2201(UTC)",
        "X-MS-Exchange-CrossTenant-Network-Message-Id": "c7b6508a-41fb-42f2-64e0-08dc4ac2c003",
        "X-MS-Exchange-CrossTenant-Id": "c09486f1-4e60-48d9-a3ca-1af438ae8849",
        "X-MS-Exchange-CrossTenant-RMS-PersistedConsumerOrg": "00000000-0000-0000-0000-000000000000",
        "X-MS-Exchange-CrossTenant-rms-persistedconsumerorg": "00000000-0000-0000-0000-000000000000",
        "X-MS-Exchange-CrossTenant-AuthSource": "CY4PEPF0000EE38.namprd03.prod.outlook.com",
        "X-MS-Exchange-CrossTenant-AuthAs": "Anonymous",
        "X-MS-Exchange-CrossTenant-FromEntityHeader": "Internet",
        "X-MS-Exchange-Transport-EndToEndLatency": "00:00:09.0388826",
        "X-MS-Exchange-Processed-By-BccFoldering": "15.20.7409.009",
        "X-Microsoft-Antispam-Mailbox-Delivery": "wl:1;pcwl:1;ucf:0;jmr:0;auth:0;dest:I;ENG:(910001)(944506478)(944626604)(920097)(811239)(255002)(410001)(930097)(140003);",
        "X-Microsoft-Antispam-Message-Info": "sk7bTTPTfs+DIAFkVCwxr5/5fLcpTVkL0qf0Bi+NaaGSZLw4SZ/bmh+l9chV1hfaIpbN/HHfSg2ZJMV6U5Ix603saZ8hgmkiykS1Kne/mqhg5+Z9SPU+mdREEHqrJpwh23riSba+xIkSqbhL80DeHTdasAnTX8Dof+lG9U5IGQWIpH6kKONTU2OrdstdQ42KFyM7E2AODrKkUm74DIsv/EyvCDvvByu0mv5Gxq/CSV34bccvtJ6hAgiaD26MucWCT9KlXFx4T6pON/tG+TeA1qQ4MPvD9e+4S1/LAqgx9Kmj5eMEZj0EkNNNlC1qvY0XHZfgI950L+ODvW4FAKjbZNv9Wzgo2ObVcnfkMJ4PpGDux6TySKlNCjX4Vuul2Ei2/wIUhLMdSa25HnKbtjDz6SHjnhU5X+sVFrvSCNu7LQkDvUVomMd73eJp/S1sP+SqFrlqRTyq1MqOp9I2jFA4/EDleavryeWU9fZooT3L+vhOlf217nxTqp89b3y7ddD1W3FT/u+oagRF0hr8a304wDx2bxNrJ1HFjOW11ISlpi6/h+pRNkQkg0d39fy8ySMZeZ0f9qISKjcEdy8wxuBolYw+nNLjn/GxD2F4gPrsNq5Hk3Yv4YdVj9ZsMHL4ovtLRDS5R9oYC9UnvLQGF9M4k20I2ThQHQd5CKKM3S71JsAyog9Iw9fZjUqX5R3JQt6rm0bgMnr6++YYDUCGVDn//n5ABXeenMwMkLwt/wSXSfyG7Pr9i2YdGK23lm599VwyBZpkncdaVyvt8ytTjTh0fja5AIZZN+OnhgTtPHn8gPyjp9bMxRDnWaRrSwm68B89SpwyJahwgbnAA7LVuQdzHiHiknXJj6Y5zfsYH2M1D+zjGSlG4VKp9FtX0UPU0v+Nd3AHqlZ+74/BkMulJyAdHeSbltrwTmIMsXuVUDLu9d6/GejtZDQF+7fRSKZ3HpBv7BuXUNivS2wjsmLEChqcqKcakUovv/LRy0LvmoEQfeaIUBStK3oIA7xj6YVEZP00AvwAql2dNDJR+cmNF+QKtl0l+Ya6yhN7K2kqjOD1rTLCnpkgV+IwcTQT8J1S+66vw0FaxLAYQ783po80brQFQZ9Kjb/COeQhw+FoEtW+2RxsRR+qF9bPEx6pbyL6Sb95POOBVD1k5zN/YU0up1SxRN7qQbEIfrSBRgj1A0Fg8Wsq0mp7JUqc7at9hGQfT6wc6KFY1k944zObpfdgGlvHGjXlMi4Xy53Sx9GOzIozBZ4pJYyBQOjKLhxZ7KU4+ISBgA+sGJkShlAkDSI8HhHQTWKE6GOT1oSR/7w93q6nnRT8XUj0u82+2tivgwuIYV7XjNYqNmTi3wlKlu08Aw9+ubI5fepHhrgkd8NCk/5cM1+aTpGi27ywBicYnqsE4cj7Zrn460R/mq6LPtdXRIFCyJ9LRWqI2Se5l6spGtmH5PQLwMlOcTGVBs0Nf1FxT62toD7hJfZgToICylTLccGx+40EuwAYaX5/7alPxtzZ1srSCpTiDDUeKJdx0b7mt3791RSpDWiaWSDiGntUXkojhoc/QTEDQktJhwo/MNWksOp3zhgM4t4cOEFTDsci3VxN2apVd0qxEEHXt+KhB5kovoSFVPqLcnE4EqwyrCQA1nXeSJzc1umLm87yXkUmcDfIyHDKrkyr51rOAs+dsONqd5GlLGj8ibYhcuY9iQyUfqlWeliImzKTAjbVG4vncWfu02F+1mqfESgBfD13V93Dt5ZWb3R1cnzd1b9tdlUf3x6fhvgsd+iYQyq6x7V02x4eKBB44LdJHbIp6OP+tKfmY/rjO4J9CmnzyQr7PoPBuQSyFd0+CnvAen1bkWaPJwV2J+v/Em/3Yy713Wg7MCC63Q=="
    },
    "Content-Type": "multipart/mixed; charset=us-ascii",
    "To": "Mahesh Kumaar Balaji <maheshkumaar.balaji@mkbdgs.com>",
    "Cc": "",
    "Bcc": "",
    "Reply-To": "",
    "Attachment-Count": 1
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

For complete documentation, check [Documentation](/documentation.md) file of this repository.