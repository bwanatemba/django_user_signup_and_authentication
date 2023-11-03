from django.shortcuts import render, redirect
from biasharaapp.models import Member


# Create your views here.
def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        member = Member(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                        email=request.POST['email'], username=request.POST['username'],
                        password=request.POST['password'])
        member.save()
        return redirect('/')
    else:
        return render(request, 'register.html')


def index(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'index.html', {'member': member})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def inner(request):
    return render(request, 'inner-page.html')


def about(request):
    return render(request, 'about.html')
