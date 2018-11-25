from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html')

def matchscout(request):
	return render(request, 'matchscout.html')
