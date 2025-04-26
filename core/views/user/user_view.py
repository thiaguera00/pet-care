from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='login')
def informacoes_usuario(request):
    usuario = request.user
    return render(request, 'core/user/user.html', {'usuario': usuario})