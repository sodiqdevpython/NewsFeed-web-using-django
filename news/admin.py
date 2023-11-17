from django.contrib import admin
from .models import Contact ,Category ,News
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ['title','category','created_time','is_avilable']
	prepopulated_fields = {"slug": ('title',)}
	list_filter = ['category', 'created_time', 'is_avilable']
	search_fields = ['title', 'body']
	date_hierarchy = 'created_time'

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'send_time']
	search_fields = ['name', 'email', 'message']
	list_filter = ['send_time']
	date_hierarchy = 'send_time'