from django.contrib import admin

from .models import CustomUser, Department, Category

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_by', 'create_date', 'update_by', 'update_date')
    search_fields = ('name', )
    ordering = ('update_date',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_by', 'create_date', 'update_by', 'update_date')
    search_fields = ('name', )
    ordering = ('update_date', )


# Register your models here.
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Category, CategoryAdmin)
