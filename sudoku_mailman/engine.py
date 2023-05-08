from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

CONNSTR = 'postgresql://sudoku.mailman:bOBUeN7adk1Q@ep-patient-math-334326.us-east-2.aws.neon.tech/users?sslmode=require'

Engine = create_engine(CONNSTR , connect_args={'options': '-csearch_path=users'})
Session = scoped_session(sessionmaker(bind=Engine))

class DBSession:
    def __enter__(self):
        self.session = Session()
        return self.session

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.session.rollback()
        self.session.close()