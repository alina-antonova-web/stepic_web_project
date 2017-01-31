from django.http import HttpResponse
def test(request, *args, **kwargs):
	return HttpResponse('OK', status=200)
