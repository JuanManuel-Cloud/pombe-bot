from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from models.person import Person
from models.response import Response
from models.response import Status


client = MongoClient()
db = client.birthdays_db
birthday_collection = db.birthday


def add_one_birthday(dni,
                     name,
                     lastname,
                     birthday,
                     custom_greeting):
    person_serialized = Person(name, lastname, birthday, custom_greeting).__dict__
    person_serialized['_id'] = dni
    try:
        birthday_collection.insert_one(person_serialized)
        return Response(Status.OK, 'Cumpleaños seteado con éxito 🥳🥳🥳!!!')
    except DuplicateKeyError:
        print('\n\nDuplicateKeyError\n\n')
        return Response(Status.FAIL, 'No se insertó el cumpleaños, motivo: ese usuario ya existe 💀💀💀')


# add_one_birthday("12345678", "test1", "test1", "01-01-01")
def say_happy_birthday(dni):
    return birthday_collection.find_one({'_id': dni})['custom_greeting']


def delete_one_birthday(dni):
    return birthday_collection.delete_one({'_id': dni})


def get_all_birthdays():
    return birthday_collection.find()[0]