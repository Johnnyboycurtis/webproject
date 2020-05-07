from django.forms import ModelForm
from mainapp.models import Data


class DataForm(ModelForm):
    class Meta:
        model = Data
        fields = ['category', 'quantity']