from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo
from wtforms import ValidationError
from ..models import User

class SignUpForm(FlaskForm):
    '''
    Sign up form where new users can register into the app
    '''
    email = StringField('', validators=[Required(), Email()], render_kw={"placeholder": "Enter your email address"})
    username = StringField('', validators=[Required()], render_kw={"placeholder": "Enter your preferred username"})
    password = PasswordField('', validators=[Required(), EqualTo('confirm_password',message = 'Passwords must match')], render_kw={"placeholder": "Enter your referred password"})
    confirm_password = PasswordField('', validators=[Required()], render_kw={"placeholder": "Confirm password"})
    submit = SubmitField('Sign Up')
    
    # Custom validators     
    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('That username is taken')    
    
    
class SignInForm(FlaskForm):
    '''
    Sign in forms where registered users can log/sign-in
    '''
    username = StringField('', validators=[Required()], render_kw={"placeholder": "Enter your username"})
    password = PasswordField('', validators=[Required()], render_kw={"placeholder": "Enter your password"})
    remember = BooleanField('Keep me signed in')
    submit = SubmitField('Sign In')