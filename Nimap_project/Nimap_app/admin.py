from django.contrib import admin
from .models import ClientModel,ProjectModel,projectUserModel
# Register your models here.

admin.site.register(ClientModel)
admin.site.register(ProjectModel)
admin.site.register(projectUserModel)

