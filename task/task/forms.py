from django import forms

from .models import Task
from .models import Uploads

from .models import IntegerRangeField


class TaskCreate(forms.ModelForm):
    owner = forms.CharField(label='Owner ', required=False, widget=forms.HiddenInput())
    title = forms.CharField(label='Title ')
    description = forms.CharField(label='Description ')
    priority = IntegerRangeField()

    id = forms.IntegerField(required=False, widget=forms.HiddenInput())
    #attached = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Task
        fields = ['title', 'description', 'owner', 'priority']

class UploadCreate(forms.ModelForm):
    attached = forms.FileField(label='Attachment ', required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = Uploads
        fields = ['attached']
