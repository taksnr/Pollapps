from django.urls import path

from . import views

app_name = "Pollapp"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("poll/<int:poll_id>/", views.PollView.as_view(), name="poll"),
]