from .Text_Encoding import TextEncoding
from copy import deepcopy


class MailAddress:
    """
        A class to represent an email address.
    """
    def __init__(self):
        self.DisplayName = str()
        """The display name component of an email address."""
        self.Email = str()
        """The complete email address."""

    def parse(self, MailAddressString: str):
        """
            A function to parse the received input string and set the properties of the 'MailAddress' object.
            :param MailAddressString: String value to be parsed into a 'MailAddress' object.
            :returns: no value(s).
        """
        MailAddressString = MailAddressString.strip()
        if MailAddressString.find("<") == -1:
            self.Email = MailAddressString
        else:
            index = MailAddressString.find("<")
            name_value = MailAddressString[0:index].strip()
            name_value = name_value.replace("\"", "")
            self.DisplayName = TextEncoding.decode_header(name_value)
            indexOne = MailAddressString.find(">")
            self.Email = MailAddressString[index + 1:indexOne].strip()

    def __str__(self) -> str:
        if self.DisplayName != str():
            return self.DisplayName + " <" + self.Email + ">"
        else:
            return self.Email


class MailAddressCollection:
    """
    A Collection to hold a list of MailAddress instance(s).
    """
    def __init__(self):
        self.__addresses = list[MailAddress]()
        """Iterable to hold the MailAddress instance(s)."""

    def append(self, address: MailAddress):
        """
        A function to insert a MailAddress instance to the end of the collection.
        :param address: MailAddress object to be added to the end of the collection.
        :returns: no value(s).
        """
        self.__addresses.append(address)

    def __str__(self) -> str:
        mail_addresses = list()
        for address in self.__addresses:
            mail_addresses.append(str(address))

        return ";".join(mail_addresses)

    def length(self) -> int:
        """
        A Function to return the number of 'MailAddress' items in the collection instance.
        :returns: the number of items in the collection.
        """
        return len(self.__addresses)

    def export_as_list(self) -> list:
        """
        A function to export MailAddressCollection as a list of 'MailAddress' instances present in the collection.
        :returns: A new list containing all the 'MailAddress' instance present in the collection.
        """
        return deepcopy(self.__addresses)
