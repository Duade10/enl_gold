from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', views.AboutView.as_view(), name='about'),
    path('service', views.ServiceView.as_view(), name='service'),
    path('team', views.TeamView.as_view(), name='team'),
    path('events', views.EventView.as_view(), name='events'),
]
