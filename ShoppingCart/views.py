from django.shortcuts import redirect, render

def index(request):
    # O Django apenas irá renderizar templates de aplicações
    # Tenha certeza de que seu arquivo html esteja em uma aplicação
    return render(request, "index.html")