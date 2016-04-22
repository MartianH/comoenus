from comoenus import app
from flask import render_template


@app.errorhandler(404)
def not_found(error):
    title = 'Nothing...(404)'
    description = 'The page you are looking for does not exist or is gone.'

    return render_template('error_page.jade',
                           title=title,
                           description=description,
                           image=False), 404


@app.errorhandler(403)
def forbidden(error):
    title = 'NO ACCESS (403)'
    description = 'You do not have access to this page. Move along, please.'

    return render_template('error_page.jade',
                           title=title,
                           description=description,
                           image=False), 403


@app.errorhandler(500)
def internal_server_error(error):
    title = 'Internal Error...(505)'
    description = 'Well, this is awkward... try reloading the page!'

    return render_template('error_page.jade',
                           title=title,
                           description=description,
                           image=True), 500
