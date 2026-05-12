from flask import Flask, render_template  , request, redirect, url_for, flash
from flask_mail import Mail, Message    
import os

app = Flask(__name__, template_folder='.')

# Configure Flask-Mail for Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Set in Heroku config
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Set in Heroku config
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')

mail = Mail(app)

# In-memory storage for user data (replace with database in production)
users = {}

@app.route('/')

@app.route('/login.html')
def login():
    return render_template('login.html') 

@app.route('/home.html')
def index():
    return render_template('home.html')

@app.route('/DASHBORD.HTML')
def dashboard():
    return render_template('DASHBORD.HTML')

@app.route('/register page.html')
@app.route('/register%20page.html')
def register():
    return render_template('register page.html')

@app.route('/courses.html')
def courses():
    return render_template('courses.html')

@app.route('/student.html')
def student():
    return render_template('student.html')

@app.route('/learning-platforms.html')
def learning_platforms():
    return render_template('learning-platforms.html')

@app.route('/learning.html')
def learning():
    return render_template('learning.html')

@app.route('/reset password.html')
@app.route('/reset%20password.html')
def reset_password():
    return render_template('reset password.html')

if __name__ == '__main__':
    app.run(debug=True)
