from django.contrib import admin
from .models import Category, Guide, Game

admin.site.register(Category)
admin.site.register(Guide)
admin.site.register(Game)