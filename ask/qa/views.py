from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET

from .models import Question, Answer
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
	question = get_object_or_404(Question, id = num)
	return render(request, 'question.html', {
		'question': question,
		'answers': question.answers.all()[:],
	})