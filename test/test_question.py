import unittest
import csv
import MySQLdb
import datetime

mydb = MySQLdb.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',
    db = 'test'
)

cursor = mydb.cursor()

a1=[[(91, 62, datetime.datetime(2007, 8, 2, 15, 45, 37), 99, 'Python', 'Its body is not about SQL but about python'), ['C++']]]
a2=['Python']
a3=[[(74570, 7709, datetime.datetime(2023, 4, 4, 9, 42, 27), -1, "'CSS : Bad Gray Line to the side of the Navigation Bar on http://perl-begin.org/'", '\'<p>I\'m maintaining <a href="http://perl-begin.org/" rel="nofollow">the Perl Beginners\' Site</a> and used a modified template from Open Source Web Designs. Now, the problem is that I still have an undesired artifact: a gray line on the left side of the main frame, to the left of the navigation menu. Here\'s <a href="http://www.shlomifish.org/Files/files/images/Computer/Screenshots/perl-begin-bad-artif.png" rel="nofollow">an image</a> highlighting the undesired effect.</p>\n\n<p>How can I fix the CSS to remedy this problem?</p>\n\''), []], [(151290, 13930, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'What combination do you use for your polyglot solution?'", "'<p>Those of us who use multiple languages to solve problems can combine them in a lot of ways.  Personally I use PL/SQL, XSLT, JavaScript, and Java plus the pseudo languages HTML, XML, CSS, Ant, and Bash.  What do you use? </p>\n'"), []], [(152670, 10422, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'How to stop the Access 2007 Configuration Progress when switching versions'", '\'<p>Like many developers I need to run more than 1 version of MS Access.  I have just installed Access 2007.  If I open Access 2003 and then open Access 2007 I have to wait 3mins for the \'Configuring Microsoft Office Enterprise 2007..." dialog.  Then if I open Access 2003 again it takes another 30secs or so to configure that.  </p>\n\n<p>PLEASE NOTE: I am using shortcuts to open the files that include the full path to Access.  Eg to open Access 2007:</p>\n\n<pre><code> "C:\\program files\\microsoft office 12\\office12\\msaccess.exe" "C:\\test.accdb"\n</code></pre>\n\n<p>and for 2003:</p>\n\n<pre><code> "C:\\program files\\microsoft office 11\\office11\\msaccess.exe" "C:\\test.mdb"\n</code></pre>\n\n<p>Does anyone have a solution to avoid this?  </p>\n\''), []]]
a4=5
a5=[[(92, 61, datetime.datetime(2007, 4, 1, 9, 45, 37), 79, 'C++', 'Its body is about C++ and C# also'), ['JavaScript']], [(93, 64, datetime.datetime(2009, 8, 1, 14, 46, 37), 87, 'Database in SQL', 'I have to write something about it as'), ['MySQL']], [(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), ['Python']]]
a6=[[(92, 61, datetime.datetime(2007, 4, 1, 9, 45, 37), 79, 'C++', 'Its body is about C++ and C# also'), ['JavaScript']], [(93, 64, datetime.datetime(2009, 8, 1, 14, 46, 37), 87, 'Database in SQL', 'I have to write something about it as'), ['MySQL']], [(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), ['Python']]]
a7=[[(94, 63, datetime.datetime(2010, 8, 1, 15, 45, 37), 123, 'Double is too muvh ', 'Is body necessary for all part is'), ['Java']], [(93, 64, datetime.datetime(2009, 8, 1, 14, 46, 37), 87, 'Database in SQL', 'I have to write something about it as'), ['MySQL']], [(91, 62, datetime.datetime(2007, 8, 2, 15, 45, 37), 99, 'Python', 'Its body is not about SQL but about python'), ['C++']]]
a8=5
a9=[[(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), ['Python']]]
a10=[[(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), ['Python']]]
a11=1
a12=5
a13=[[(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), ['Python']]]

from flask_blog.question import question_from_tag, questionTag_from_id, tag_list_from_listof_id,question_page,question_page2,showQuestion_byscore_help,sort_que_by_time,sort_que_by_time_number,pagefunction,pagefunction2,pagefunction_number,pagefunction_number_all,sort_quesbyTag

class TestQuestion(unittest.TestCase):
    def test_question_from_tag(self):
        x = question_from_tag("c++",0)
        self.assertEqual(a1,x)
    
    def test_questionTag_from_id(self):
        x = questionTag_from_id(90)
        self.assertEqual(a2,x)


    def test_tag_list_from_listof_id(self):
        l = ((74570, 7709, datetime.datetime(2023, 4, 4, 9, 42, 27), -1, "'CSS : Bad Gray Line to the side of the Navigation Bar on http://perl-begin.org/'", '\'<p>I\'m maintaining <a href="http://perl-begin.org/" rel="nofollow">the Perl Beginners\' Site</a> and used a modified template from Open Source Web Designs. Now, the problem is that I still have an undesired artifact: a gray line on the left side of the main frame, to the left of the navigation menu. Here\'s <a href="http://www.shlomifish.org/Files/files/images/Computer/Screenshots/perl-begin-bad-artif.png" rel="nofollow">an image</a> highlighting the undesired effect.</p>\n\n<p>How can I fix the CSS to remedy this problem?</p>\n\''), (151290, 13930, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'What combination do you use for your polyglot solution?'", "'<p>Those of us who use multiple languages to solve problems can combine them in a lot of ways.  Personally I use PL/SQL, XSLT, JavaScript, and Java plus the pseudo languages HTML, XML, CSS, Ant, and Bash.  What do you use? </p>\n'"), (152670, 10422, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'How to stop the Access 2007 Configuration Progress when switching versions'", '\'<p>Like many developers I need to run more than 1 version of MS Access.  I have just installed Access 2007.  If I open Access 2003 and then open Access 2007 I have to wait 3mins for the \'Configuring Microsoft Office Enterprise 2007..." dialog.  Then if I open Access 2003 again it takes another 30secs or so to configure that.  </p>\n\n<p>PLEASE NOTE: I am using shortcuts to open the files that include the full path to Access.  Eg to open Access 2007:</p>\n\n<pre><code> "C:\\program files\\microsoft office 12\\office12\\msaccess.exe" "C:\\test.accdb"\n</code></pre>\n\n<p>and for 2003:</p>\n\n<pre><code> "C:\\program files\\microsoft office 11\\office11\\msaccess.exe" "C:\\test.mdb"\n</code></pre>\n\n<p>Does anyone have a solution to avoid this?  </p>\n\''))
        x = tag_list_from_listof_id(l,3)
        self.assertEqual(a3,x)
    def test_question_page(self):
        x=question_page(0)
        self.assertEqual(a4,x)
    def test_question_page2(self):
        x=question_page2(1,1)
        self.assertEqual(a5,x)
    
    def test_showQuestion_byscore_help(self):
        x=showQuestion_byscore_help(1)
        self.assertEqual(a6,x)
    def test_sort_que_by_time(self):
        x=sort_que_by_time(1)
        self.assertEqual(a7,x)
    def test_sort_que_by_time_number(self):
        x=sort_que_by_time_number()
        self.assertEqual(a8,x)
    def test_pagefunction(self):
        x=pagefunction("Python")
        self.assertEqual(a9,x)
    def test_pagefunction2(self):
        x=pagefunction2(1,"Python")
        self.assertEqual(a10,x)
    def test_pagefunction_number(self):
        x=pagefunction_number("Python")
        self.assertEqual(a11,x)
    def test_pagefunction_number_all(self):
        x=pagefunction_number_all()
        self.assertEqual(a12,x)
    def test_sort_quesbyTag(self):
        x=sort_quesbyTag("Python",1)
        self.assertEqual(a13,x)
