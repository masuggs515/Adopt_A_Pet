from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPet(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Picture URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Additionl Notes")

class EditPet(FlaskForm):
    photo_url = StringField("Picture URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[NumberRange(min=0, max=30)])
    notes = StringField("Additionl Notes")