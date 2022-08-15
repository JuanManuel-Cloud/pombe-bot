class Person:
    def __init__(self,
                 name,
                 lastname,
                 birthday,
                 custom_greeting):
        DEFAULT_GREETING = f'Hola, feliz cumpleaños {name} {lastname} 🥳🥳🥳!!!'

        self.name = name
        self.lastname = lastname
        self.birthday = birthday
        self.custom_greeting = custom_greeting

    def get_greeting(self):
        return self.custom_greeting
