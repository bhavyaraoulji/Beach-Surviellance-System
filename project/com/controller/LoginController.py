from project import app
import pymysql
from flask import render_template, request
from project.com.dao.LoginDao import LoginDao


@app.route('/')
def login():
    return render_template('staff/signin.html')


@app.route('/login', methods = ['POST'])
def login2():
    loginUsername = request.args('username')
    loginPassword = request.args('passwrd')

    print loginPassword, loginUsername

    loginDAO = LoginDao()
    obj = loginDAO.LogDAO(loginUsername, loginPassword)
    if len(obj) != 0:
        render_template('/home')
    else:
        render_template('/')
