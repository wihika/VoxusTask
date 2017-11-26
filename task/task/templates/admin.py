from django.contrib import admin

# Register your models here.
# from .models import User, Task
from .models import Task
# from .forms import UserSignUp, TaskCreate
from .forms import TaskCreate

# class UserSignUpAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'password']
#     form = UserSignUp
#
# admin.site.register(User, UserSignUpAdmin)

class TaskCreateAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'owner', 'collaborator1', 'collaborator2', 'collaborator3', 'state']
    form = TaskCreate

admin.site.register(Task, TaskCreateAdmin)
