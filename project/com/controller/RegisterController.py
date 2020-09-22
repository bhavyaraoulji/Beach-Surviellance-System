from project import app
import pymysql
from flask import render_template,request


@app.route('/signin')
def login1():
    return render_template('staff/signin.html')


@app.route('/signup')
def register():
    return render_template('staff/signup.html')

@app.route('/home')
def home():
    return render_template('staff/index.html')


@app.route('/validation')
def validate():
    return render_template('staff/validation.html')


@app.route('/datatable')
def datatab():
    return render_template('staff/data-tables.html')


@app.route('/complain')
def complain():
    return render_template('staff/addComplain.html')


@app.route('/feedback')
def feedback():
    return render_template('staff/addFeedback.html')


if __name__ == '__main__':
    app.run()