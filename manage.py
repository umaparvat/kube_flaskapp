import os
from flask_script import Manager
from movies.app_file import app
from flask_migrate import MigrateCommand


manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def routes():
    """Show all routes available"""
    print(app.url_map)


@manager.command
def run():
    """Run app"""
    routes()
    app.run(host='127.0.0.1', port=5000, threaded=True, debug=True)


@manager.command
def rm_pyc():
    """Remove al pyc on bash only"""
    os.system('find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete')


if __name__ == "__main__":
    manager.run()

