from django.contrib import admin
from .models import Recipe
# Register your models here.

# @admin.register(Recipe)        admin.site.register(Recipe, RecipeAdmin) narakhni vaya yo line (decoretor) rakh ne hunxa
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id','name','ingredients','time']
    list_filter = ['time']
    search_fields = ['name','ingredients','time']
    list_per_page = 10
    
    
admin.site.register(Recipe, RecipeAdmin)