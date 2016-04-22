from flask import request, session, jsonify, abort
from comoenus import app, flask_bcrypt as b, db, rest_api
from comoenus.model import User, Submission, Votes
from slugify import slugify
from tools import time_ago


@rest_api.route('/submissions_thumb')
def api_submissions_thumb():
    submissions = Submission.query.order_by(Submission.date.desc())
    result = []
    for submission in submissions:
        result.append({
            'id': submission.id,
            'title': submission.title,
            'slug': slugify(submission.title),
            'id_string': submission.id_string,
            'user': str(submission.user),
            'timestamp': time_ago(submission.date)
        })

    return jsonify(submissions=result)


@rest_api.route('/user_submissions_thumb/<username>')
def api_user_submissions_thumb(username):
    user = User.query.filter(
        User.username == username
    ).first()
    submissions = Submission.query.filter(
        Submission.user_id == user.id
    ).order_by(Submission.date.desc())
    result = []
    for submission in submissions:
        result.append({
            'id': submission.id,
            'title': submission.title,
            'slug': slugify(submission.title),
            'id_string': submission.id_string,
            'user': str(submission.user),
            'timestamp': time_ago(submission.date)
        })

    return jsonify(submissions=result)


@rest_api.route('/sub_vote:<plus_minus>/<sub_id_string>:<username>', methods=['POST'])
def submission_vote(plus_minus, sub_id_string, username):
    user = User.query.filter_by(username=username).first()
    status = None
    try:
        sub = Submission.query.filter_by(id_string=sub_id_string).first()
        vote = Votes.query.filter_by(
            submission_id=sub.id,
            comment_id=None,
            user_id=user.id 
            ).first()
        if plus_minus == 'plus':
            if vote is None:
                new_vote = Votes(user.id, None,sub.id, 1)
                db.session.add(new_vote)
                db.session.commit()
            else:
                if vote.value == 0 or vote.value == -1:
                    vote.value = 1
                    db.session.commit()
                elif vote.value == 1:
                    vote.value = 0
                    db.session.commit()
        elif plus_minus == 'minus':
            if vote is None:
                new_vote = Votes(user.id, None,sub.id, -1)
                db.session.add(new_vote)
                db.session.commit()
            else:
                if vote.value == 0 or vote.value == 1:
                    vote.value = -1
                    db.session.commit()
                elif vote.value == -1:
                    vote.value = 0
                    db.session.commit()
    except Exception, e:
        status = [False, str(e)]
    else:
        status = [True, vote.value]
    
    return jsonify(status=status)


@rest_api.route('/comm_vote:<lus_minus>/<sub_id>:<user_id>')
def comment_vote(plus_minus, comment_id, user_id):
    status = None
    try:
        vote = Votes.query.filter_by(
            submission_id=None,
            comment_id=comment_id,
            user_id=user_id 
            ).first()
        if plus_minus == 'plus':
            if vote is None:
                new_vote = Votes(user_id, comment_id,None, 1)
                db.session.add(new_vote)
                db.session.commit()
            else:
                if vote.value == 0 or vote.value == -1:
                    vote.value = 1
                    db.session.commit()
                elif vote.value == 1:
                    vote.value = 0
                    db.session.commit()
        elif plus_minus == 'minus':
            if vote is None:
                new_vote = Votes(user_id, comment_id, None, -1)
                db.session.add(new_vote)
                db.session.commit()
            else:
                if vote.value == 0 or vote.value == 1:
                    vote.value = -1
                    db.session.commit()
                elif vote.value == -1:
                    vote.value = 0
                    db.session.commit()
    except Exception, e:
        status = [False, str(e)]
    else:
        status = [True, None]
    
    return jsonify(status=status)
