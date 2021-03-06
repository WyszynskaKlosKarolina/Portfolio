from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<page_name>')
def upload_page(page_name=None):
    return render_template(page_name)
