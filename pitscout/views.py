from django.shortcuts import render
from .models import pitscout
from .forms import pitscout_form
# Create your views here.

def pitscoutview(request):

	if request.method == 'POST':

		teamnum = request.session.get('team_num')
		if teamnum == -1:
			form = pitscout_form(request.POST,request.FILES)
		else: 
			prof = pitscout.objects.get(team_number=teamnum)
			form = pitscout_form(request.POST,request.FILES,instance=prof)
		
		if form.is_valid():
			obj = form.save(commit=False)
			obj.save()
			form.save_m2m()
			search_run = True
		else:
			form = pitscout_form()
			search_run = False
	else:
		form = pitscout_form()
		search_run = False

	return render(request, 'pitscout.html', {'form': form, 'search_run':search_run})

def pitscoutedit(request):
	if request.method == 'GET':
		team_number = request.GET.get('team_number', 0)
		search_run = True
		if team_number == 0:
			form = pitscout_form()
			request.session['team_num'] = -1
		else: 
			try:
				prof = pitscout.objects.get(team_number=team_number)
				form = pitscout_form(instance=prof)
				request.session['team_num'] = team_number
			except:
				form = pitscout_form()
				request.session['team_num'] = -1
	
	return render(request, 'pitscoutedit.html', {'form': form, 'search_run':search_run})
