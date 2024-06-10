from django.urls import path
from . import views

app_name = "medias"

urlpatterns = [
    path("", views.MediaView.as_view(), name="medias"),
    path("photo-album", views.PhotoAlbumView.as_view(), name="photo_album")
]