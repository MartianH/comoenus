from behave import *
import requests


@when(u'I send a GET request for submission thumbnail for "{username}"')
def step_impl(context, username):
	r = requests.get('http://localhost:5000/api/user_submissions_thumb/'+ username)
	context.response = r.status_code


@then(u'response code should be 200')
def step_impl(context):
	assert  context.response == 200


@when(u'I send a GET request for submission thumbnail for misspelled "{bad_username}"')
def step_impl(context, bad_username):
	r = requests.get('http://localhost:5000/api/user_submissions_thumb/'+ bad_username)
	context.response = r.status_code


@then(u'response code should be 404')
def step_impl(context):
	assert  context.response == 404