from django.shortcuts import render
from django.contrib.auth.models import User


def home_view(request):
    qs = User.objects.all()
    return render(request, 'main.html', {'qs': qs})
