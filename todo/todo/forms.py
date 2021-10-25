from django import forms
from django.forms import ModelForm
from django.db.models import fields

from .models import *

class TehtavaLomake(forms.ModelForm):

    class Meta:
        model = Tehtava
        fields = ('otsikko', 'muistiinpano', 'tehty')