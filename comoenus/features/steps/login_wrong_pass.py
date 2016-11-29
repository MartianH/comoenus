from behave import *
import requests


"""
Scenario 2
----------

User gives wrong password
"""

@when(u'user logs with username "dummy" and password "WrongPass"')
def step_impl(context):
    r = requests.post('http://localhost:5000/login', data={
        'username': "dummy",
        'password': "WrongPass"
        })
    context.response = r.text


@then(u'auth message should read "{auth_message}"')
def step_impl(context, auth_message):
    assert context.response == auth_message
