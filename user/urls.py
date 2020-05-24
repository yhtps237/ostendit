from django.urls import path
from .views import (
    signup_view,
    login_view,
    logout_view,
    user_profile_view,

)

app_name = 'user'
urlpatterns = [
    path('signup/', signup_view, name="signup_view"),
    path('login/', login_view, name="login_view"),
    path('logout/', logout_view, name="logout_view"),
    path('<str:username>/', user_profile_view, name="user_profile_view"),
]
