from django.shortcuts import render

from django.http import HttpResponse

from .models import Question, Answer
from django.http import Http404
# Create your views here.


def index(request):
    question_list = Question.objects.order_by('-published')
    context = {'question_list': question_list}
    return render(request, 'index.html', context)


def question(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question not found!")
    context = {'question': question}
    return render(request, 'question.html', context)
