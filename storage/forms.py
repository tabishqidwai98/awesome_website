from django import forms
from .models import AiModel


class AimodelUploadForm(forms.ModelForm):
    class Meta:
        model = AiModel
        fields = ('name','summary','model_file','category','model_image')