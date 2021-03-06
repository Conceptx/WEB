from flask import Flask, render_template, url_for
import gunicorn


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    