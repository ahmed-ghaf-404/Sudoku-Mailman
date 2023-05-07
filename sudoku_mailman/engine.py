from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

CONNSTR = 'postgresql://sudoku.mailman:bOBUeN7adk1Q@ep-patient-math-334326.us-east-2.aws.neon.tech/users'

Engine = create_engine(CONNSTR , connect_args={'options': '-csearch_path=users'})