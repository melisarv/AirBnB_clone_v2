#/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
import MySQLdb


class TestDBStorage(unittest.TestCase):
    '''this will test the FileStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Holby"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()
        cls.storage.save()

    @classmethod
    def teardownClass(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def test_db_insert(self):
        """ tests if database working """

        database = MySQLdb.connect(host="localhost",
                                   port=3306,
                                   user="hbnb_dev",
                                   passwd="hbnb_dev_pwd",
                                   db="hbnb_dev_db")

        cursor = database.cursor()

        cursor.execute("SELECT * FROM states")
        rows = cursor.fetchall()
        before = len(rows)
        print(before)

        state = State()
        state.name = "brent"
        state.save()

        cursor.execute("SELECT * FROM states")
        rows = cursor.fetchall()
        after = len(rows)
        print(rows)


        self.assertTrue(before + 1 == after)

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 1, "fix pep8")

    def test_all(self):
        """tests if all works in File Storage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._DBStorage__objects)

    def test_new(self):
        """test when new is created"""
        storage = DBStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Betty"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        self.assertIsNotNone(obj[key])


if __name__ == "__main__":
    unittest.main()
