import unittest
import csv
import MySQLdb
import datetime

from flask_blog.user import dis_user

L = ('1/8/2006', (66, 'Satyam', 'Something needs to be written there', datetime.datetime(2006, 8, 1, 15, 45, 37), datetime.datetime(2023, 4, 8, 20, 0, 10), 'India', 378, 893, 98, 'https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg', 'www.gooogle.com', '1234'))
L = ('1/8/2006', (66, 'Satyam', 'Something needs to be written there', datetime.datetime(2006, 8, 1, 15, 45, 37), None, 'India', 378, 893, 98, 'https://static.vecteezy.com/system/resources/previews/005/544/718/original/profile-icon-design-free-vector.jpg', 'www.gooogle.com', '1234'))
 
class Test_User(unittest.TestCase):
        def test_dis_User(self):
                x = dis_user(66)
                self.assertEqual((L),x)
