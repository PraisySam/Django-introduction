from django.shortcuts import render , HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse("this is homepage")

def project(request):
    return render(request,'project.html')

def team(request):
    return render(request,'team.html')

def events(request):
    
    return render(request,'events.html')

def idea(request):
    return render(request,'idea.html')