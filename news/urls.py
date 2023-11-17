from django.urls import path
from .views import homepage, get_404, detail,contact, mahalliy,TechView

urlpatterns = [
	path('', homepage, name = 'home'),
	path('wrong/', get_404, name = 'wrong'),
	path('article/<slug:slug>/', detail, name = 'detail'),
	path('contact/',contact, name='contact'),
	path('mahalliy/', mahalliy, name='mahalliy'),
	path('texnalogiya/', TechView.as_view(), name='texnalogiya')
]