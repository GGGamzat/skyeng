from django.contrib import admin
from .models import CustomUser, Profile, File

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(File)
