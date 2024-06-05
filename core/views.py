from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/index.html')


class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/about.html')


class ServiceView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/service.html')


class TeamView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'core/team.html')
