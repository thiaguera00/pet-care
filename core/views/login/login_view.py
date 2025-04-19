from django.shortcuts import render

def login(request):
     return render(request, 'core/login/login.html')