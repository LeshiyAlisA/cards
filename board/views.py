# Create your views here.
from django.shortcuts import render_to_response
from cards.board import forms
from cards.board.models import word
from cards.board.translate import translate

def AddWords(request):
    if request.method=='POST':
        form=forms.AddWords(request.POST)
        if form.is_valid():
            tr=translate()
            cd=form.cleaned_data
            words=cd['words']
            for wrd in words.split():
                value=tr.ValueTranscription(wrd)
                wr=word()
                wr.transcription=value['transcription']
                wr.value=value['value']
                wr.word=wrd
                wr.id_user=1
                wr.save()

            

    form= forms.AddWords()
    return render_to_response('index.html',locals())



def test(request):
    if request.method=='POST':
        form=forms.SaveWord(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            wr=word()
            wr.word=cd['word']
            tr=translate()
            value=tr.ValueTranscription(wr.word)
            wr.transcription=value['transcription']
            wr.value=value['value']
            wr.id_user=1
            wr.save()

    else:
        form=forms.SaveWord()

    return render_to_response('index.html',locals())


