
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

# def question_from_id(id): # output list of all questions from a given id
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     l=cursor.execute('SELECT * FROM Question where id = ' + str(id))
#     l=cursor.fetchall()
#     M = []
#     for i in l:
#         M.append(i)
#     cursor.close()
#     conn.close()
#     return list(M)
# def questionTag_from_id(id): # list of tag from question id
#     conn=requestConnection()
#     cursor=requestCursor(conn)
#     l=cursor.execute('SELECT tags FROM Tag where id = ' + str(id))
#     l=cursor.fetchall()
#     tag_list=[]
#     # print(l)
#     for k in range(0,len(l)):
#         tag_list.append(l[k][0])
#     cursor.close()
#     conn.close()
#     return tag_list

def particular_que_from_id(id):
    conn=requestConnection()
    cursor=requestCursor(conn)
    a=cursor.execute('select * from Question where ID='+str(id))
    a=cursor.fetchall()
    b=cursor.execute('select tags from Tag where ID='+str(id))
    b=cursor.fetchall()
    a=list(a)
    a.append(list(b))
    cursor.close()
    conn.close()
    return a
# print(answer_from_id())
# print(particular_que_from_id(80))

def answer_from_parent_id(id):
    conn = requestConnection()
    cursor = requestCursor(conn)
    l = cursor.execute('SELECT * FROM Answer where Parent_ID = ' + str(id))
    l = cursor.fetchall()
    Answer_list = []
    for k in range(len(l)):
        Answer_list.append(l[k])
    return Answer_list

def score_question(Up,id):
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('select Score from Question where id='+str(id))
        score=cursor.fetchone()
        cursor.execute('Update Question set Score= '+str(score[0]+Up)+' where Id='+str(id))
        Ownerid=cursor.execute('select Owner_User_Id,Score from Question where Id= '+str(id))
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
        l=particular_que_from_id(id)
        # n=1
        # ans_list=answer_from_parent_id(id)
        # m=len(ans_list)
        # return l,n,ans_list,m 
        return l[0][3]

def score_answer(Up,id):
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
        cursor.execute('select Parent_Id from Answer where id='+str(id))
        Pid=cursor.fetchone()
        l=particular_que_from_id(Pid[0])
        n=1
        ans_list=answer_from_parent_id(Pid[0])
        m=len(ans_list)
        cursor.close()
        conn.close()
        return l,n,ans_list,m 

def sort_ans_by_time(id,time):
    conn = requestConnection()
    cursor = requestCursor(conn)
    l=particular_que_from_id(id)
    n=1
    if time:
      ans_list= cursor.execute('SELECT * FROM Answer  where Parent_ID = ' + str(id)+' Order by Creation_Date')
    else:
        ans_list= cursor.execute('SELECT * FROM Answer  where Parent_ID = ' + str(id)+' Order by Score')
    ans_list = cursor.fetchall()
    Answer_list = []
    m=len(ans_list)
    for k in range(m):
        Answer_list.append(ans_list[k])
    cursor.close()
    conn.close()
    return l,n,Answer_list,m 

# def put_answer(id,body): #has to correct this function
def put_answer(id,ownerid,body):
    conn = requestConnection()
    cursor = requestCursor(conn)
    # l=particular_que_from_id(id)
    # n=1 
    cursor.execute('insert into Answer (Owner_User_Id,Parent_ID,Score,Body) Values ("%s","%s","%s","%s")',(ownerid,id,0,body))
    # cursor.execute('insert into Answer (Parent_ID,Score,Body) Values ("%s","%s","%s")',(id,0,body))
    conn.commit()
    cursor.close()
    conn.close()
    # ans_list=answer_from_parent_id(id)
    # m=len(ans_list)
    # return l,n,ans_list,m 
    return ""




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
