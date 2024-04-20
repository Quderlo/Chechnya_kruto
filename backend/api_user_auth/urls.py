from django.urls import path
from api_user_auth import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='auth-login'),
    path('logout/', views.UserLogout.as_view(), name='auth-logout'),
    path('register/', views.UserRegister.as_view(), name='auth-register'),
    path('profile/', views.UserDetail.as_view(), name='auth-profile'),
]