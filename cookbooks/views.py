from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	# return HttpResponse("test")
	return render(request, 'index.html', {})

def google3442(request):
	return render(request, 'google3442c2f65fabc905.html', {})