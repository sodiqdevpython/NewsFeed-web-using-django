from django.shortcuts import render

# Create your views here.
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'user_profile.html', context)