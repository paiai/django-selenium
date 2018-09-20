from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

def index(request):
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html', context)
    return render(request, 'search_app/index.html')
