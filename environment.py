import os
import sys
import tempfile
import threading
from wsgiref import simple_server
from selenium import webdriver


# Set Path
pwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(pwd)
new_path = pwd.strip(project)
activate_this = os.path.join(new_path, 'comoenus')
sys.path.append(activate_this)


from comoenus import app, request
import comoenus.model


def before_feature(context, feature):
    context.client = app.test_client()
