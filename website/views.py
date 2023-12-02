from django.shortcuts import render, redirect
from django.http import HttpResponse
from news.forms import ArticlesForm
def index(request):
	return render(request, 'website/index.html')

def read(request):
	return render(request, 'website/news.html')

def create(request):
	error = ''
	if request.method == 'POST':
		form = ArticlesForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('news_home')
		else:
			error = 'Форма была неверной'
	form = ArticlesForm()

	return render(request, 'website/create.html', {'form': form, 'error': error})