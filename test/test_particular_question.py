import unittest
import csv
import MySQLdb
import datetime
from flask_blog.particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time,put_answer

question_from_tag_answer = [(90, 66, datetime.datetime(2007, 8, 1, 14, 45, 37), 98, 'SQL', 'Its body is about SQL'), [('Python',)]]
answer_list1=([(80, 26, datetime.datetime(2023, 4, 4, 9, 42, 22), 96, "'SQLStatement.execute() - multiple queries in one statement'", '\'<p>I\'ve written a database generation script in <a href="http://en.wikipedia.org/wiki/SQL">SQL</a> and want to execute it in my <a href="http://en.wikipedia.org/wiki/Adobe_Integrated_Runtime">Adobe AIR</a> application:</p>\n\n<pre><code>Create Table tRole (\n      roleID integer Primary Key\n      ,roleName varchar(40)\n);\nCreate Table tFile (\n    fileID integer Primary Key\n    ,fileName varchar(50)\n    ,fileDescription varchar(500)\n    ,thumbnailID integer\n    ,fileFormatID integer\n    ,categoryID integer\n    ,isFavorite boolean\n    ,dateAdded date\n    ,globalAccessCount integer\n    ,lastAccessTime date\n    ,downloadComplete boolean\n    ,isNew boolean\n    ,isSpotlight boolean\n    ,duration varchar(30)\n);\nCreate Table tCategory (\n    categoryID integer Primary Key\n    ,categoryName varchar(50)\n    ,parent_categoryID integer\n);\n...\n</code></pre>\n\n<p>I execute this in Adobe AIR using the following methods:</p>\n\n<pre><code>public static function RunSqlFromFile(fileName:String):void {\n    var file:File = File.applicationDirectory.resolvePath(fileName);\n    var stream:FileStream = new FileStream();\n    stream.open(file, FileMode.READ)\n    var strSql:String = stream.readUTFBytes(stream.bytesAvailable);\n    NonQuery(strSql);\n}\n\npublic static function NonQuery(strSQL:String):void\n{\n    var sqlConnection:SQLConnection = new SQLConnection();\n    sqlConnection.open(File.applicationStorageDirectory.resolvePath(DBPATH);\n    var sqlStatement:SQLStatement = new SQLStatement();\n    sqlStatement.text = strSQL;\n    sqlStatement.sqlConnection = sqlConnection;\n    try\n    {\n        sqlStatement.execute();\n    }\n    catch (error:SQLError)\n    {\n        Alert.show(error.toString());\n    }\n}\n</code></pre>\n\n<p>No errors are generated, however only <code>tRole</code> exists. It seems that it only looks at the first query (up to the semicolon- if I remove it, the query fails). Is there a way to call multiple queries in one statement?</p>\n\''), [('flex',), ('actionscript-3',), ('air',)]], 1, [(124, 26, datetime.datetime(2023, 4, 4, 9, 49, 24), 80, 55, '\'<p>I wound up using this. It is a kind of a hack, but it actually works pretty well. The only thing is you have to be very careful with your semicolons. : D</p>\n\n<pre><code>var strSql:String = stream.readUTFBytes(stream.bytesAvailable);      \nvar i:Number = 0;\nvar strSqlSplit:Array = strSql.split(";");\nfor (i = 0; i &lt; strSqlSplit.length; i++){\n    NonQuery(strSqlSplit[i].toString());\n}\n</code></pre>\n\''), (10008, 1109, datetime.datetime(2023, 4, 4, 9, 49, 24), 80, 19, '\'<p>The <a href="http://en.wikipedia.org/wiki/SQLite" rel="nofollow">SQLite</a> API has a function called something like <code>sqlite_prepare</code> which takes <em>one</em> statement and prepares it for execution, essentially parsing the SQL and storing it in memory. This means that the SQL only has to be sent once to the database engine even though the statement is executed many times.</p>\n\n<p>Anyway, a statement is a single SQL query, that\'s just the rule. The AIR SQL API doesn\'t allow sending raw SQL to SQLite, only single statements, and the reason is, likely, that AIR uses the <code>sqlite_prepare</code> function when it talks to SQLite.</p>\n\''), (193378, None, datetime.datetime(2023, 4, 7, 17, 17, 51), 80, 0, "'gvbyub'"), (193379, None, datetime.datetime(2023, 4, 7, 17, 18, 28), 80, 0, "'gyuguygyu'"), (193380, None, datetime.datetime(2023, 4, 7, 17, 18, 57), 80, 0, "'ggygyugyu'"), (193381, None, datetime.datetime(2023, 4, 7, 17, 20, 47), 80, 0, "'bybvhjy'"), (193382, None, datetime.datetime(2023, 4, 7, 18, 18, 39), 80, 0, "'hi how are you'"), (193383, None, datetime.datetime(2023, 4, 7, 18, 26, 18), 80, 0, "'hi how are you'"), (193384, None, datetime.datetime(2023, 4, 7, 18, 26, 18), 80, 0, "''"), (193385, None, datetime.datetime(2023, 4, 7, 18, 42, 44), 80, 0, "''"), (193386, None, datetime.datetime(2023, 4, 7, 18, 44, 4), 80, 0, "''"), (193387, None, datetime.datetime(2023, 4, 7, 18, 44, 4), 80, 0, "''")], 12)
answer_list=answer_from_parent_id(90)
print(answer_from_parent_id(90))
questionscore=score_question(0,90)
print(questionscore)
answerscore=score_answer(0,92)
print(answerscore)
tag_list_from_listof_id_answer = [[(74570, 7709, datetime.datetime(2023, 4, 4, 9, 42, 27), -1, "'CSS : Bad Gray Line to the side of the Navigation Bar on http://perl-begin.org/'", '\'<p>I\'m maintaining <a href="http://perl-begin.org/" rel="nofollow">the Perl Beginners\' Site</a> and used a modified template from Open Source Web Designs. Now, the problem is that I still have an undesired artifact: a gray line on the left side of the main frame, to the left of the navigation menu. Here\'s <a href="http://www.shlomifish.org/Files/files/images/Computer/Screenshots/perl-begin-bad-artif.png" rel="nofollow">an image</a> highlighting the undesired effect.</p>\n\n<p>How can I fix the CSS to remedy this problem?</p>\n\''), ['html', 'css']], [(151290, 13930, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'What combination do you use for your polyglot solution?'", "'<p>Those of us who use multiple languages to solve problems can combine them in a lot of ways.  Personally I use PL/SQL, XSLT, JavaScript, and Java plus the pseudo languages HTML, XML, CSS, Ant, and Bash.  What do you use? </p>\n'"), ['polyglot']], [(152670, 10422, datetime.datetime(2023, 4, 4, 9, 42, 29), -1, "'How to stop the Access 2007 Configuration Progress when switching versions'", '\'<p>Like many developers I need to run more than 1 version of MS Access.  I have just installed Access 2007.  If I open Access 2003 and then open Access 2007 I have to wait 3mins for the \'Configuring Microsoft Office Enterprise 2007..." dialog.  Then if I open Access 2003 again it takes another 30secs or so to configure that.  </p>\n\n<p>PLEASE NOTE: I am using shortcuts to open the files that include the full path to Access.  Eg to open Access 2007:</p>\n\n<pre><code> "C:\\program files\\microsoft office 12\\office12\\msaccess.exe" "C:\\test.accdb"\n</code></pre>\n\n<p>and for 2003:</p>\n\n<pre><code> "C:\\program files\\microsoft office 11\\office11\\msaccess.exe" "C:\\test.mdb"\n</code></pre>\n\n<p>Does anyone have a solution to avoid this?  </p>\n\''), ['ms-access', 'ms-access-2007']]]
sortans=sort_ans_by_time(90,1)
print(sortans)
putans= put_answer(90,66,"")
print(putans)

class TestParticular_question(unittest.TestCase):
    def test_particular_que_from_id(self):
        x = particular_que_from_id(90)
        self.assertEqual((question_from_tag_answer),x)
    
    def test_answer_from_parent_id(self):
        x = answer_from_parent_id(90)
        self.assertEqual((answer_list),x)
    
    def test_score_question(self):
        x = score_question(0,90)
        self.assertEqual((questionscore),x)

    def test_score_answer(self):
        x = score_answer(0,92)
        self.assertEqual((answerscore),x)
    
    def test_sort_ans_by_time(self):
        x = sort_ans_by_time(90,1)
        self.assertEqual((sortans),x)
    
    def test_put_answer(self):
        x = put_answer(90,66,"")
        self.assertEqual((putans),x)
