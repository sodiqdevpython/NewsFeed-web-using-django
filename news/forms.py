from django import forms
from .models import Contact, News, Comments

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = "__all__"

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comments
		fields = ('comment',)