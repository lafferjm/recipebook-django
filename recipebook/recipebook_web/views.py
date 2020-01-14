from django.shortcuts import render

def index(request):
    return render(request, 'recipebook_web/index.html')
