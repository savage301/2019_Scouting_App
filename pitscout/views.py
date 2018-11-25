from django.shortcuts import render

# Create your views here.
def pitscout(request):
	return render(request, 'pitscout.html')