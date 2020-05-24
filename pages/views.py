from django.shortcuts import render
from shows.models import Shows

# Create your views here.


def home_view(request):
    context = {
        'title': 'Hello World'
    }
    if request.user.is_authenticated:
        queryset = Shows.objects.published()
    else:
        queryset = Shows.objects.published()[:5]

    context['queryset'] = queryset

    return render(request, 'home.html', context)


def about_view(request):
    context = {
        'title': 'About me'
    }
    return render(request, 'about.html', context)
