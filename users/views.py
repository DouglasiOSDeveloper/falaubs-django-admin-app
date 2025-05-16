from django.shortcuts import render, redirect
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")
        # Mock authentication: accept any non-empty cpf and password
        if cpf and password:
            # Redirect to home page after "login"
            return redirect("home")
        else:
            error = "CPF and password are required."
            return render(request, "users/login.html", {"error": error})
    return render(request, "users/login.html")

def home_view(request):
    # Mock home page with greeting, map placeholder, navigation cards, chat button
    return render(request, "users/home.html")

def nearby_ubs_view(request):
    # Expanded mock data for nearby UBSs with additional fields
    ubs_list = [
        {
            "name": "UBS Central",
            "address": "Rua Principal, 123",
            "district": "Centro",
            "hours": "08:00 - 17:00",
            "phone": "(61) 1234-5678",
            "vaccines": ["BCG", "Hepatite B", "Febre Amarela", "DTP", "Poliomielite"],
            "services": ["Consulta Geral", "Pediatria", "Vacinação", "Exames", "Atendimento 24h"],
            "accessibility": ["Acesso para cadeirantes", "Sinalização em Braille"],
            "age_groups": ["Crianças", "Adultos", "Idosos"],
            "distance_km": 1.2,
        },
        {
            "name": "UBS Norte",
            "address": "Av. Norte, 456",
            "district": "Norte",
            "hours": "07:00 - 16:00",
            "phone": "(61) 2345-6789",
            "vaccines": ["Hepatite A", "Tríplice Viral", "HPV", "Meningocócica", "Varicela"],
            "services": ["Consulta Geral", "Ginecologia", "Vacinação", "Exames", "Atendimento 24h"],
            "accessibility": ["Acesso para cadeirantes"],
            "age_groups": ["Adultos", "Idosos"],
            "distance_km": 3.5,
        },
        {
            "name": "UBS Sul",
            "address": "Rua Sul, 789",
            "district": "Sul",
            "hours": "08:00 - 18:00",
            "phone": "(61) 3456-7890",
            "vaccines": ["DTP", "Poliomielite", "Febre Amarela", "Hepatite B", "Tríplice Viral"],
            "services": ["Consulta Geral", "Cardiologia", "Vacinação", "Exames", "Atendimento 24h"],
            "accessibility": ["Sinalização em Braille"],
            "age_groups": ["Crianças", "Adultos"],
            "distance_km": 4.8,
        },
        {
            "name": "UBS Leste",
            "address": "Rua Leste, 101",
            "district": "Leste",
            "hours": "08:00 - 17:00",
            "phone": "(61) 4567-8901",
            "vaccines": ["BCG", "Hepatite B", "HPV", "Varicela", "Meningocócica"],
            "services": ["Consulta Geral", "Pediatria", "Vacinação", "Exames"],
            "accessibility": ["Acesso para cadeirantes", "Sinalização em Braille"],
            "age_groups": ["Crianças", "Adultos", "Idosos"],
            "distance_km": 2.3,
        },
        {
            "name": "UBS Oeste",
            "address": "Av. Oeste, 202",
            "district": "Oeste",
            "hours": "07:00 - 15:00",
            "phone": "(61) 5678-9012",
            "vaccines": ["Tríplice Viral", "Febre Amarela", "DTP", "Poliomielite", "Hepatite A"],
            "services": ["Consulta Geral", "Ginecologia", "Vacinação", "Exames"],
            "accessibility": ["Acesso para cadeirantes"],
            "age_groups": ["Adultos", "Idosos"],
            "distance_km": 5.0,
        },
    ]
    return render(request, "users/nearby_ubs.html", {"ubs_list": ubs_list})

def vaccination_view(request):
    return render(request, "users/vaccination.html")
