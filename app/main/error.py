from flask import render_template
from . import main

@main.app_errorhandler(404)
def error_four(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('error404.html'),404