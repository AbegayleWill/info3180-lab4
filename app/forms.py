from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed,FileRequired,FileField


class UploadForm(FlaskForm):
    photo_File = FileField("Photo",validators=[FileAllowed(['jpg', 'png', 'Upload Images only!']),FileRequired()])
