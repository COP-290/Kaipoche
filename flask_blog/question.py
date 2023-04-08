# from flask import Flask, render_template, request, url_for, flash, redirect
# from werkzeug.exceptions import abort
# from flask_paginate import Pagination, get_page_args
# import MySQLdb
# app=Flask(__name__)

# def requestConnection():
#     mydb = MySQLdb.connect(host='localhost',
#     user='root',
#     passwd='root',
#     db='test')
#     return mydb

# def requestCursor(conn):
#     return conn.cursor()

# # def get_id_question(tag):
# #     conn = requestConnection()
# #     cursor = requestCursor(conn)
# #     tags = '"' + tag + '"'
# #     l = cursor.execute('SELECT ID FROM Tag where tags= ' + tags)
# #     l = cursor.fetchall()
# #     ans = []
# #     for i in range(len(l)):
# #         ans.append(l[i][0])
# #     return ans


# def questionTag_from_id(id): # list of tag from question id
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
#     l=cursor.fetchall()
#     tag_list=[]
#     for k in range(0,len(l)):
#         tag_list.append(l[k][0])
#     cursor.close()
#     conn.close()
#     return tag_list



# def question_from_tag(tag,offset):
#     Ans=[]
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     tags = '"' + tag + '"'
#     f = str(offset)
#     a=cursor.execute('select ID from Tag where tags = '+ tags +' limit 3 offset '+ f  )
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

# # print(len(question_from_tag("flex",0)))

# def tag_list_from_listof_id(l,n):
#     ans=[]
#     for i in range(0,n):
#         a=l[i][0]
#         b=questionTag_from_id(a)
#         c=[]
#         c.append(l[i])
#         c.append(b)
#         ans.append(c)
#     return ans

# # Not able to do unit test for this
# def question_page(val): # took care when question is less than 3 
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
#     per_page=3
#     offset=(page-1)*per_page
#     if val==0:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date DESC limit 3 offset '+str(offset))
#     elif val==1:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     n=len(l)
#     ans=tag_list_from_listof_id(l,n)
#     p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
#     p=cursor.fetchall()
#     total = (p[0][0])
#     pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return (ans,n,page,3,pagination,total)

# def question_page_new(val,page): # took care when question is less than 3 
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     # page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
#     per_page=3
#     offset=(page-1)*per_page
#     if val==0:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
#     elif val==1:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     n=len(l)
#     ans=tag_list_from_listof_id(l,n)
#     p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
#     p=cursor.fetchall()
#     total = (p[0][0])
#     # pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return ans

# def question_page2(val,page): # took care when question is less than 3 
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     per_page=3
#     offset=(page-1)*per_page
#     if val==0:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
#     elif val==1:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     n=len(l)
#     ans=tag_list_from_listof_id(l,n)
#     p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
#     p=cursor.fetchall()
#     total = (p[0][0])
#     # pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     # n=0
#     # if (total)<3*(page):
#     #     n=total % 3
#     # else:
#     #     n=3
#     cursor.close()
#     conn.close()
#     return ans

# def question_page2(val,page): # took care when question is less than 3 
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     per_page=3
#     offset=(page-1)*per_page
#     if val==0:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
#     elif val==1:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     n=len(l)
#     ans=tag_list_from_listof_id(l,n)
#     p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
#     p=cursor.fetchall()
#     total = (p[0][0])
#     # pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     # return (ans,n,page,3,pagination)
#     return ans

# # print(question_page(1))

# def showQuestion_byscore_help(page):
#     a=question_page2(1,page)
#     return a

# def sort_que_by_time(page):
#     # b=question_page(0)
#     b=question_page_new(0,page)
#     return b

# def sort_que_by_time_number():
#     # b=question_page(0)
#     b=question_page(0)[5]
#     return b    
# # print(question_page(1))
# # # print(sort_que_by_time())
# # if __name__=="__main__":
# #     app.run(host='0.0.0.0',debug=True,port=7000)

# def pagefunction(tag='flex'):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
#     per_page=3
#     offset=(page-1)*per_page
#     l=question_from_tag(tag,offset)
#     tags='"'+tag+'"'
#     p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
#     p=cursor.fetchall()
#     total = (p[0][0])
#     pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return (l,n,page,3,pagination)

# def pagefunction2(page,tag='flex'):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     per_page=3
#     offset=(page-1)*per_page
#     l=question_from_tag(tag,offset)
#     print("jnjnjnjn",l)
#     tags='"'+tag+'"'
#     p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
#     p=cursor.fetchall()
#     total = (p[0][0])
#     pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return l

# def pagefunction_number(tag='flex'):
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     per_page=3
#     page = 1
#     offset=(page-1)*per_page
#     l=question_from_tag(tag,offset)
#     tags='"'+tag+'"'
#     p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
#     p=cursor.fetchall()
#     total = (p[0][0])
#     pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return total

# def pagefunction_number_all():
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     per_page=3
#     page = 1
#     offset=(page-1)*per_page
#     l=question_from_tag(tag,offset)
#     tags='"'+tag+'"'
#     p=cursor.execute('SELECT count(id) FROM Tag')
#     p=cursor.fetchall()
#     total = (p[0][0])
#     # pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return total

# # print(pagefunction('flex'))


# # def search_question(search):
# #     conn = requestConnection()
# #     cursor = requestCursor(conn)
# #     # search = request.form['search']
# #     search  = '"' + search + '"'
# #     cursor.execute("SELECT * from Question WHERE Body LIKE " + (search))
# #     M = cursor.fetchall()
# #     print(M)

# # print(search_question("SQL"))
# def sort_quesbyTag(tag,page): # remember to add Tag list in the question
#     conn = requestConnection()
#     cursor = requestCursor(conn)
#     per_page=3
#     offset=(page-1)*per_page
#     tag='"'+tag+'"'
#     l=cursor.execute('SELECT Question.Id,Question.Owner_User_Id,Question.Creation_Date,Question.Score,Question.Title,Question.Body from Question inner join Tag where Tag.tags='+str(tag)+' and Question.Id=Tag.Id order by Score Desc limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     cursor.close()
#     conn.close()
#     ans=tag_list_from_listof_id(l,len(l))
#     return ans

# # print(sort_quesbyTag('flex',1))
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


def questionTag_from_id(id): # list of tag from question id
    conn=requestConnection()
    cursor=requestCursor(conn)
    l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
    l=cursor.fetchall()
    tag_list=[]
    for k in range(0,len(l)):
        tag_list.append(l[k][0])
    cursor.close()
    conn.close()
    return tag_list



def question_from_tag(tag,offset):
    Ans=[]
    conn=requestConnection()
    cursor=requestCursor(conn)
    tags = '"' + tag + '"'
    f = str(offset)
    a=cursor.execute('select ID from Tag where tags = '+ tags +' limit 3 offset '+ f  )
    a=cursor.fetchall()
    for i in range(len(a)):
        l=cursor.execute('SELECT * FROM Question where id = ' + str(a[i][0]))
        l=cursor.fetchall()
        m = cursor.execute('SELECT tags FROM Tag where id = ' + str(a[i][0]))
        m = cursor.fetchall()
        M = []
        for i in range(len(m)):
            M.append( m[i][0])
        L = list(l)
        L.append(M)
        Ans.append(L)  
    cursor.close()
    conn.close()        
    return Ans

# a=((question_from_tag("mysql",0)))
# print(len(a))


def tag_list_from_listof_id(l,n):
    ans=[]
    for i in range(0,n):
        a=l[i][0]
        b=questionTag_from_id(a)
        c=[]
        c.append(l[i])
        c.append(b)
        ans.append(c)
    return ans
# print(tag_list_from_listof_id(a,3))

# Not able to do unit test for this
def question_page(val): # took care when question is less than 3 
    conn=requestConnection()
    cursor=requestCursor(conn)
    p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
    p=cursor.fetchall()
    total = (p[0][0])
    cursor.close()
    conn.close()
    return total

# def question_page_new(val,page): # took care when question is less than 3 
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     # page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
#     per_page=3
#     offset=(page-1)*per_page
#     if val==0:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
#     elif val==1:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     n=len(l)
#     ans=tag_list_from_listof_id(l,n)
#     p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
#     p=cursor.fetchall()
#     total = (p[0][0])
#     # pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     n=0
#     if (total)<3*(page):
#         n=total % 3
#     else:
#         n=3
#     cursor.close()
#     conn.close()
#     return ans

# def question_page2(val,page): # took care when question is less than 3 
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     per_page=3
#     offset=(page-1)*per_page
#     if val==0:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date ASC limit 3 offset '+str(offset))
#     elif val==1:
#         l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
#     l=cursor.fetchall()
#     n=len(l)
#     ans=tag_list_from_listof_id(l,n)
#     p=cursor.execute('SELECT count(ID) FROM Question') # This is not giving correct answer why?
#     p=cursor.fetchall()
#     total = (p[0][0])
#     # pagination = Pagination(page=page, per_page=per_page, total=total,css_framework='bootstrap5')
#     # n=0
#     # if (total)<3*(page):
#     #     n=total % 3
#     # else:
#     #     n=3
#     cursor.close()
#     conn.close()
#     return ans

def question_page2(val,page): # took care when question is less than 3 
    conn=requestConnection()
    cursor=requestCursor(conn)
    per_page=3
    offset=(page-1)*per_page
    if val==0:
        l=cursor.execute('SELECT * FROM Question ORDER BY Creation_Date DESC limit 3 offset '+str(offset))
    elif val==1:
        l=cursor.execute('SELECT * FROM Question ORDER BY Score limit 3 offset '+str(offset))
    l=cursor.fetchall()
    n=len(l)
    ans=tag_list_from_listof_id(l,n)
    cursor.close()
    conn.close()
    # return (ans,n,page,3,pagination)
    return ans

# print(question_page(1))

def showQuestion_byscore_help(page):
    a=question_page2(1,page)
    return a

def sort_que_by_time(page):
    # b=question_page(0)
    b=question_page2(0,page)
    return b

def sort_que_by_time_number():
    # b=question_page(0)
    b=question_page(0)
    return b    
# print(question_page(1))
# # print(sort_que_by_time())
# if __name__=="__main__":
#     app.run(host='0.0.0.0',debug=True,port=7000)

def pagefunction(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    cursor.close()
    conn.close()
    return (l)

def pagefunction2(page,tag='flex'):
    per_page=3
    offset=(page-1)*per_page
    l=question_from_tag(tag,offset)
    return l

def pagefunction_number(tag='flex'):
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    page = 1
    offset=(page-1)*per_page
    tags='"'+tag+'"'
    p=cursor.execute('SELECT count(id) FROM Tag where tags='+str(tags))
    p=cursor.fetchall()
    total = (p[0][0])
    cursor.close()
    conn.close()
    return total

def pagefunction_number_all():
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    page = 1
    offset=(page-1)*per_page
    p=cursor.execute('SELECT count(id) FROM Tag')
    p=cursor.fetchall()
    total = (p[0][0])
    cursor.close()
    conn.close()
    return total

def sort_quesbyTag(tag,page): # remember to add Tag list in the question
    conn = requestConnection()
    cursor = requestCursor(conn)
    per_page=3
    offset=(page-1)*per_page
    tag='"'+tag+'"'
    l=cursor.execute('SELECT Question.Id,Question.Owner_User_Id,Question.Creation_Date,Question.Score,Question.Title,Question.Body from Question inner join Tag where Tag.tags='+str(tag)+' and Question.Id=Tag.Id order by Score Desc limit 3 offset '+str(offset))
    l=cursor.fetchall()
    cursor.close()
    conn.close()
    ans=tag_list_from_listof_id(l,len(l))
    return ans

# print(sort_quesbyTag('mysql',1))

