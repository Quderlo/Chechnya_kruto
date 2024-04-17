from django.urls import include, path
from .views import views

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    path('register/', views.UserRegister.as_view(), name='register'),
    path('logout/', views.UserLogin.as_view(), name='logout'),
    path('user/', views.UserView.as_view(), name='user'),
]