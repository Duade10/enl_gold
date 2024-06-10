from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from . import models


class EventView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        events = models.Event.objects.order_by('-created_at')

        is_events_exist = events.exists()

        if is_events_exist:
            items_per_page = 10
            paginator = Paginator(events, items_per_page)
            page = request.GET.get('page')

            try:
                events_page = paginator.page(page)
            except PageNotAnInteger:
                events_page = paginator.page(1)
            except EmptyPage:
                events_page = paginator.page(paginator.num_pages)
            context = {
                "events": events_page,
                "is_events_exist": is_events_exist
            }
        return render(request, "events/events.html", context)
