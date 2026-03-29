from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tours/', views.all_tours, name='all_tours'), # This fixes the error!
    path('tour/<int:tour_id>/', views.tour_detail, name='tour_detail'),
    path('booking-success/', views.success, name='success'),
    path('about/', views.about, name='about'),
    path('terms/', views.terms, name='terms'),
]