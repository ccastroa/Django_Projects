from django import forms
from pics.models import Pic
from django.core.files.uploadedfile import InMemoryUploadedFile
from pics.humanize import naturalsize
from django.core.exceptions import ValidationError
from django.core import validators


# https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/2.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    ad = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'ad'
    comment = forms.CharField(required=True, max_length=500, min_length=3, strip=True)


    class Meta:
        model = Ad
        fields = ['title', 'text', 'ad', 'comment']  # Picture is manual

    # Validate the size of the picture
    def clean(self) :
        cleaned_data = super().clean()
        ad = cleaned_data.get('ad')
        if ad is None : return
        if len(ad) > self.max_upload_limit:
            self.add_error('ad', "File must be < "+self.max_upload_limit_text+" bytes")
            
    # Convert uploaded File object to a picture
    def save(self, commit=True) :
        instance = super(CreateForm, self).save(commit=False)

        # We only need to adjust picture if it is a freshly uploaded file
        f = instance.ad   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read();
            instance.content_type = f.content_type
            instance.ad = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance
