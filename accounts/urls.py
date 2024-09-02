from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('csrf/', views.get_csrf_token, name='get_csrf_token'),
    path('user/', views.get_user_info, name='user'),
]