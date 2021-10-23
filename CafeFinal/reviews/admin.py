from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('title', 'updated')
    ordering = ('title',)
    search_fields = ('title',)

admin.site.register(Review, ReviewAdmin)