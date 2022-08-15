import json
from pymongo import MongoClient
from models.person import Person

client = MongoClient()
db = client.birthdays_db
birthday_collection = db.birthday


def add_one_birthday(dni,
                     name,
                     lastname,
                     birthday,
                     alias=None,
                     custom_greeting=None):
    person_serialized = Person(name, lastname, birthday).__dict__
    person_serialized['_id'] = dni
    result = birthday_collection.insert_one(person_serialized)
    return result


# add_one_birthday("12345678", "test1", "test1", "01-01-01")
def say_happy_birthday(dni):
    return birthday_collection.find_one({'_id': dni})['custom_greeting']


def delete_one_birthday(dni):
    return birthday_collection.delete_one({'_id': dni})


def get_all_birthdays():
    return birthday_collection.find()[0]