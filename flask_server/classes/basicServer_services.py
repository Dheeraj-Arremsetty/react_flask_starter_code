import os, json
from flask import jsonify, request, Response, redirect
BASE_PATH = str(os.path.realpath(__file__))
BASE_PATH = BASE_PATH.replace('basicServer_services.pyc', '')
BASE_PATH = BASE_PATH.replace('basicServer_services.pyo', '')
BASE_PATH = BASE_PATH.replace('basicServer_services.py', '')

CLASS_PATH = BASE_PATH.replace('classes', '')

def register_services(app, WSGI_PATH_PREFIX):
    BaseServices(app, WSGI_PATH_PREFIX)


class BaseServices:
    def __init__(self, app, WSGI_PATH_PREFIX):
        self.session_users = {}
        self.app = app

        print'----------------------------------------------------------------------------'
        print '                        Elastic is Stretching'
        print'----------------------------------------------------------------------------'
        print '                        Register MDMDQ API'
        print'----------------------------------------------------------------------------'
        #       ----------------------------------------------------------------------------
        #                                 MDMDQ Services
        #       ----------------------------------------------------------------------------
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/demo', 'demo', self.demo, methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/giveJson', 'giveJson', self.giveJson, methods=['POST', 'GET'])
        self.app.add_url_rule(WSGI_PATH_PREFIX + '/services/add', 'add', self.add, methods=['POST', 'GET'])

    def demo(self):
        return  'In DEMO method'

    def giveJson(self):
        _d = {i:i*'*' for i in xrange(55)}
        print _d
        return jsonify({"data":_d})

    def getparams(self, request):
        return request.form if (request.method == 'POST') else request.args

    def add(self):
        #http://0.0.0.0:5050/basicServer/services/add?a=100&b=200
        params = self.getparams(request)
        a =params.get('a',5)
        b =params.get('b',10)
        c = int(a)+int(b)
        return str(c)
