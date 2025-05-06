import requests
import plotly.express as px
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages

def informacoes_admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('password')

        try:
            response = requests.post(
                "http://localhost:5000/auth/login",
                json={"email": email, "password": senha}
            )
            if response.status_code == 200:
                token = response.json().get("access_token")
                request.session['admin_token'] = token
                return redirect('dashboard_admin')
            else:
                messages.error(request, 'Credenciais inválidas.')
        except Exception as e:
            print(f"Erro na autenticação: {e}")
            messages.error(request, 'Erro ao conectar à API.')

    return render(request, 'core/admin/login_admin.html')

def dashboard_pets(request):
    try:
        response = requests.get("http://localhost:5000/pets/")
        pets = response.json()
        
        response_clinics = requests.get("http://localhost:5000/clinics/")
        clinics = response_clinics.json()
    except Exception as e:
        pets, clinics = [], []
        print(f"Erro ao consumir API: {e}")

    df_pets = pd.DataFrame(pets)
    df_clinics = pd.DataFrame(clinics)

    df_merged = df_pets.merge(df_clinics, left_on='clinic_id', right_on='id', how='left')
    df_merged['name_y'] = df_merged['name_y'].fillna('Sem Clínica')

    grafico_clinica = px.pie(
        df_merged,
        names='name_y',
        title='Distribuição de Pets por Clínica'
    )
    grafico_clinica_html = grafico_clinica.to_html(full_html=False)

    df_especie = df_pets['species'].value_counts().reset_index(name='count')
    df_especie.columns = ['species', 'count']

    grafico_especie = px.bar(
        df_especie,
        x='species',
        y='count',
        labels={'species': 'Espécie', 'count': 'Quantidade'},
        title='Quantidade de Pets por Espécie'
    )

    grafico_especie_html = grafico_especie.to_html(full_html=False)

    return render(request, 'core/admin/dashboard.html', {
        'pets': pets,
        'clinics': clinics,
        'grafico_clinica': grafico_clinica_html,
        'grafico_especie': grafico_especie_html
    })
