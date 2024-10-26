from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Borrow)
admin.site.register(models.Author)
admin.site.register(models.Tag)


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ['title']
    }