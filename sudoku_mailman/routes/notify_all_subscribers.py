
from sudoku_mailman.engine import DBSession
from sudoku_mailman.models.Subscriber import Subscriber
from sudoku_mailman.util.send_sudoku import send_sudoku
from sudoku_mailman.routes.index import index
from flask import Blueprint


notify_all_subscribers_bp = Blueprint('notify_all_subscribers', __name__)
@notify_all_subscribers_bp.route('/notify_all', methods=['POST'])
def notify_all_subscribers():
    with DBSession() as session:
        subscribers = session.query(Subscriber).all()
        for subscriber in subscribers:
            send_sudoku(recipient_email=subscriber.email, puzzle_path='sudoku_mailman/puzzles/puzzle1.pdf')
    return index()