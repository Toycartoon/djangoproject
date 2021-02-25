from django.contrib import admin
from account.models import Photo, Data


class PhotoInline(admin.TabularInline):
    model = Photo


class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]


admin.site.register(Data, PostAdmin)

