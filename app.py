from flask import Flask, render_template, request
from sudoku_mailman.engine import DBSession
from sudoku_mailman.models.Subscriber import Subscriber
from sudoku_mailman.util.send_sudoku import send_sudoku
from sudoku_mailman.base import PORT,HOST



app = Flask(__name__, template_folder='sudoku_mailman/templates', static_folder='sudoku_mailman/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notify_all', methods=['POST'])
def notify_all_subscribers():
    with DBSession() as session:
        subscribers = session.query(Subscriber).all()
        for subscriber in subscribers:
            send_sudoku(recipient_email=subscriber.email, puzzle_path='sudoku_mailman/puzzles/puzzle1.pdf')
    return index()

@app.route('/send-sample', methods=['POST'])
def send_sample():
    email = request.form['email']
    send_sudoku(recipient_email=email, puzzle_path='sudoku_mailman/puzzles/puzzle1.pdf')
    return index()

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    with DBSession() as session:
        if session.query(Subscriber).filter_by(email=email).first():
            return render_template('index.html')
        new_subscriber = Subscriber(email=email)
        session.add(new_subscriber)
        session.commit()
    return index()





@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form['email']
    with DBSession() as session:
        subscriber = session.query(Subscriber).filter_by(email=email).first()
        # if the subscriber exists, delete it from the database
        if subscriber:
            session.delete(subscriber)
            session.commit()
    return index()
# from sudoku_mailman.routes.index import index
# from sudoku_mailman.routes.subscribe import subscribe_bp
# from sudoku_mailman.routes.unsubscribe import unsubscribe_bp
# from sudoku_mailman.routes.send_sample import send_sample_bp
# from sudoku_mailman.routes.notify_all_subscribers import notify_all_subscribers_bp 


if __name__ == '__main__':
    app.run(debug=True, port=PORT, host=HOST)


