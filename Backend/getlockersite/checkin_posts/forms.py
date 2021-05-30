from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class SewaForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    checkin_btn = SubmitField('Check in')



class SewaForm2(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    checkin_btn2 = SubmitField('Check in')

class AddFingerprintForm(FlaskForm):
    # no empty titles or text possible
    # we'll grab the date automatically from the Model later
    addfinger_btn = SubmitField('Add Fingerprint')