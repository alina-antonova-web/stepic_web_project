from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET, require_POST

from .models import Question, Answer
from .forms import AskForm, AnswerForm
from .paginate import paginate


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions_list(request):
    questions = Question.objects.new()
    limit = 10
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        # 'user': request.user,
    })


def popular_questions_list(request):
    questions = Question.objects.popular()
    limit = 10
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        # 'user': request.user,
    })


def question_details(request, num):
    question = get_object_or_404(Question, id=num)
    answers = Answer.objects.filter(question=question.pk).order_by('-added_at')[0:10]
    if request.method == "POST":
        answer_form = AnswerForm(request.POST)
        if answer_form.is_valid():
            # answer_form._user = request.user
            answer = answer_form.save()
            url = answer.question.get_url()
            return HttpResponseRedirect(url)
    else:
        answer_form = AnswerForm(initial={'question': question.pk})

    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        # 'user': request.user,
        'form': answer_form,
    })
    

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            # form._user = request.user
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form, 
                                        # 'user': request.user,
                                        })

