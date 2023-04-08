import unittest
import csv
import MySQLdb
import datetime

# mydb = MySQLdb.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'root',
#     db = 'test'
# )

# cursor = mydb.cursor()
a1=[(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), [('Python',)]]
a2=[(92, 61, datetime.datetime(2008, 8, 1, 14, 45, 37), 90, 13, 'Its Answer is too long therefore i am reducing its size'), (93, 62, datetime.datetime(2008, 8, 1, 15, 45, 37), 90, 14, 'Its Answer is too long therefore i am reducing its size to very small answer')]
a3=98
a4=""
a5=13
from flask_blog.particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time,put_answer

class TestParticular_question(unittest.TestCase):
    def test_particular_que_from_id(self):
        x = particular_que_from_id(90)
        # print(x)
        # print(List)
        self.assertEqual((a1),x)
    
    def test_answer_from_parent_id(self):
        x = answer_from_parent_id(90)
        # print(x)
        # print(List)
        self.assertEqual((a2),x)
    
    def test_score_question(self):
        x = score_question(0,90)
        # print(x)
        # print(List)
        self.assertEqual((a3),x)

    
    def test_sort_ans_by_time(self):
        x = put_answer(90,66,"")
        # print(x)
        # print(List)
        self.assertEqual((a4),x)
    
    def test_put_answer(self):
        x = put_answer(0,95)
        # print(x)
        # print(List)
        self.assertEqual((a5),x)
