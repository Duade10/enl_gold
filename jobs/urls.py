from django.urls import path
from . import views

app_name = "jobs"

urlpatterns = [
    path('', views.JobsView.as_view(), name="jobs"),
    path('application', views.ApplicationView.as_view(), name="application")
]