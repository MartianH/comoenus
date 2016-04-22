from flask import render_template, request, session, jsonify, abort, make_response, redirect, url_for
from comoenus import app, flask_bcrypt as b, db
from comoenus.model import User, Submission
from slugify import slugify
from tools import time_ago
from os import urandom


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.jade')


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        plain_pass = request.form['password']
        candidate = User.query.filter(
            User.username == username
        ).first()

        if candidate is not None:
            password_is_valid = b.check_password_hash(
                candidate.password,
                plain_pass.encode('utf-8')
            )
            if password_is_valid:
                message = "Success"
                session['uid'] = candidate.id
                session['username'] = candidate.username
            else:
                message = abort(make_response("Wrong password...", 403))
        else:
            message = abort(make_response("User does not exist", 403))

    return jsonify(message=message)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = None
    if request.method == 'POST':
        data = request.get_json(force=False, silent=False, cache=True)
        username = data['uname']
        email = data['email']
        password = data['pswd']
        prop_user = User(username, password, email)
        db.session.add(prop_user)
        db.session.commit()
        message = "Success"
    return jsonify(message=message)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


@app.route('/post/<title>_<id_string>')
def submission(title, id_string):
    # path = os.getcwd() + '/comoenus/static/'
    # text = open(path + 'post.txt', 'r').read()
    meta = None
    sub = Submission.query.filter(
            Submission.id_string == id_string,
        ).first()
    if sub is not None:
        user = User.query.filter(
                User.id == Submission.user_id
            ).first()
        meta = {
            'title': sub.title,
            'user': user.username,
            'timestamp': time_ago(sub.date),
            'text': sub.text
        }
    else:
        abort(404)

    return render_template('submission.jade',
                           meta=meta)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    return_variable = render_template('submit.jade')
    if 'username' in session:
        title = None
        text = None
        if request.method == 'POST':
            title = request.form['title']
            text = request.form['text']
            if title is not None and text is not None:
                user = User.query.filter(
                    User.username == session['username']
                ).first()
            sub = Submission(title, text, user.id, urandom(6).encode('hex'))
            db.session.add(sub)
            db.session.commit()
            return_variable = redirect(url_for('submission',
                                       title=slugify(sub.title),
                                       id_string=sub.id_string))
    else:
        return_variable = redirect(url_for('index'))
    return return_variable


@app.route('/user/<username>')
def user_page(username):
    return render_template('userpage.jade', username=username)
