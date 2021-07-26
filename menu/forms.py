from django.forms import ModelForm
from .models import DB


class BbForm(ModelForm):
    class Meta:
        model = DB
        fields = ('question', 'answer')
