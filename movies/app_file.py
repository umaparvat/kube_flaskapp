"""Initialize flask"""
import os
import sys
sys.path.append("/app")
from flask import Flask, jsonify
from flask_migrate import Migrate
from movies.models.db import database
from movies.core.utils import cache
from flask_restplus import Resource
from movies.core.exceptions import MoviesError
from werkzeug.middleware.proxy_fix import ProxyFix
from movies.apis import api



def load_config(app):
    """set the application configuration variable"""
    app.config.from_object('config.app_conf_local')
    # print(app.config)
    if 'CONFFILE_PATH' in os.environ:
        app.config.from_envvar('CONFFILE_PATH')


def database_init(app):
    database.init_app(app)
    Migrate(app, database)


def create_app():
    """To setup the flask app"""
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app)
    load_config(app)
    database_init(app)
    api.init_app(app)
    cache.init_app(app)
    return app


app = create_app()


# @api.route("/hello")
# class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}


#####################################
# Error Handlers
#####################################


@app.errorhandler(Exception)
def all_error_handler(error):
    status_code = 500
    error_dict = {'contact': {'name': 'xxx'},
                  'log_url': "https://yyy.com",
                  "errors": {
                      "message": "The application encountered exception",
                      "error_id": '102',
                      "error_details": str(error)
                  }
                  }
    response = jsonify(error_dict)
    response.status_code = status_code
    return response



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)
