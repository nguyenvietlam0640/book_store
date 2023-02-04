from django.shortcuts import render

# Create your views here.
def register(request):
    pass


def login(request):
    pass


def home(request):
    l =[]
    for i in range(100):
        l.append(i)
    return render(request, 'base.html', {'len' : l})