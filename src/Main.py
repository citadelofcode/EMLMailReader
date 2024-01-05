if __name__ == "__main__":
    from Mail_Reader import MailReader
    from Rx_Mail_Message import RxMailMessage
    from Mail_Address import MailAddress

    reader = MailReader()
    message: RxMailMessage = reader.get_email("./../Sample-Emails/Sample-Email-1.eml")
    FromAddress: MailAddress = message.From
    print("From address is:", FromAddress.tostring())
    print("Number of headers captured:", len(message.Headers))
