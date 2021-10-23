from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') 
    # Columnas que se van a mostrar
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title','author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        res  = ""
        for c in obj.categories.all().order_by("name"):
            res += c.name + ", "
        res = res[:len(res)-2]
        return res;

    post_categories.short_description = "Categorías"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)