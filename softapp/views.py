from django.shortcuts import render, HttpResponse
from .algo_rytm import genereting_pass
# Create your views here.



def index(request):
    if request.method == 'POST':
        response = request.POST.get('num')
        if response:
            number = int(response)
            password = genereting_pass(number)
            context = {'password': password}
            return render(request, 'softapp/index.html', context=context)
    return render(request, 'softapp/index.html')