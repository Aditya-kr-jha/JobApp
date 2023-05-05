from django import forms
from uploadapp.models import Upload, UploadFiles


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = '__all__'


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFiles
        fields = '__all__'
