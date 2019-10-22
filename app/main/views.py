from flask import render_template, request, redirect, url_for, abort
from . import main
from .forms import SharePitchForm, UpdateProfile
from flask_login import login_required
from ..models import User
from .. import db


# Views
# Home Page
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its details
    '''
    
    title = 'Minute-Wise'
    return render_template('index.html', title=title)

# Share your pitch form
@main.route('/sharePitch', methods=['GET','POST'])
@login_required
def sharePitch():
    form = SharePitchForm()
    '''
    View share_pitch page function that returns the pitch-sharing page and its form
    '''
    return render_template('/new_pitch.html', SharePitchForm=form)

# User profile
@main.route('/user/<usrname>')
def profile(usrname):
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    return render_template('/profile/profile.html',user=user)



# Redirect to update profile page
@main.route('/update/<usrname>')
def goToUpdate(usrname):
    
    form = UpdateProfile()
    user = User.query.filter_by(username = usrname).first()
    
    if user is None:
        abort(404)
    
    return render_template('/profile/update.html',user=user,profEditForm = form)


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
    return render_template('/profile/update.html', profEditForm = form)