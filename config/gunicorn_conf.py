import multiprocessing
import getpass

base_dir = f"/app"
gunicorn_dir = base_dir + 'gunicorn/'
# secrets_dir = base_dir + 'secrets/'
# server
bind = '0.0.0.0:8443'
workers = multiprocessing.cpu_count() * 2 + 1
timeout = 2000
daemon = True
# certfile = base_dir + "ssl_keys/srv.pem"
# keyfile = base_dir + "ssl_keys/srv.key"


# files
errorlog = gunicorn_dir + '/var/log/error.log'
accesslog = gunicorn_dir + '/var/log/access.log'


