from django.shortcuts import render
from softapp.algo_rytm import genereting_pass
# Create your views here.


def index(request):
    return render(request, 'generating/index.html')


def generat_pass(request):
    return render(request, 'generating/generating.html')

def password(request):
    uppers = request.GET.get('Uppercase')
    numbers = request.GET.get('Number')
    special = request.GET.get('Special')
    length = int(request.GET.get('Length', '12')) if int(request.GET.get('Length', '12')) < 12 else 12
    testing = genereting_pass(length, uppers, numbers, special)
    context = {
        'password': testing
    }
    return render(request, 'generating/password.html', context=context)