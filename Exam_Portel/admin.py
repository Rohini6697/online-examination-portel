from django.contrib import admin

from .models import Questions, Result

# Register your models here.
admin.site.register(Questions),
admin.site.register(Result),