from flask import Flask
from sudoku_mailman.base import PORT,HOST


app = Flask(__name__, template_folder='sudoku_mailman/templates', static_folder='sudoku_mailman/static')

from sudoku_mailman.routes.index import index
# from sudoku_mailman.routes.subscribe import subscribe_bp
# from sudoku_mailman.routes.unsubscribe import unsubscribe_bp
# from sudoku_mailman.routes.send_sample import send_sample_bp
# from sudoku_mailman.routes.notify_all_subscribers import notify_all_subscribers_bp 


if __name__ == '__main__':
    app.run(debug=True, port=PORT, host=HOST)


