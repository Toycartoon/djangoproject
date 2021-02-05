from django.contrib import admin
from account.models import Data_Model


class auth(admin.ModelAdmin):
    list_display = ['id', 'name', 'text']

admin.site.register(Data_Model, auth)