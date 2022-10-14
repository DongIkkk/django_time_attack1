from django.urls import path
from user import views


urlpatterns = [
    path('signup/', views.sign_up, name='sign-up'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
]