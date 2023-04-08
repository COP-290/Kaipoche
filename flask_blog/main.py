from flask import Flask, jsonify, render_template, request, url_for, flash, redirect, session
from werkzeug.exceptions import abort
import json
from werkzeug.security import generate_password_hash, check_password_hash
from flask_paginate import Pagination, get_page_args
import MySQLdb
from tag import get_tags
from user import dis_user
from question import pagefunction
from question import showQuestion_byscore_help,sort_que_by_time,sort_que_by_time_number
from particular_question import particular_que_from_id,answer_from_parent_id,score_question,score_answer,sort_ans_by_time,put_answer
# from user import check_login
import re
app = Flask(__name__)
Current_questionid=0

def requestConnection():
    mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='root',
    db='test')
    return mydb

def requestCursor(conn):
    return conn.cursor()
app.config['SECRET_KEY'] = 'your secret key'

def max_questionid():
    conn=requestConnection()
    cursor=requestCursor(conn)
    cursor.execute('SELECT @last_id := MAX(id) FROM Question')
    Current_questionid=cursor.fetchone()
    cursor.close()
    conn.close()
    return Current_questionid

Current_questionid=max_questionid()

@app.route('/tag',methods=['GET'])
def tag_page():
    page, per_page, offset = get_page_args(page_parameter='page',per_page_parameter='per_page')
    per_page=6
    offset = (page - 1) *per_page
    pagination_users,total=get_tags(offset=offset,per_page=6)
    pagination = Pagination(page=page, per_page=6, total=total,css_framework='bootstrap5')
    return render_template('tag.html',tags=pagination_users,page=page,per_page=6,pagination=pagination)


@app.route('/<string:tag>/question',methods=['GET'])
def display_question(tag): # took care when question is less than 3
    ans=pagefunction(tag)
    print(ans[0])
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[2],per_page=ans[3],pagination=ans[4])




@app.route('/question')
def zaurez():
    ans=pagefunction("flex")
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[2],per_page=ans[3],pagination=ans[4])

@app.route('/')
def index():
    tag='flex'
    return render_template('index.html',tag=tag)

@app.route('/<int:id>/nw',methods=['GET','POST'])
def after_posting_question(id):
    if 'loggedin' in session:
        # id=session['id']
        l=particular_que_from_id(id)
        print(l)
        print("hi")
        n=1
        # ans_list=answer_from_parent_id(id)
        # m=len(ans_list)
        return render_template('particular_question.html',l=l,n=n,ans_list=[],m=0)
    else:
        redirect(url_for('login'))

@app.route('/score/question',methods=['GET'])
def showQuestion_byscore():
    ans=showQuestion_byscore_help()
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[1],per_page=ans[3],pagination=ans[4])

@app.route('/time/question',methods=['GET'])
def sort_que_by_time_main():
    ans=sort_que_by_time()
    return render_template('question.html',l=ans[0],n=ans[1],page=ans[1],per_page=ans[3],pagination=ans[4])


@app.route('/<int:id>/answer',methods=['GET'])
def particular_question(id):
    l=particular_que_from_id(id)
    n=1
    ans_list=answer_from_parent_id(id)
    m=len(ans_list)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)

@app.route('/ask/question', methods=['GET','POST']) #error in this function as id not generated in good ways
def create():
    if 'loggedin' in session:
        # print(session['id'])
        if request.method == 'POST':
            # if check_login: # how he checked here login by zaurez
            title = request.form['title']
            content = request.form['content']
            tag = request.form['tag'] # take care of how to get particular tag from list of tags
            conn = requestConnection()
            cursor = requestCursor(conn)
            print(title,content,session['id'])
            cursor.execute('INSERT INTO Question (Title, Body,Owner_User_Id,Score) VALUES ("%s","%s", "%s","%s")',(title, content,session['id'],0))
            conn.commit()
            total =max_questionid()[0]
            print(total)
            tag_list=tag.split()
            for k in tag_list:
               cursor.execute('INSERT INTO Tag (ID,tags) VALUES ("%s", "%s")',(total,k))
               conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('after_posting_question',id=total))
    else:
        return redirect(url_for('login'))
    return render_template('new_question.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    msg = ''
    conn = requestConnection()
    cursor = requestCursor(conn)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        # password=check_password_hash(user.password, password) #working but need to increase password size
        # username = '"' + username + '"'
        cursor.execute('SELECT * FROM User WHERE Display_Name = %s AND password = %s', (username, password,))
        account = cursor.fetchall()
        account = list(account)
        # print(account[0])
        if account:
            session['loggedin'] = True
            session['username'] = account[0][1]
            session['id'] = account[0][0]
            return redirect(url_for("show_user"))
        else:
            msg = 'Incorrect username/password!'
        cursor.close()
        conn.close()
    return render_template('login.html', msg=msg)

@app.route('/login/logout')
def logout():
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    conn = requestConnection()
    cursor = requestCursor(conn)
    if request.method=='POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        username1 = '"' + username + '"'
        cursor.execute('SELECT * FROM User WHERE Display_Name = ' +  (username1))
        account = cursor.fetchone()
# Remember to remove duplicacy from account
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        # elif not re.match(r'[A-Za-z0-9]+', username):
        #     msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
        # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO User (Display_Name, password) VALUES (%s, %s)', (username, password))
            conn.commit()
            msg = 'You have successfully registered!'
            return redirect(url_for('show_user'))
    cursor.close()
    conn.close()
    return render_template('signup.html', msg=msg)

@app.route('/user')
def show_user():
    if 'loggedin' in session:
      date,detail=dis_user(session['id'])
      print(detail[9],"hkj")
      return render_template('profile.html',date=date,detail=detail)
    else:
        # print('hi')
        msg = "Please login before"
        return redirect(url_for('login'))

# @app.route('/<int:id>/upscore',methods=['PUT','GET'])
# def up_score(id):
#     if 'loggedin' in session:
#         l,n,ans_list,m=score_question(1,id)
#         return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
#     else:
#         return redirect(url_for('login'))

@app.route('/<int:id>/upscore',methods=['PUT','GET'])
def up_score(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_question(1,id) 
        print(l[0][3])
        return jsonify({'response' : str(l[0][3])})
    else:
        return redirect(url_for('login'))


@app.route('/<int:id>/downscore',methods=['PUT','GET'])
def down_score(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_question(-1,id) 
        return jsonify({'response' : str(l[0][3])})
    else:
        return redirect(url_for('login'))

# def one_ans(1,id):
    
@app.route('/<int:id>/upans',methods=['PUT','GET'])
def up_ans(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_answer(1,id)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        return redirect(url_for('login'))

@app.route('/<int:id>/downans',methods=['PUT','GET'])
def down_ans(id):
    if 'loggedin' in session:
        l,n,ans_list,m=score_answer(-1,id)
        return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)
    else:
        return redirect(url_for('login'))

@app.route('/<int:id>/score/ans',methods=['GET'])
def showAns_byscore(id):
    l,n,ans_list,m=sort_ans_by_time(id,0)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)

@app.route('/<int:id>/time/ans',methods=['GET'])
def sort_ans_by_time_main(id):
    l,n,ans_list,m=sort_ans_by_time(id,1)
    return render_template('particular_question.html',l=l,n=n,ans_list=ans_list,m=m)

@app.route('/<int:id>/new_ans',methods=['POST','GET'])
def newanswer(id):
    if 'loggedin' in session:
        if request.method == 'POST':
            content = request.form['Answer']
            l,n,ans_list,m=put_answer(id,session['id'],content)
            return redirect(url_for('particular_question',id=id))
    else:
        return redirect(url_for('login'))



@app.route('/about')
def about():
    return render_template('About.html')

if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True,port=5010)