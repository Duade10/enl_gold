from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(widget=forms.TextInput(attrs={"type": "date"}))

    class Meta:
        model = Application
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
