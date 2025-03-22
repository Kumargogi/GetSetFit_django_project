from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Get Set Fit")

def home(request):
    return render(request, 'home.html')

def login(request):
    context = {
        'motto' : 'DATTOBAYO'
    }
    return render(request, 'login.html',context)
    
def bulking(request):
    return render(request,'bulking.html')

def cutting(request):
    return render(request,'cutting.html')