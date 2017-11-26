from __future__ import unicode_literals

from django.db import models
from django import forms


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(null=False, blank=False, max_length=50)
    description = models.CharField(null=False, blank=False, max_length=50)
    owner = models.CharField(null=False, blank=False, max_length=50)
    priority = IntegerRangeField(null=False, min_value=1, max_value=5)
    state = models.BooleanField(null=False, default=False)
    updated_by = models.CharField(null=True, default=None, blank=False, max_length=50)

    def getOwner(self):
        return self.owner

    def getUploads(self):
        return Uploads.objects.filter(uploaded_by_id=self.id)

class Uploads(models.Model):
    uploaded_by_id = models.IntegerField(null=False)
    attached = models.FileField(null=False, upload_to='uploads/', max_length=100)
