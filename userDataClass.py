DEFAULT_CLASS_NUMBER = "WCY23IY1S1"
DEFAULT_GROUP_NUMBER = "I3Y1S1"

class UserData:
    classNumber = ""
    groupNumber = ""
    name = ""
    surname = ""

    def __init__(self) -> None:
        self.classNumber = DEFAULT_CLASS_NUMBER
        self.groupNumber = DEFAULT_GROUP_NUMBER
        pass

    def set(self, name, surname, classNumber, groupNumber ):
        self.name = name
        self.surname = surname
        self.classNumber = classNumber
        self.groupNumber = groupNumber

        return self