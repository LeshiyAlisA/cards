# Create your views here.
from django.shortcuts import render_to_response
from cards.board.forms import SaveWord



def test(request):
    if request.method=="POST":
        form=SaveWord(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print cd['translate']
            print cd['word']
            print cd['value']
        
    else:
        form=SaveWord()

    return render_to_response('index.html',locals())


