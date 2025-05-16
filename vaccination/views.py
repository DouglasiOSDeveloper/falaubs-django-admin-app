from django.shortcuts import render

def vaccination_mock_view(request):
    # Mock vaccine data
    vaccines = [
        {"name": "Vacina A", "description": "Descrição da Vacina A", "age_group": "0-5 anos"},
        {"name": "Vacina B", "description": "Descrição da Vacina B", "age_group": "6-12 anos"},
        {"name": "Vacina C", "description": "Descrição da Vacina C", "age_group": "Adultos"},
    ]
    return render(request, "vaccination/vaccination.html", {"vaccines": vaccines})
