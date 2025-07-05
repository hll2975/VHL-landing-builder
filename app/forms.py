from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import DataRequired

class LandingForm(FlaskForm):
    slug = StringField('Nombre de la página', validators=[DataRequired()])
    title = StringField('Título principal', validators=[DataRequired()])
    description = StringField('Descripción breve', validators=[DataRequired()])
    theme = SelectField('Plantilla', choices=[
        ('modern', 'Moderna'),
        ('classic', 'Clásica')
    ])
    submit = SubmitField('Crear Landing')
