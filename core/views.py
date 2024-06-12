from django.shortcuts import render
from django.views import View
from team.models import TeamMember
from events.models import Event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        events = Event.objects.order_by('-created_at')

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
            context["events"] = events_page
            context["is_events_exist"] = is_events_exist

        team_members = TeamMember.objects.order_by('created_at')

        is_team_members_exist = team_members.exists()

        if is_team_members_exist:
            items_per_page = 10
            paginator = Paginator(team_members, items_per_page)
            page = request.GET.get('page')

            try:
                team_members_page = paginator.page(page)
            except PageNotAnInteger:
                team_members_page = paginator.page(1)
            except EmptyPage:
                team_members_page = paginator.page(paginator.num_pages)
            context["team_members"] = team_members_page
            context["is_team_members_exist"] = is_team_members_exist
        return render(request, 'core/index.html', context)


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/about.html')


class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/service.html')


