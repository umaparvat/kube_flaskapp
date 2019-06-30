from flask_restplus import Api
from movies.apis.movies_api import namespace as movies_namespace, namespace_db as movies_db_namespace


api = Api()
api.add_namespace(movies_namespace, path="/movies")
api.add_namespace(movies_db_namespace, path="/db")
