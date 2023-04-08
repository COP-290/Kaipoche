
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
from flask_paginate import Pagination, get_page_args
import MySQLdb
app=Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()

# def filterbytag(s): # to use in question api
#     # conn=get_db_connection()
#     # cursor.execute('SELECT question FROM Question WHERE tags="%s',s)
#     # post=cursor.fetchall()
#     # cursor.close
#     # if post is None:
#     #     abort(404)
#     ans=[]
#     s="'"+s+"'"
#     for k in tag_list:
#         # print(k[0]==s,k[0])
#         if k==s:
#             ans.append(k)
#     if ans==[]:
#         abort(404)
#     return ans
    

# @app.route('/tag',methods=['GET'])
# def tag_filter():
#     s = request.form['s']
#     a=filterbytag(s)
#     total = len(a)
#     pagination_users=get_tags(offset=0,per_page=len(a)%10)
#     pagination = Pagination(page=1, per_page=total%10, total=total,css_framework='bootstrap4')
#     return render_template('tag.html',tags=a,page=1,per_page=total%10,pagination=pageination)

# @app.route('/score/question',methods=['GET'])
# def showQuestion_byscore():
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     l=cursor.execute('SELECT * FROM Question ORDER BY Score DESC')
#     l=cursor.fetchall()
#     n=len(l)
#     return render_template('question.html',l=l,n=n)

# def get_id_question(tag):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     tags = '"' + tag + '"'
#     l = cursor.execute('SELECT ID FROM Tag where tags= ' + tags)
#     l = cursor.fetchall()
#     ans = []
#     for i in range(len(l)):
#         ans.append(l[i][0])
#     return ans

# def question_from_tag(tag,offset):
#     Ans=[]
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     tags = '"' + tag + '"'
#     a=cursor.execute('select ID from Tag where tags = '+tags+' limit 3 offset '+str(offset))
#     a=cursor.fetchall()
#     for i in range(len(a)):
#         l=cursor.execute('SELECT * FROM Question where id = ' + str(a[i][0]))
#         l=cursor.fetchall()
#         m = cursor.execute('SELECT tags FROM Tag where id = ' + str(a[i][0]))
#         m = cursor.fetchall()
#         M = []
#         for i in range(len(m)):
#             M.append( m[i][0])
#         L = list(l)
#         L.append(M)
#         Ans.append(L)  
#     cursor.close()
#     conn.close()        
#     return Ans

# # print(question_from_tag("c++",0))
# # print()
# # print(question_from_tag('c++',1))

# # conn=requestConnection()
# # cursor=requestCursor(conn)
# # tag='"flex"'
# # a=cursor.execute('select score from Question where ID='+str(80))
# # a=cursor.fetchone()
# # print(a[0],type(a[0]))
# # # b=cursor.execute('select tags from Tag where ID='+str(80))
# # # b=cursor.fetchall()
# # # a=list(a)
# # # a.append(list(b))
# # # print(a[1])
# # a="adsfjas da dskl dfsk ksdkf dfs   fdsjkl"
# # b=a.split()
# # print(b)

# def max_questionid():
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     cursor.execute('SELECT @last_id := MAX(id) FROM Question')
#     Current_questionid=cursor.fetchone()
#     return Current_questionid
# print(max_questionid())

def one_ans(Up,id):
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('select Score from Answer where id='+str(id))
        score=cursor.fetchone()
        cursor.execute('Update Answer set Score= '+str(score[0]+Up)+' where Id='+str(id))
        Ownerid=cursor.execute('select Owner_User_Id,Score from Answer where Id= '+str(id))
        Ownerid=cursor.fetchone()
        ownscore=Ownerid[1]
        Ownerid=Ownerid[0]
        if Up==1:
          cursor.execute('Update User set up_votes='+str(ownscore+Up)+' where id='+str(Ownerid))
        else:
            cursor.execute('Update User set down_votes='+str(ownscore+Up)+' where id='+str(Ownerid))
        conn.commit()
        cursor.close()
        conn.close()
        return score[0]+Up

def editDisplayname(id,name):
    conn = requestConnection()
    cursor = requestCursor(conn)
    p=cursor.execute('Update User set Display_Name='+str(name)+' where Id= '+str('id'))
    conn.commit()
    cursor.close()
    conn.close()
    return "Done"

def editAboutme(id,s):
    conn = requestConnection()
    cursor = requestCursor(conn)
    p=cursor.execute('Update User set About_me='+str(name)+' where Id= '+str('id'))
    conn.commit()
    cursor.close()
    conn.close()
    return "Done"

@app.route('/user/displayname')
def Update_name(name):
    if 'loggedin' in session:
        id=session['id']
        editDisplayname(id,name)
        return "True"
    else:
        return "first logged in"

@app.route('/user/aboutme')
def Update_About(body):
    if 'loggedin' in session:
        id=session['id']
        editAboutme(id,name)
        return "True"
    else:
        return "first logged in"