from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.CustomUser)
admin.site.register(models.Meter)
admin.site.register(models.Transaction)
admin.site.register(models.Token)
admin.site.register(models.Account)
