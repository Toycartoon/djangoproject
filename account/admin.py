from django.contrib import admin
from account.models import Photo, Data_Model


class PhotoInline(admin.TabularInline):
    model = Photo

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(Data_Model, PostAdmin)
