from django.contrib import admin

# Register your models here.
from .models import Track, Choice, Log

admin.site.register(Track)
admin.site.register(Choice)
admin.site.register(Log)