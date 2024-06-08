from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views import View

from .models import Job


class JobsView(View):
    def get(self, request):
        jobs = Job.objects.filter(is_active=True).order_by('-created_at')

        is_jobs_exist = jobs.exists()

        if is_jobs_exist:
            items_per_page = 10
            paginator = Paginator(jobs, items_per_page)
            page = request.GET.get('page')

            try:
                jobs_page = paginator.page(page)
            except PageNotAnInteger:
                jobs_page = paginator.page(1)
            except EmptyPage:
                jobs_page = paginator.page(paginator.num_pages)

            context = {
                "jobs": jobs_page,
                "is_jobs_exist": is_jobs_exist
            }
            return render(request, 'jobs/available.html', context=context)
        else:
            context = {
                "jobs": jobs,
                "is_jobs_exist": is_jobs_exist
            }
            return render(request, 'jobs/no-available.html', context=context)


class ApplicationView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'jobs/application.html')
