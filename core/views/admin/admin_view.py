from django.shortcuts import render

def informacoes_admin(request):
    return render(request, 'core/admin/login_admin.html')

def dashboard_admin(request):
    return render(request, 'core/admin/dashboard.html')