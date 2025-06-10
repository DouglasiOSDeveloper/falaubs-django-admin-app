import os
import json
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.conf import settings
from urllib.parse import unquote

def normalize_name(name):
    """Normalize UBS name for matching."""
    return name.lower().replace(' ', '').replace('-', '').replace('_', '').strip()

def ubs_detail_view(request, ubs_name):
    """View for displaying UBS details."""
    # Load centralized UBS data from staticfiles directory (correct one)
    json_path = os.path.join(settings.BASE_DIR, 'staticfiles', 'mock_data', 'ubs_data.json')
    
    try:
        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Http404("UBS data not found")

    # URL decode the UBS name and normalize it
    decoded_name = unquote(ubs_name)
    normalized_name = normalize_name(decoded_name)
    
    # Find UBS by normalized name
    ubs = next((u for u in data['ubsList'] if normalize_name(u['name']) == normalized_name), None)
    if not ubs:
        raise Http404(f"UBS not found: {decoded_name}")

    # Determine open/closed status (mocked as always open for now)
    ubs['status'] = "Aberta"

    return render(request, 'vaccination/ubs_detail.html', {'ubs': ubs})
