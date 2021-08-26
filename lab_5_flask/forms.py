from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, TextAreaField, IntegerField
from wtforms.fields import html5
from wtforms.validators import DataRequired, NumberRange


class SendForm(FlaskForm):
    name = StringField("name", validators=[DataRequired(message="заповніть поле")])
    lastname = StringField("lastname", validators=[DataRequired(message="заповніть поле")])
    age = html5.IntegerField("age", validators=[DataRequired(message="заповніть поле"),NumberRange(min=0, max=100,message="невірна довжина")])
    txt = TextAreaField("txt", validators=[DataRequired(message="заповніть поле")])
    submit = SubmitField('Відправити')
