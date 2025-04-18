from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TelField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message='Please enter a valid email address')
    ])
    
    phone = TelField('Phone Number', validators=[
        Length(max=20, message='Phone number must be less than 20 characters')
    ])
    
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=1000, message='Message must be between 10 and 1000 characters')
    ])
    
    submit = SubmitField('Send Message')
