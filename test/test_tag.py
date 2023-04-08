import unittest
import csv
import MySQLdb

mydb = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='root',
    db='testing')

cursor = mydb.cursor()
# List = []
# with open("tag.csv", 'r') as file:
#   csvreader = list(csv.reader(file))
#   for row in csvreader[1:11]:
#     r = list(row)
#     cursor.execute('INSERT INTO TAG (tag,ID) VALUES("%s", "%s")',((r[1]),int(r[0],)))
#     List.append((int(r[0],r[1])))
# # sql1 =  DROP TABLE IF EXISTS Tag; 
# # sql2 = CREATE TABLE TAG (ID int,tag varchar(80));

# mydb.commit()
# cursor.close()
# print ("Done")


from flask_blog.main_ import tag_page, tag_page_number,tag_list

class TestTags(unittest.TestCase):
    def test_tags(self):
        x = tag_page(6,1)
        l=[]
        self.assertEqual((l, 6),x)


