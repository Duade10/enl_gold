from django.shortcuts import render
from django.views import View


class MediaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'medias/media.html')


class PhotoAlbumView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'medias/ouralbum.html')
