from flask import Flask, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
import MySQLdb
from flask_blog.tag import get_tags
from question import pagefunction
from question import showQuestion_byscore_help,sort_que_by_time
# from particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time
# from user import check_login
import re
app = Flask(__name__)

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()
app.config['SECRET_KEY'] = 'your secret key'




def dis_user(id):
        conn = requestConnection()
        cursor = requestCursor(conn)
        cursor.execute('SELECT Creation_Date from User where ID = ' + str(id))
        date = cursor.fetchone()
        # cursor.execute('SELECT website_url  from User where ID = ' + str(id))
        # websiteurl = cursor.fetchone()
        # cursor.execute('SELECT profile_image_url  from User where ID = ' + str(id))
        # profile = cursor.fetchone()
        # cursor.execute('SELECT About_me  from User where ID = ' + str(id))
        # about=cursor.fetchone()
        detail=cursor.execute('SELECT * from User where ID = ' + str(id))
        detail=cursor.fetchone()
        date = date[0]
        d = date.day
        mth = date.month
        ye = date.year
        # print(profile[0])
        date = str(d) + "/" + str(mth) + "/"+ str(ye)
        cursor.close()
        conn.close()
        return (date,detail)


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
