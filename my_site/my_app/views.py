
from django.shortcuts import render

def index(request):
    return render(request, 'myapp/index.html')  # Ensure the template path is correct
