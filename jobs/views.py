import os

from django.contrib import messages
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

from .forms import ApplicationForm
from .models import Job, Application


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


class ApplicationView(CreateView):
    model = Application
    form_class = ApplicationForm
    template_name = 'jobs/application.html'
    success_url = reverse_lazy('jobs:jobs')

    def form_valid(self, form):
        try:
            with transaction.atomic():
                application = form.save(commit=False)
                resume = self.request.FILES.get('resume')

                if not resume:
                    raise ValidationError("Resume file is required.")

                self.validate_file_type(resume)

                application.file = resume
                application.save()

            messages.success(self.request, "Your application has been submitted successfully!")
            return super().form_valid(form)

        except ValidationError as e:
            form.add_error('resume', str(e))
            return self.form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error in your application. Please review the form.")
        return super().form_invalid(form)

    def validate_file_type(self, file):
        allowed_types = ['.pdf', '.doc', '.docx']
        file_type = os.path.splitext(file.name)[1].lower()
        if file_type not in allowed_types:
            raise ValidationError(f"Invalid file type. Please upload a PDF or Word document. You uploaded: {file_type}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allowed_file_types'] = "PDF, DOC, or DOCX"
        return context
