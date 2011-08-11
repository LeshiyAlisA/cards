__author__ = 'leshiy'

from django import forms

class SaveWord(forms.Form):
    word=forms.CharField()
    transcription=forms.CharField()
    value=forms.CharField()

class AddWords(forms.Form):
    words=forms.CharField(widget=forms.Textarea)

