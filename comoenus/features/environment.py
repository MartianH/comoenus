import os, sys, threading
from wsgiref.simple_server import make_server
from comoenus import app


def before_all(context):
    context.server = make_server('', 5000, app)
    context.thread = threading.Thread(target=context.server.serve_forever)
    context.thread.start()



def after_all(context):
    context.server.shutdown()
    context.thread.join()


def before_feature(context, feature):
    app.config.from_object('comoenus.test_config')
    context.client = app.test_client()








def before_feature(context, feature):
    context.client = app.test_client()
