from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']
    list_filter = ['published_date', 'tag']
    list_per_page = 100
    ordering = ['title']
    search_fields = ['title__icontains', 'author__full_name']
    prepopulated_fields = {
        'slug': ['title']
    }


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'created_at']
    list_filter = ['user__role' ,'created_at']
    list_per_page = 100
    ordering = ['user__first_name', 'user__last_name']
    search_fields = ['user__first_name__icontains', 'user__last_name__icontains', 'user__username__istartswith']


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_per_page = 100
    ordering = ['full_name']
    search_fields = ['full_name__icontains']


@admin.register(models.Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'borrowed_date', 'due_date', 'return_date', 'status']
    list_editable = ['status']
    list_filter = ['borrowed_date', 'due_date', 'return_date', 'status']
    list_per_page = 50
    ordering = ['-borrowed_date']
    search_fields = ['book__title__icontains', 'author__full_name__icontains']


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['tag']
    list_per_page = 20
    ordering = ['tag']
    search_fields = ['tag__icontains']
    prepopulated_fields = {
        'slug':['tag']
    }


