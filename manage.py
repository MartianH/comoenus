from comoenus import app, db
from flask.ext.script import Manager
manager = Manager(app)


@manager.command
def create_tables():
    import comoenus.model as model
    import os
    message = ''
    try:
        db_file = os.getcwd()+'/dev.db'
        if not os.path.exists(db_file): 
            open(db_file, 'a').close()
        db.drop_all()
        db.create_all()
        db.session.commit()
        prop_user = model.User('dummy', 'Password2016', 'dummy@example.com')
        db.session.add(prop_user)
        db.session.commit()
        title = 'Lorem Ipsum, more latin.'
        path = os.getcwd() + '/comoenus/static/'
        text = open(path + 'post.txt', 'r').read()
        prop_submission = model.Submission(
            title, text.decode('utf-8'),
            1, os.urandom(6).encode('hex')
            )
        db.session.add(prop_submission)
        db.session.commit()

    except Exception, e:
        message = 'Error: ' + str(e)
    else:
        message = 'tables have been created in database.'

    print message


if __name__ == '__main__':
    manager.run()
