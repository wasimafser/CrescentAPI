from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Subject)
admin.site.register(models.Branch)
admin.site.register(models.Department)
admin.site.register(models.Designation)
admin.site.register(models.Profile)