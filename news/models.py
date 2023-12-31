from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length = 200)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

class News(models.Model):
	title = models.CharField(max_length = 250)
	slug = models.SlugField(max_length = 250)
	body = models.TextField()
	image = models.ImageField(upload_to = 'media/')
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	publish_time = models.DateTimeField(auto_now = True)
	created_time = models.DateTimeField(auto_now_add= True)
	is_avilable = models.BooleanField(default=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Yangilik'
		verbose_name_plural = 'Yangiliklar'

class Contact(models.Model):
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length = 200)
	message = models.TextField()
	send_time = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'Xabar'
		verbose_name_plural = 'Xabarlar'


class Comments(models.Model):
	name = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField(max_length=800)
	time = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.comment[:20]

	class Meta:
		verbose_name = 'Kamentariya'
		verbose_name_plural = 'Kamentariyalar'