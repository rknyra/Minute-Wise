from flask import render_template, request, redirect, url_for, abort, session
from . import main
from .forms import SharePitchForm, UpdateProfile, CommentForm
from flask_login import login_required,current_user
from ..models import User, Pitch, Comment
from .. import db, photos


# Views
# Home Page
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its details
    '''
    comment_form = CommentForm()
    
    pitches = Pitch.query.all()
    
    title = 'Minute-Wise'
    return render_template('index.html', title=title, CommentForm=comment_form)

# Share your pitch form
@main.route('/sharePitch', methods=['GET','POST'])
@login_required
def sharePitch():
    '''
    View share_pitch page function that returns the pitch-sharing page and its form
    '''
    posted_pitches = Pitch.query.all()
    form = SharePitchForm()
     
    if form.validate_on_submit():
        pitch = Pitch(pitch = form.pitch.data, category=form.pitch_category.data)
        
        db.session.add(pitch)
        db.session.commit()
        
        return redirect(url_for('main.goToPitches'))
    
    title = 'Minute-Wise: SharePitch'
    return render_template('new_pitch.html', SharePitchForm=form, title=title)

# User profile
@main.route('/user/<usrname>')
def profile(usrname):
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    title = 'Minute-Wise MyProfile'
    return render_template('/profile/profile.html',user=user, title=title)



# Redirect to update profile page
@main.route('/update/<usrname>')
def goToUpdate(usrname):
    
    form = UpdateProfile()
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    title = 'Minute-Wise: MyProfile'
    return render_template('/profile/update.html',user=user,profEditForm = form, title=title)


# Update Profile
@main.route('/update/<usrname>', methods=['GET','POST'])
@login_required
def update_profile(usrname):
    
    form = UpdateProfile()
    user = User.query.filter_by(username = usrname).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile', usrname=user.username))
    
    title = 'Minute-Wise'
    return render_template('/profile/update.html', profEditForm = form, title=title)

# Upload prof pic
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
        
    return redirect(url_for('main.profile',usrname=uname))



# Redirect to pitches page
@main.route('/pitches')
def goToPitches():
    '''
    View pitches page function that returns the pitches page and its details
    '''   
    catOnePitches = Pitch.query.filter_by(category='Hot & Trending').all()
    catTwoPitches = Pitch.query.filter_by(category='Pick-up Lines').all()
    catThreePitches = Pitch.query.filter_by(category='Love & Life').all()
    
    categoryOne = Pitch.query.filter_by(category='Hot & Trending').first()
    catTwo = Pitch.query.filter_by(category='Pick-up Lines').first()
    catThree = Pitch.query.filter_by(category='Love & Life').first()
     
    comment_form = CommentForm()
    # comments = Comment.query.filter(Comment.id > 0).all()
    comments = Comment.query.all()

    title = 'Minute-Wise: Pitches'
    return render_template('/pitches.html', catOnePitches=catOnePitches, catTwoPitches=catTwoPitches, catThreePitches=catThreePitches, categoryOne=categoryOne, catTwo=catTwo, catThree=catThree, comments=comments, CommentForm=comment_form, title=title)


# Comment on other people's pitches
# @main.route('/pitpitchcommentsches', methods=['GET','POST'])
@main.route('/comments', methods=['GET','POST'])

@login_required
def post_comment():
        
    '''
    View post_comment function that facilitates posting of comments
    '''
    # comment_form = CommentForm()
    
    if request.method == 'POST':
    
        print(request.form.get('comment'))
        print('=========================================')   
        print(request.form.get('pitches_id'))
        print('===above me shld be pitches_id a foreign key from pitches table to comments table=====')
        pitches_id = request.form.get('pitches_id')

        comments = Comment.query.filter(Comment.pitches_id > 0).all()
        # pitches_id = Comment.query.filter(comments.pitches_id > 0).all()

        print(comments)
        # print(pitches_id)
        print('===============adfadf================')
        
        comment=Comment(comment=request.form.get('comment'), pitches_id = pitches_id, users_id=current_user.id)
        print(comment)
        print('this is the second =====================')

        db.session.add(comment)
        db.session.commit()
            
        return redirect(url_for('main.goToPitches'))

    title = 'Minute-Wise: Pitches'    
    return render_template('comments.html', CommentForm=comment_form, title=title, pitches_id=pitches_id)

# Redirect to comments
@main.route('/pitchcomments', methods=['GET','POST'])
def goToPitchComments():
    '''
    View pitches page function that returns the pitches page and its details
    '''   
    catOnePitches = Pitch.query.filter_by(category='Hot & Trending').all()
    catTwoPitches = Pitch.query.filter_by(category='Pick-up Lines').all()
    catThreePitches = Pitch.query.filter_by(category='Love & Life').all()
    
    categoryOne = Pitch.query.filter_by(category='Hot & Trending').first()
    catTwo = Pitch.query.filter_by(category='Pick-up Lines').first()
    catThree = Pitch.query.filter_by(category='Love & Life').first()
     
    comment_form = CommentForm()
    # comments = Comment.query.filter(Comment.id > 0).all()
    comments = Comment.query.all()

    title = 'Minute-Wise: Pitches'
    return render_template('/comments.html', catOnePitches=catOnePitches, catTwoPitches=catTwoPitches, catThreePitches=catThreePitches, categoryOne=categoryOne, catTwo=catTwo, catThree=catThree, comments=comments, CommentForm=comment_form, title=title)