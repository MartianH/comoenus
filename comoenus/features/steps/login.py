from behave import *
from comoenus.model import User
import requests, json

@given(u'That app is running')
def comoenus_is_running(context):
    assert context.client

@given(u'that user is in the database')
def step_impl(context):
	username = 'dummy'
	candidate = User.query.filter(
    	User.username == username
    ).first()

	assert candidate is not None


@when(u'user logs with username "dummy" and password "Password2016"')
def step_impl(context):
    r = requests.post('http://localhost:5000/login', data={
        'username': "dummy",
        'password': "Password2016"
        })
    context.response = r.json()['message']


@then(u'auth message should be "{auth_message}"')
def step_impl(context, auth_message):
    assert context.response == auth_message