from flask import Flask
from sudoku_mailman.routes.index import index_bp
from sudoku_mailman.routes.subscribe import subscribe_bp
from sudoku_mailman.routes.unsubscribe import unsubscribe_bp
from sudoku_mailman.routes.send_sample import send_sample_bp
from sudoku_mailman.routes.notify_all_subscribers import notify_all_subscribers_bp 
from sudoku_mailman.base import PORT,HOST


app = Flask(__name__, template_folder='sudoku_mailman/templates', static_folder='sudoku_mailman/static')
app.register_blueprint(index_bp)
app.register_blueprint(subscribe_bp)
app.register_blueprint(unsubscribe_bp)
app.register_blueprint(send_sample_bp)
app.register_blueprint(notify_all_subscribers_bp)
app.run(debug=True, port=PORT, host=HOST)


