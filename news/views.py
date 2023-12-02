from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView


def news_home(request):
	news = Articles.objects.order_by('-date')
	return render(request, 'website/news.html', {'news': news})

class NewsDetail(DetailView):
	model = Articles
	template_name = 'website/details_view.html'
	context_object_name = 'article'