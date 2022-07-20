import unittest
from project.persistence.users_dao import create_user, get_user, get_users


class userdb(unittest.TestCase):
    
    def test_get_users(self):
        result=get_users()
        print(result)
        self.assertTrue(len(result)>0)
        

    def test_create_user(self):
        previous_date=get_users()
        result=create_user("Rincy","r@r.com", "10July", "India", "trivandrum","Kerala street","password")
        print(result)
        self.assertTrue(result)
        after_date=get_users()
        print(len(after_date))
        print(len(previous_date))
        self.assertTrue(len(after_date)>len(previous_date))




