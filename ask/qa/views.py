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
    })


@require_GET
def question_details(request, num):
    question = get_object_or_404(Question, id=num)
    answers = Answer.objects.filter(question=num).order_by('-added_at').all()[:]
    answer_form = AnswerForm({"question": question.id})
    return render(request, 'question.html', {
        'question': question,
        'answers': answers,
        'form': answer_form
    })

@require_POST
def answer_add(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        form.author = 1
        answer = form.save()
        return redirect(answer.question)

def ask(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            form.author = 1
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask.html', {'form': form, })

