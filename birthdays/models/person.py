from webbrowser import get


class Person:

    def __init__(self,
                 name,
                 lastname,
                 birthday,
                 alias=None,
                 custom_greeting=None):
        DEFAULT_GREETING = f'Hola, feliz cumpleaños {name} {lastname} 🥳🥳🥳!!!'

        self.name = name
        self.lastname = lastname
        self.birthday = birthday
        self.alias = alias
        if custom_greeting == None:
            self.custom_greeting = DEFAULT_GREETING
        else:
            self.custom_greeting = custom_greeting

    def get_greeting(self):
        return self.custom_greeting
