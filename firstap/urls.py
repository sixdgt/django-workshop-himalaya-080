from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('country/', views.country, name='country'),
    path('province/', views.province, name='province'),
    path('add-country/', views.add_country, name='add.country'),
    path('add-province/', views.add_province, name='add.province')
]