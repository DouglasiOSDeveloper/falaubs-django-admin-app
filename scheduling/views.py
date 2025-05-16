from django.shortcuts import render

def scheduling_mock_view(request):
    # Mock data for scheduling steps
    steps = [
        "Tipo de Consulta/Exame",
        "Especialidade",
        "Unidade de Saúde (UBS)",
        "Data e Horário",
        "Confirmação"
    ]
    return render(request, "scheduling/scheduling.html", {"steps": steps})
