from django.contrib import admin
from .models import DailyTodo, Task, Project

# Register your models here.
all_models = {DailyTodo, Task, Project}

for model in all_models:
    admin.site.register(model)