from django.contrib import admin
from .models import Contact ,Category ,News, Comments
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

@admin.register(Comments)
class CommentsViewAdmin(admin.ModelAdmin):
	list_display = [ 'user', 'time', 'active' ]
	search_fields = [ 'user', 'body' ]
	list_filter = [ 'user', 'active' ]
	actions = ['enable_comments','disable_comments']

	def disable_comments(self, request, queryset):
		queryset.update(active=False)
	
	def enable_comments(self, request, queryset):
		queryset.update(active=True)