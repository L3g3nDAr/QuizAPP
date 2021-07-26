from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from .forms import BbForm

from .models import DB


def menu(request):
    return render(request, 'menu/Menu.html')


def start_the_quiz(request):
    counter = 0
    questions = DB.objects.order_by('?')[:3]
    content = {'questions': questions}
    if request.method == 'POST':
        firstq = questions[0]
        secoundq = questions[1]
        thirdq = questions[2]
        print(request.POST)
        if request.POST[1] == str(firstq.answer):
            counter += 1
        if request.POST[2] == str(secoundq.answer):
            counter += 1
        if request.POST[3] == str(thirdq.answer):
            counter += 1
        return redirect('results')
    else:
        return render(request, 'menu/startq.html', content)

def results(request):
    return render(request, 'menu/results.html')

def create(request):
    return render(request, 'menu/create.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('menu')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)


class BbCreateView(CreateView):
    template_name = 'Menu/create.html/'
    form_class = BbForm
    success_url = '/'
