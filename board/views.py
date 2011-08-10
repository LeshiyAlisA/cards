# Create your views here.
from django.shortcuts import render_to_response
from cards.board.forms import SaveWord
from cards.board.models import word
from cards.board.translate import translate

def test(request):
    if request.method=="POST":
        form=SaveWord(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            wr=word()
            wr.word=cd['word']
            wr.transcription=cd['transcription']
            wr.value=cd['value']
            wr.id_user=1
            wr.save()
            tr=translate()
            tr.test(wr.word)
    else:
        form=SaveWord()

    return render_to_response('index.html',locals())


