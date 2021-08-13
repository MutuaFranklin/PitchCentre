from . import main
from flask import render_template,request,redirect,url_for
from flask_login import login_required, current_user 



@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'PitchCentere Home'
    return render_template('index.html', title = title)

# @main.route('/promotion')
# def fun():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     title = 'PC Promotion'
#     return render_template('index.html', title = title)


# @main.route('/interview')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#     title = 'PC Interview'
#     return render_template('index.html', title = title)

