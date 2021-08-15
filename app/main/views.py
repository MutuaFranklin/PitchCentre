from . import main
from flask import render_template,request,redirect,url_for, abort
from flask_login import login_required, current_user 
from ..models import User,Pitch, Comment
from .. import db,photos
from .forms import UpdateProfile, PitchForm, CommentForm





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

        return redirect (url_for ("main.home"))


    '''
    View root page function that returns the index page and its data
    '''
    pitches = Pitch.query.all()
    # random = "Product Pitch"
    # pitches = Pitch.query.filter_by(category =random).all()

    title = 'PitchCentere Home'
    return render_template('home.html', title = title, pform = pform, pitch=pitches)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    pitches = Pitch.query.filter_by(user=current_user)
    return render_template("profile/profile.html", pitches = pitches,user=current_user)

@main.route('/product')
def product():

    title = 'Pitch-Product'
    h4 = 'Interview Pitches'
    random = "Product Pitch"
    pitches = Pitch.query.filter_by(category =random).all()

    return render_template('categories.html', title = title, pitch=pitches, h4=h4)

@main.route('/interview')
def interview():

    title = 'Pitch-Interview'
    h4 = 'Interview Pitches'
    random = "Interview Pitch"
    pitches = Pitch.query.filter_by(category =random).all()
    return render_template('categories.html', title = title, pitch = pitches, h4 =h4)


@main.route('/technology')
def technology():

    title = 'Technology-Pitch'
    h4 = 'Technology Pitches'
    random = "Technology Pitch"
    pitches = Pitch.query.filter_by(category =random).all()
    return render_template('categories.html', title = title, pitch = pitches, h4 =h4)
    
@main.route('/fashion')
def fashion():

    title = 'Fashion-Product'
    h4 = 'Fashion Pitches'
    random = "Fashion Pitch"
    pitches = Pitch.query.filter_by(category =random).all()
    return render_template('categories.html', title = title, pitch = pitches, h4 =h4)
    

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
    

@main.route('/pitch/more<int:id>',methods=['GET','POST'])
@login_required
def more_pitch_details(id):
    single_pitch=Pitch.query.get(id)
    comments= Comment.query.filter_by(pitch_id=id).all()
    commentCount = 'pitch_comment'
    # total_comments = Comment.query.filter_by(commentCount).count()

    cForm=CommentForm()


    if request.args.get("up_vote"):
        single_pitch.up_vote = single_pitch.up_vote+1

        db.session.add(single_pitch)
        db.session.commit()

        # return redirect("/pitch/more/{pitch_id}",pitch_id= single_pitch.pitch_id)

    elif request.args.get("down_vote"):
        single_pitch.down_vote=single_pitch.down_vote+1

        db.session.add(single_pitch)
        db.session.commit()

        # return redirect("/pitch/more/{pitch_id}", pitch_id= single_pitch.pitch_id)
    

    if cForm.validate_on_submit():
        comment = Comment(pitch_comment = cForm.comment.data,pitch_id=single_pitch.pitch_id, user=current_user)


        db.session.add(comment)
        db.session.commit()

        
        return redirect (url_for ("main.more_pitch_details", id= single_pitch.pitch_id))




    
    return render_template('more_pitch_details.html',comments=comments, single_pitch=single_pitch, cForm=cForm)

   