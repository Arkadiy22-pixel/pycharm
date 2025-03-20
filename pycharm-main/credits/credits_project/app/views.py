from  django.shortcuts import render,redirect


def admin(request):
    template = 'Admin.html'
    context = {}
    return render(request, template, context)

def general(request):
    template = 'General.html'
    context = {}
    return render(request, template, context)

def login(request):
    template = 'Login.html'
    context = {}
    return render(request, template, context)

def my_applications(request):
    template = 'My_applications.html'
    context = {}
    return render(request, template, context)
def registration(request):
    template = 'Registration.html'
    context = {}
    return render(request, template, context)
def logout(request):
    return redirect('registration')

# Create your views here.
