from flask import request,Blueprint
# from sudoku_mailman.routes import bp
from sudoku_mailman.routes.index import index
from sudoku_mailman.util.send_sudoku import send_sudoku


send_sample_bp = Blueprint('send_sample', __name__)

@send_sample_bp.route('/send-sample', methods=['POST'])
def send_sample():
    email = request.form['email']
    send_sudoku(recipient_email=email, puzzle_path='sudoku_mailman/puzzles/puzzle1.pdf')
    return index()