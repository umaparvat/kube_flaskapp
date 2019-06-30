import os

DATA_DIR = os.path.abspath(os.path.dirname(__file__) + '\movies\resources')
MOVIES_CSV_PATH = DATA_DIR + '\movies.csv'
MOVIES_DB_PATH = os.path.join(DATA_DIR + "..\..\db\movies.db")