from behave import *
import requests
from flask import app

@given(u'that user is in the database')
def step_impl(context):
    assert True


@when(u'user logs with username "dummy" and password "Password2016"')
def step_impl(context):
    r = requests.post('http://localhost:5000/login', data={
        'username': "dummy",
        'password': "Password2016"
        })
    context.response = r.text


@then(u'auth message should be "{auth_message}"')
def step_impl(context, auth_message):
    assert context.failed is not True
