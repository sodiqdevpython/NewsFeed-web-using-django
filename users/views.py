from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, UpdateView
from .models import Profile
from django.contrib.auth.decorators import login_required


@login_required()
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'user_profile.html', context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'