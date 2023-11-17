from .models import News

def last_news(request):
	news = News.objects.all().order_by('-id')[:6]
	context = {
		'news_ticker': news
	}
	return context