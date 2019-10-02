import os
from ast import literal_eval

_basedir = os.path.join(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLDATABASE_URI")
# SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
TRAP_HTTP_EXCEPTIONS = True
ERROR_404_HELP = True
BUNDLE_ERRORS = True
CACHE_TYPE = 'simple'
