from django.shortcuts import render

def chat_mock_view(request):
    # Mock chat messages
    messages = [
        {"sender": "bot", "text": "Olá! Como posso ajudar você hoje?"},
        {"sender": "user", "text": "Gostaria de agendar uma consulta."},
        {"sender": "bot", "text": "Claro! Qual especialidade você precisa?"},
    ]
    return render(request, "chat/chat.html", {"messages": messages})
