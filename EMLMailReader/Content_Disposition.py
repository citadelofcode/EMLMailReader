import json
from .Enumerations import DispositionType


class ContentDisposition:
    """
        A class to represent the Content-Disposition header of a MIME entity.
    """
    def __init__(self):
        self.DispositionType: DispositionType = DispositionType.ATTACHMENT
        """Disposition type of the MIME entity."""
        self.FileName = ""
        """File name of the MIME entity."""
        self.CreationDate = ""
        """Date when the MIME entity was created."""
        self.ModificationDate = ""
        """Date when the MIME entity was last modified."""
        self.Size = 0
        """Size of the MIME entity."""

    def parse(self, ContentDispositionString: str):
        """
            A function to parse the given string and create a ContentDisposition object.
            :param ContentDispositionString: The Content-Disposition string to be parsed.
            :returns: no value(s).
        """
        ContentDispositionString = ContentDispositionString.strip()
        if ContentDispositionString.find(";") != -1:
            ContentDispositionValues = ContentDispositionString.split(";")
            if (ContentDispositionValues[0].strip()).lower() == "inline":
                self.DispositionType = DispositionType.INLINE
            else:
                self.DispositionType = DispositionType.ATTACHMENT
            for index in range(1, len(ContentDispositionValues)):
                Current_Value = ContentDispositionValues[index]
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

                if key.lower().strip() == "filename":
                    self.FileName = value.strip()
                elif key.lower().strip() == "size":
                    self.Size = int(value.strip())
                elif key.lower().strip() == "creation-date":
                    self.CreationDate = value.strip()
                elif key.lower().strip() == "modification-date":
                    self.ModificationDate = value.strip()
                else:
                    raise Exception("Invalid parameter present in Content-Disposition header")
        else:
            self.DispositionType = ContentDispositionString.strip()

    def __str__(self) -> str:
        return_data = dict()
        return_data.update({
            "Disposition-Type": self.DispositionType.name,
            "File-Name": self.FileName,
            "Creation-Date": self.CreationDate,
            "Modification-Date": self.ModificationDate,
            "Size": self.Size
        })

        return json.dumps(return_data)
