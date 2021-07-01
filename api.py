from flask import Flask
from flask_restful import Resource, Api , request
from time import strftime

import os

import logging
from logging.handlers import RotatingFileHandler
import traceback


os.makedirs('./logs', exist_ok=True)

debug = True

logging.basicConfig(filename='logs/record.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logging.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    return response

@app.errorhandler(Exception)
def exceptions(e):
    tb = traceback.format_exc()
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logging.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, tb)
    return e.status_code

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


class HelloWorld2(Resource):
    def get(self):
        data = None

        len(data)

        app.logger.info('Info level log')
        app.logger.warning('Warning level log')

        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')
api.add_resource(HelloWorld2, '/test')

if __name__ == '__main__':

    app.run(debug=debug)
