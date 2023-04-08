import unittest
import csv
import MySQLdb
mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='test')
cursor = mydb.cursor()
List = ([(1, 'Python'), (1, 'C++'), (1, 'JavaScript'), (1, 'MySQL'), (1, 'Java')], 5)

get_tags_list_answer = [('Python',), ('C++',), ('JavaScript',), ('MySQL',), ('Java',)]
# print ("Done")

from flask_blog.tag import get_tags, get_tags_list
# print(get_tags())

class TestTags(unittest.TestCase):
    def test_tags(self):
        x = get_tags()
        self.assertEqual((List),x)
    def test_get_tags_list(self):
        x = get_tags_list()
        self.assertEqual((get_tags_list_answer),x)
