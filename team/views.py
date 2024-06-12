from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views import View

from .models import TeamMember


class TeamView(View):
    def get(self, request, *args, **kwargs):
        context = {}
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
            context = {
                "team_members": team_members_page,
                "is_team_members_exist": is_team_members_exist
            }
        return render(request, "team/team.html", context)
