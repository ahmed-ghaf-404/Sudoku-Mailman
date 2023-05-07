from flask import Flask, render_template, request
from sudoku_mailman.engine import Session
from sudoku_mailman.Subscriber import Subscriber
# from flask_mail import Mail, Message
from sudoku_mailman.send_sudoku import send_sudoku
from apscheduler.schedulers.background import BackgroundScheduler
import requests

app = Flask(__name__)
# app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    with Session() as session:
        if session.query(Subscriber).filter_by(email=email).first():
            return render_template('index.html')
        new_subscriber = Subscriber(email=email)
        session.add(new_subscriber)
        session.commit()
    return render_template('index.html')
@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form['email']
    with Session() as session:
        subscriber = session.query(Subscriber).filter_by(email=email).first()
        # if the subscriber exists, delete it from the database
        if subscriber:
            session.delete(subscriber)
            session.commit()
    return render_template('index.html')

@app.route('/send-email', methods=['POST'])
def send_email_to_subscribers():
    with Session() as session:
        subscribers = session.query(Subscriber).all()
        for subscriber in subscribers:
            send_sudoku(recipient_email=subscriber.email)
    return "index.html"

def send_emails_job():
    url = 'http://127.0.0.1:5000/send-email'
    response = requests.post(url)
    print(response.text)
    # send_email_to_subscribers()

scheduler = BackgroundScheduler()
scheduler.add_job(send_emails_job, 'cron', day_of_week='mon-sun', hour=2, minute=51)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=False)