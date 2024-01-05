class MailAddress:
    def __init__(self):
        self.DisplayName = ""
        self.Email = ""

    def parse(self, MailAddressString: str):
        MailAddressString = MailAddressString.strip()
        if MailAddressString.find("<") == -1:
            self.Email = MailAddressString
        else:
            index = MailAddressString.find("<")
            self.DisplayName = MailAddressString[0:index].strip()
            indexOne = MailAddressString.find(">")
            self.Email = MailAddressString[index + 1:indexOne].strip()

    def tostring(self) -> str:
        if self.DisplayName != "":
            return self.DisplayName + " <" + self.Email + ">"
        else:
            return self.Email
