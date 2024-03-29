from flask_wtf import FlaskForm
from wtforms import SelectField,StringField,TextAreaField,SubmitField
from wtforms.validators import Required
from wtforms import ValidationError

class SharePitchForm(FlaskForm):
    pitch_category = SelectField('Pitch here!', choices=[('Hot & Trending', 'Hot & Trending'), ('Pick-up Lines','Pick-up Lines'), ('Love & Life', 'Love & Life')], validators=[Required()])
    pitch = TextAreaField('', validators=[Required()], render_kw={"placeholder": "Write your pitch here :)"})
    # contributor_name = StringField('', validators=[Required()], render_kw={"placeholder":"Write your username"})
    # username should pick from current user's username
    submit = SubmitField('Share')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you',validators=[Required()])
    submit = SubmitField('Update Bio')

class CommentForm(FlaskForm):
    comment = TextAreaField('', validators=[Required()], render_kw={"placeholder": "Post your comment"})
    submit = SubmitField('Post Comment')