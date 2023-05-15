from flask import render_template, current_app as app
# from app import app

@app.route('/')
def index():
    return render_template('index.html')