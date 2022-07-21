import json
import unittest
from project import app
from project.persistence.products_dao import get_products


class TestApp(unittest.TestCase):
    token=''

    def test_get_user_products(self):
        result=get_products()
        print(result)
        self.assertTrue(len(result)>0)
  

    