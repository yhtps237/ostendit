from django.shortcuts import render
from .models import Search
from shows.models import Shows
# Create your views here.


def search_view(request):
    query = request.GET.get('q')
    context = {
        'query': query
    }
    user = None
    if request.user.is_authenticated:
        user = request.user
    if query is not None:
        Search.objects.create(user=user, query=query)
        queryset = Shows.objects.published().search(query)
        context['list'] = queryset
    return render(request, 'searches/search.html', context)
