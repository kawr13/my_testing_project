from django.shortcuts import render

from portfolio.models import Projects


# Create your views here.


def index(request):
    projects = Projects.objects.all()
    context = {
        'title': 'My portfolio',
        'projects': projects,
    }
    return render(request, 'portfolio/portfolio.html', context=context)
