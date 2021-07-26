from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import CreateView
from .forms import BbForm
from .models import DB


def menu(request):
    return render(request, 'menu/Menu.html')


def get_question():
    questions = DB.objects.order_by('?')[:3]
    firstq = questions[0]
    secoundq = questions[1]
    thirdq = questions[2]
    question1 = firstq.question
    correct_answer1 = firstq.answer
    question2 = secoundq.question
    correct_answer2 = secoundq.answer
    question3 = thirdq.question
    correct_answer3 = thirdq.answer

    return question1, \
           question2, \
           question3, \
           correct_answer1, \
           correct_answer2, \
           correct_answer3


def start_the_quiz(request):
    question1, question2, question3, correct_answer1, correct_answer2, correct_answer3 = get_question()
    count = 0
    if request.method == 'POST':
        if request.POST['1'] == str(correct_answer1):
            count += 1
        if request.POST['2'] == str(correct_answer2):
            count += 1
        if request.POST['3'] == str(correct_answer3):
            count += 1
        print(count)
        return render(request, 'menu/results.html', {'count': count})
    else:
        return render(request, 'menu/startq.html', {"question1": question1, "question2": question2, "question3": question3})


def results(request):
    return render(request, 'menu/results.html')


def create(request):
    if request.user.is_authenticated:
        return render(request, 'menu/create.html')
    else:
        return redirect('menu')


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
