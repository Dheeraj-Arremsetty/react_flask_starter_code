import os, sys, flask
base_path = os.path.dirname(__file__)
class_path = os.path.join(base_path, "classes")
config_path = os.path.join(base_path, "config/")
sys.path.insert(0, base_path)
sys.path.insert(1, class_path)

WSGI_PATH_PREFIX = ''
from flask import redirect, url_for
import basicServer_services as services
class Config():
    def __init__(self,app,WSGI_PATH_PREFIX):
        self.app = app
        # register managers and then services
        print'----------------------------------------------------------------------------'
        print '                   WSGIPrefix set to %s'%WSGI_PATH_PREFIX
        self.srvs = services.register_services(app, WSGI_PATH_PREFIX)

# create application
application = flask.Flask(__name__)
application.config['CONFIG_PATH'] = config_path
cfg = None


@application.route(WSGI_PATH_PREFIX + '/basicServer')
def index():
    print 'comming here'
    return "<b>hello</b>"

def set_wsgi_prefix(prefix='/'):
    print 'comming in setWsgi'
    WSGI_PATH_PREFIX = prefix
    cfg = Config(application, WSGI_PATH_PREFIX)

@application.route(WSGI_PATH_PREFIX + '/')
def root():
    print 'comming in root'
    return redirect(url_for('index'))

if __name__ == '__main__':
    WSGI_PATH_PREFIX = '/basicServer'
    cfg = Config(application, WSGI_PATH_PREFIX)
    dport = int(sys.argv[1]) if len(sys.argv) > 1 else 5050
    application.run(host='0.0.0.0',port=dport,debug=True,use_reloader=True,processes=100,static_files={'/':'static'})
else:
    cfg = Config(application, WSGI_PATH_PREFIX)