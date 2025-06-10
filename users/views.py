import json
import os
from django.shortcuts import render, redirect
from django.conf import settings

def load_ubs_data():
    json_path = os.path.join(settings.STATIC_ROOT, 'mock_data', 'ubs_data.json')
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        # Fallback to the static directory if STATIC_ROOT is not populated
        json_path = os.path.join(settings.BASE_DIR, 'static', 'mock_data', 'ubs_data.json')
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)

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
    # Load data from centralized JSON
    data = load_ubs_data()
    
    # Transform UBS data for the view
    ubs_list = []
    for ubs in data['ubsList']:
        # Get list of unique vaccines from this UBS
        vaccines = list(set(vaccine['name'] for vaccine in ubs['vaccines']))
        
        ubs_data = {
            'name': ubs['name'],
            'address': ubs['address'],
            'district': ubs['address'].split(',')[2].strip() if len(ubs['address'].split(',')) > 2 else "",
            'hours': ubs['openingHours'],
            'phone': ubs['phone'],
            'vaccines': vaccines,
            'services': ubs['services'],
            'accessibility': ubs['accessibility'],
            # Age groups derived from vaccines
            'age_groups': list(set(vaccine['ageGroup'].split(',')[0].strip() 
                                 for vaccine in ubs['vaccines'])),
            'distance_km': 1.2,  # This would be calculated dynamically based on user location
        }
        ubs_list.append(ubs_data)
    
    return render(request, "users/nearby_ubs.html", {"ubs_list": ubs_list})

def vaccination_view(request):
    # Load data from centralized JSON
    data = load_ubs_data()
    
    # Collect all unique vaccines across all UBS
    all_vaccines = []
    seen_vaccines = set()
    
    for ubs in data['ubsList']:
        for vaccine in ubs['vaccines']:
            if vaccine['name'] not in seen_vaccines:
                seen_vaccines.add(vaccine['name'])
                all_vaccines.append({
                    'name': vaccine['name'],
                    'description': vaccine['description'],
                    'age_group': vaccine['ageGroup'],
                    'status': vaccine['status'],
                    'scheduling': vaccine['scheduling'],
                    'unit': vaccine['unit']
                })
    
    return render(request, "users/vaccination.html", {"vaccines": all_vaccines})
