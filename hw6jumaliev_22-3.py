import re

class Data:
    def init(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

data = open('MOCK_DATA.txt', "r")
content = data.read()
data.close()
with open("MOCK_DATA.txt", "r", encoding='UTF-8') as file:
    file.read()
    full_name_mock = re.findall(r"\b[A-Z][A-Za-z-]+\s[A-Za-z\' ]+\b", content)
    with open("full_name", "w", encoding='UTF-8') as file:
        for i in full_name_mock:
            file.write(f"{i}\n")

    colors_mock = re.findall(r"[0-9A-Fa-f]{6}", content)
    with open("colors", "w", encoding='UTF-8') as file:
        for i in colors_mock:
            file.write(f'{i}\n')

    file_name_mock = re.findall(r"\b[\w]+@[\w\-]+(\.[\w]+)+\b", content)
    with open("file_name", "w", encoding='UTF-8') as file:
        for i in file_name_mock:
            file.write(f"{i}\n")
            print(i)

    email_mock = re.findall(r'\b([\w\-]+)[@][\w]+(\.[\w]+)+', content)
    with open("email", "w", encoding='UTF_8') as file:
        for i in email_mock:
            file.write(f'{i}\n')