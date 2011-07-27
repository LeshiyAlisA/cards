# Create your views here.
from django.shortcuts import render_to_response
from cards.board.forms import SaveWord
from django.core.context_processors import csrf


def test(request):
    c = {}
    c.update(csrf(request))

    if request.method=="POST":
        form=SaveWord(request.POST)
    else:
        form=SaveWord()

    return render_to_response('index.html',{'form':form,'c':c})


