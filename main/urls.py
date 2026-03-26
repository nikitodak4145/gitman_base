from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('abilities/', views.abilities, name='abilities'),
    path('missions/', views.missions, name='missions'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('increase-seed/', views.increase_seed, name='increase_seed'),
    path('decrease-seed/', views.decrease_seed, name='decrease_seed'),
    path('add-mission/', views.add_mission, name='add_mission'),
    path('get-tip/', views.get_tip, name='get_tip'),
    path('api/missions/', views.api_missions, name='api_missions'),
    path('api/seed/', views.api_seed, name='api_seed'),
]