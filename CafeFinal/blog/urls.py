from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.blog, name="blog"),
    path('category/<int:category_id>', views.category, name="category")
]