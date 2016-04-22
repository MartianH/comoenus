from comoenus import flask_bcrypt as b, db
from datetime import datetime
from os import urandom


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), unique=False, nullable=False)
    warning_count = db.Column(db.Integer, default=0)
    email = db.Column(db.String(254), unique=True)
    submission = db.relationship('Submission', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    votes = db.relationship('Votes', backref='user', lazy='dynamic')

    def __init__(self, username, password, email):
        self.username = username
        self.password = b.generate_password_hash(password, 9)
        self.email = email

    def __repr__(self):
        return self.username.encode('utf-8')


class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flag_count = db.Column(db.Integer, default=0)
    title = db.Column(db.String(120), unique=False, nullable=False)
    text = db.Column(db.Text, unique=False, nullable=False)
    id_string = db.Column(db.String(12),
                          unique=True,
                          nullable=False,
                          default=urandom(6).encode('hex')
                          )
    date = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('Comment', backref='submission', lazy='dynamic')
    votes = db.relationship('Votes', backref='submission', lazy='dynamic')

    def __init__(self, title, text, user_id, id_string):
        self.title = title
        self.text = text
        self.date = datetime.utcnow()
        self.user_id = user_id
        self.id_string = id_string

    def __repr__(self):
        return "<submission: %r>" % self.title


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thread_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'))
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    votes = db.relationship('Votes', backref='comment', lazy='dynamic')

    def __init__(self, thread_id, user_id, text):
        self.thread_id = thread_id
        self.user_id = user_id
        self.text = text

    def __repr__(self):
        return "<Comment %r>" % self.id


class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comment.id'), nullable=True)
    value = db.Column(db.SmallInteger, nullable=False, default=0)

    def __init__(self, user_id,comment_id, submission_id, value):
        self.user_id = user_id
        self.comment_id = comment_id
        self.submission_id = submission_id
        self.value = value
