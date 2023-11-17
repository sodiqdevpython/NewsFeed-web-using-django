from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import ContactForm
from django.views.generic import ListView
# Create your views here.

def homepage(request):
	data = News.objects.all()[:5]
	category_list = Category.objects.all()
	local = News.objects.all().filter(category__name="Mahalliy")[:5]
	texnalogiya = News.objects.all().filter(category__name="Texnalogiya")[::-1][:5]
	talim = News.objects.all().filter(category__name="Ta'lim")[:5]
	iqtisodiyot = News.objects.all().filter(category__name="Iqtisodiyot")[::-1][:5]
	context = {
		'data_slider': data,
		'local':local,
		'category_list':category_list,
		'texnalogiya':texnalogiya,
		'talim':talim,
		'iqtisodiyot':iqtisodiyot
	}
	return render(request, 'index.html', context=context)

def get_404(request):
	data = News.objects.all()[::-1][:5]
	context = {
		'data_slider': data
	}
	return render(request, '404.html', context=context)

def detail(request, slug):
	data_detail = get_object_or_404(News, slug = slug)
	context = {
		'data_detail': data_detail
	}
	return render(request, 'single_page.html', context = context)

def contact(request):
	data = News.objects.all()[::-1][:5]
	form = ContactForm(request.POST or None)
	if form.is_valid() and request.method=="POST":
		form.save()
		return redirect("home")
	context = {
		"form":form,
		"posts": data
	}
	return render(request,'contact.html',context)


def mahalliy(request):
	data = News.objects.all().filter(category__name = 'Mahalliy')
	context = {
		'data':data
	}
	return render(request, 'mahalliy_news.html',context) 

class TechView(ListView):
	model = News
	template_name = 'texnalogiya.html'
	context_object_name = 'tech'

	def get_queryset(self):
		news = self.model.all().filter(category__name='Texnalogiya')