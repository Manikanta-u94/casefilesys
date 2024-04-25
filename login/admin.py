from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from login.models import LoginPageImage, LogoPolicy
from login import models


class LoginImageAdmin(admin.ModelAdmin):
    model = LoginPageImage
    list_display = ['name', 'is_active']



class LogoPolicyAdmin(admin.ModelAdmin):
    model = LogoPolicy
    list_display = ['policy',]


admin.site.register(LoginPageImage, LoginImageAdmin)
admin.site.register(LogoPolicy, LogoPolicyAdmin)

