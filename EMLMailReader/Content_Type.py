import json


class ContentType:
    """
        A class to represent the Content-Type header of a MIME entity.
    """
    def __init__(self):
        self.MediaType = "text/plain"
        """Media type and sub-type of the MIME entity."""
        self.Charset = "us-ascii"
        """Character set of the MIME entity."""
        self.Boundary = str()
        """Boundary value for 'multipart' MIME entities."""
        self.Name = str()
        """Name of the MIME entity."""

    def parse(self, ContentTypeString: str = "text/plain; charset=us-ascii"):
        """
            A function to parse the given string and create a ContentType object. As per RFC 2045, a 'Content-Type' header contains a default value of 'text/plain;charset=us-ascii' in case of Content-Type header being absent or having an invalid value.
            :param ContentTypeString: The Content-Type string to be parsed.
            :returns: no value(s).
        """
        ContentTypeString = ContentTypeString.strip()
        if ContentTypeString.find(";") != -1:
            ContentTypeValues = ContentTypeString.split(";")
            self.MediaType = ContentTypeValues[0]
            for index in range(1, len(ContentTypeValues)):
                Current_Value = ContentTypeValues[index]
                index_one = Current_Value.find("\"")
                if index_one == -1:
                    key = Current_Value.split("=")[0]
                    value = Current_Value.split("=")[1]
                else:
                    key = Current_Value[0:index_one]
                    key = key.strip("=")
                    Current_Value = Current_Value.replace(key + "=\"", "")
                    index_two = Current_Value.find("\"")
                    value = Current_Value[0:index_two]

                if key.lower().strip() == "charset":
                    self.Charset = value.strip().lower()
                elif key.lower().strip() == "boundary":
                    self.Boundary = value.strip()
                elif key.lower().strip() == "name":
                    self.Name = value.strip()
                else:
                    raise Exception("Invalid parameter present in Content-Type header")
        else:
            self.MediaType = "text/plain"
            self.Charset = "us-ascii"

    def __str__(self) -> str:
        return_data = dict()
        return_data.update({
            "Media-Type": self.MediaType,
            "Character-Set": self.Charset,
            "Name": self.Name,
            "Boundary": self.Boundary
        })

        return json.dumps(return_data)
