from django.shortcuts import render, redirect
from django.views import View
from . import forms


class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = forms.ContactMessageForm()
        return render(request, "contacts/contact.html", {"form":form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = forms.ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:contact")
        return render(request, "contacts/contact.html")
