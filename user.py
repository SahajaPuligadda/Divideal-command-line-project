
class User:

    __id = None
    __name = None
    __email = None
    __phone = None

    def __init__(self, idx, name, email, phone):
        self.__id = idx
        self.__name = name
        self.__email = email
        self.__phone = phone

    def setId(self, idx):
        self.__id = idx

    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email

    def setPhone(self, phone):
        self.__phone = phone

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPhone(self):
        return self.__phone
