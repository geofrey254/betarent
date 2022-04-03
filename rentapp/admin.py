from django.contrib import admin
from .models import List, Category    
# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display=('title','status','created_on', 'house_type')
    list_filter=("status","house_type","created_on","categories")
    search_fields=['title','body','blog_type']
    prepopulated_fields={'slug':('title',)}
    
 
    class Meta:
       model = List
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}    
    
admin.site.register(List,ListAdmin)
admin.site.register(Category, CategoryAdmin)
