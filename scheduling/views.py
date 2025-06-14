import os
import json
from django.shortcuts import render
from django.conf import settings

def scheduling_view(request):
    # Load UBS data from JSON
    json_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'mock_data', 'ubs_data.json')
    with open(json_path, 'r', encoding='utf-8') as file:
        ubs_data = json.load(file)

    # Mock user data
    user_data = {
        "name": "Carlos Pereira",
        "cpf": "123.456.789-10"
    }

    context = {
        "ubs_data": json.dumps(ubs_data),
        "user_data": user_data
    }
    
    return render(request, "scheduling/scheduling.html", context)
