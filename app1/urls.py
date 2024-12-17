from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    ]
