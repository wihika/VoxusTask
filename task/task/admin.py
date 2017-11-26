from django.contrib import admin
from .models import Task
from .models import Uploads
from .forms import TaskCreate
from .forms import UploadCreate

class TaskCreateAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'owner', 'priority', 'state', 'updated_by']
    form = TaskCreate

class UploadsCreateAdmin(admin.ModelAdmin):
    list_display = ['uploaded_by_id', 'attached']
    form = UploadCreate


admin.site.register(Uploads, UploadsCreateAdmin)
admin.site.register(Task, TaskCreateAdmin)
