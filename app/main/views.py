from . import main
from flask import render_template,request,redirect,url_for, abort
from flask_login import login_required, current_user 
from ..models import User,Pitch, Comment
from .. import db,photos
from .forms import UpdateProfile, PitchForm





@main.route('/landingPage')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'PitchCentere Home'
    return render_template('index.html', title = title)

@main.route('/home', methods= ['POST', 'GET'])
@login_required
def home():

    pform = PitchForm()

    if pform.validate_on_submit():
        pitch = Pitch(pitch_title = pform.title.data, category = pform.category.data, pitch_content = pform.pitch.data, user=current_user)


        db.session.add(pitch)
        db.session.commit()

    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    title = 'PitchCentere Home'
    return render_template('home.html', title = title, pform = pform, pitches=pitches)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches = Pitch.query.all()
    return render_template("profile/profile.html", user = user, pitches = pitches)

@main.route('/product')
def product():

    title = 'Pitch-Product'
    return render_template('categories.html', title = title)

@main.route('/interview')
def interview():

    title = 'Pitch-Interview'
    return render_template('categories.html', title = title)


@main.route('/technology')
def technology():

    title = 'Technology-Product'
    return render_template('categories.html', title = title)
    
@main.route('/fashion')
def fashion():

    title = 'Fashion-Product'
    return render_template('categories.html', title = title)
    

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
    

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
    

# @main.route('/home/postpitch/<int:id>',methods= ['POST'])
# @login_required
# def post_pitch():   
#     pform = PitchForm()

#     if pform.validate_on_submit():
#         pitch = Pitch(pitch_content = pform.pitch.data, cat_id = pform.category.data)

#         db.session.add(pitch)
#         db.session.commit()
    
#     return render_template('home.html' ,pform = pform, pid =id)

 
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

