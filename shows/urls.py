from django.urls import path
from .views import (
    shows_list_view,
    show_detail_view,
    show_create_view,
    show_update_view,
    show_delete_view,

)

app_name = 'shows'
urlpatterns = [
    # path('movies/', shows_list_view),
    # path('<slug:slug>/', show_detail_view),
    path('live-action/', shows_list_view, name='live-action'),
    path('animation/', shows_list_view, name='animation'),
    path('new/', show_create_view, name='new'),
    path('all/', shows_list_view, name='all'),
    path('<str:username>/<slug:slug>/', show_detail_view),
    path('<str:username>/<slug:slug>/edit/', show_update_view),
    path('<str:username>/<slug:slug>/delete/', show_delete_view),
    path('', shows_list_view),

]
