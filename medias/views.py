from django.shortcuts import render
from django.views import View
from .models import MachineAndEquipment, PhotoAlbum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class MediaView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        machine_and_equipments = MachineAndEquipment.objects.order_by('-created_at')

        is_machine_and_equipments_exist = machine_and_equipments.exists()

        if is_machine_and_equipments_exist:
            items_per_page = 10
            paginator = Paginator(machine_and_equipments, items_per_page)
            page = request.GET.get('page')

            try:
                machine_and_equipments_page = paginator.page(page)
            except PageNotAnInteger:
                machine_and_equipments_page = paginator.page(1)
            except EmptyPage:
                machine_and_equipments_page = paginator.page(paginator.num_pages)
            context = {
                "machine_and_equipments": machine_and_equipments_page,
                "is_machine_and_equipments_exist": is_machine_and_equipments_exist
            }
        return render(request, 'medias/media.html', context)


class PhotoAlbumView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        photo_albums = PhotoAlbum.objects.order_by('-created_at')

        is_photo_album_exist = photo_albums.exists()

        if is_photo_album_exist:
            items_per_page = 10
            paginator = Paginator(photo_albums, items_per_page)
            page = request.GET.get('page')

            try:
                photo_albums_page = paginator.page(page)
            except PageNotAnInteger:
                photo_albums_page = paginator.page(1)
            except EmptyPage:
                photo_albums_page = paginator.page(paginator.num_pages)
            context = {
                "photo_albums": photo_albums_page,
                "is_photo_album_exist": is_photo_album_exist
            }
        return render(request, 'medias/ouralbum.html', context)
