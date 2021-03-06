from django.shortcuts import render
from .forms import matchscout_form
from .models import matchscout
from django.db.models import Avg, Max, Min
# Create your views here.

def index(request):
	return render(request, 'index.html')

def matchscout_view(request):
	if request.method == 'POST':
		form = matchscout_form(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form.save_m2m()
	
	form = matchscout_form()
	return render(request, 'matchscout.html', {'form': form})

def teamsummary(request):
	if request.method == 'GET':
		team_number = request.GET.get('team_number', 0)
		results = matchscout.objects.filter(team_num = team_number)
		average = list(results.aggregate(Avg('score')).values())[0]
		maximum = list(results.aggregate(Max('score')).values())[0]
		minimum = list(results.aggregate(Min('score')).values())[0]
		if team_number != 0:
			search_run = True
			return render(request, 'teamsummary.html', {'results': results, 'search_run':search_run, 'score_avg': average, 'score_max': maximum, 'score_min': minimum})
		else:
			search_run = False
			return render(request, 'teamsummary.html', {'search_run':search_run})
	else:
		search_run = False
		return render(request, 'teamsummary.html', {'search_run':search_run}) 
