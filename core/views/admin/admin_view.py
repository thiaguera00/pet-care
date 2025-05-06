import requests
import plotly.express as px
import pandas as pd
from django.shortcuts import render

def informacoes_admin(request):
    return render(request, 'core/admin/login_admin.html')

def dashboard_pets(request):
    try:
        response = requests.get("http://localhost:5000/pets/")
        pets = response.json()
        
        response_clinics = requests.get("http://localhost:5000/clinics/")
        clinics = response_clinics.json()
    except Exception as e:
        pets = []
        clinics = []
        print(f"Erro ao consumir API: {e}")

    # Cria DataFrames
    df_pets = pd.DataFrame(pets)
    df_clinics = pd.DataFrame(clinics)

    # Junta os dados para pegar o nome da clínica
    df_merged = df_pets.merge(df_clinics, left_on='clinic_id', right_on='id', how='left')

    # Preenche nomes vazios
    df_merged['name_y'] = df_merged['name_y'].fillna('Sem Clínica')

    # Agrupa
    grafico = px.pie(
        df_merged,
        names='name_y',  # nome da clínica
        title='Distribuição de Pets por Clínica'
    )
    grafico_html = grafico.to_html(full_html=False)

    return render(request, 'core/admin/dashboard.html', {
        'pets': pets,
        'clinics': clinics,
        'grafico_html': grafico_html
    })
