from flask import Blueprint, request
from sudoku_mailman.models.Subscriber import Subscriber
# from sudoku_mailman.routes import bp
from sudoku_mailman.routes.index import index
from sudoku_mailman.engine import DBSession

unsubscribe_bp = Blueprint('unsubscribe', __name__)
@unsubscribe_bp.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    email = request.form['email']
    with DBSession() as session:
        subscriber = session.query(Subscriber).filter_by(email=email).first()
        # if the subscriber exists, delete it from the database
        if subscriber:
            session.delete(subscriber)
            session.commit()
    return index()