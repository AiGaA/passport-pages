from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.


def home(request):
    return render(request, 'blog/index.html')


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'blog/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'blog/login.html', context)
