from flask import render_template, request, Blueprint
from sudoku_mailman.models.Subscriber import Subscriber
from sudoku_mailman.routes.index import index
from sudoku_mailman.engine import DBSession


subscribe_bp = Blueprint('subscribe', __name__)
@subscribe_bp.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    with DBSession() as session:
        if session.query(Subscriber).filter_by(email=email).first():
            return render_template('index.html')
        new_subscriber = Subscriber(email=email)
        session.add(new_subscriber)
        session.commit()
    return index()