from flask_uploads import UploadSet, IMAGES
from wtforms import Form, BooleanField, TextAreaField
#StringField, RadioField, SelectField, validators
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired

photos = UploadSet('photos', IMAGES)

class UpdateMoviesForm(Form):
#    movie_title = TextAreaField('Movie Title', validators=[DataRequired()])
    movie_image = FileField(validators=[FileRequired()])
    movie_name = TextAreaField('Movie Name', validators=[DataRequired()])
    movieagerating = TextAreaField('Movie Rating', validators=[DataRequired()])
    movieduration = TextAreaField('Movie Duration', validators=[DataRequired()])
    gvexclusivetag = BooleanField('GV EXCLUSIVE?')
    #choices  =['Horror','Drama','Comedy','Science','Romance','Animation','Crime Film','Thriller','Adventure','Emotional','Mystery','Action']
    movieHorror = BooleanField('Horror')
    movieDrama = BooleanField('Drama')
    movieComedy = BooleanField('Comedy')
    movieScience = BooleanField('Science')
    movieRomance = BooleanField('Romance')
    movieAnimation = BooleanField('Animation')
    movieCrimeFilm = BooleanField('CrimeFilm')
    movieThriller = BooleanField('Thriller')
    movieAdventure = BooleanField('Adventure')
    movieEmotional = BooleanField('Emotional')
    movieMystery = BooleanField('Mystery')
    movieAction = BooleanField('Action')
#Form object – Used to create a WTForms Form.
#StringField object – Used to create an HTML textfield.
#RadioField object – Used to create an HTML radio button group.
#SelectField object – Used to create an HTML dropdown list.
#TextAreaField object – Used to create an HTML textarea.
#validators object – validators allow you to specify the constraints for each of the fields such as minimum and maximum length, DataRequried or Optional.

