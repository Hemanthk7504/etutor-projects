from django.shortcuts import render


def clothes_donation(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def verify_email(request):
    return render(request, 'verify_email.html')


def activation(request, token):
    return render(request, 'activation.html')


def login(request):
    return render(request, 'login.html')


def dashboard(request):
    return render(request, 'dashboard.html')
