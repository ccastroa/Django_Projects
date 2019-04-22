from django import forms
from stars.models import Star
from django.core.files.uploadedfile import InMemoryUploadedFile
from stars.humanize import naturalsize

class CreateForm(forms.ModelForm):

    class Meta:
        model = Star
        fields = ['name', 'distance', 'diameter']  # Picture is manual

    def save(self, commit=True) :
        instance = super(CreateForm, self).save(commit=False)

        if commit:
            instance.save()

        return instance

class CommentForm(forms.Form):
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)
