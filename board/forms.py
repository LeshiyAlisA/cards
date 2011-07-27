__author__ = 'leshiy'

from django import forms

class SaveWord(forms.Form):
    word=forms.CharField()
    translate=forms.CharField()
    value=forms.CharField()

