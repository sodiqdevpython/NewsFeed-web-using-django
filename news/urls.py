from django.urls import path
from .views import homepage, get_404, detail,contact,UpdateNews,DeleteNews

urlpatterns = [
	path('', homepage, name = 'home'),
	path('wrong/', get_404, name = 'wrong'),
	path('article/<slug:slug>/', detail, name = 'detail'),
	path('contact/',contact, name='contact'),
	path('article/<slug:slug>/edit/', UpdateNews.as_view(), name='edit'),
	path('article/<slug:slug>/delete/', DeleteNews.as_view(), name='del')
]