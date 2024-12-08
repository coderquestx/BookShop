from django.contrib import admin
from .models import Category, Course

admin.site.site_header = "BookShop"
admin.site.site_title = "My Books"
admin.site.index_title = "BookShop"

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category')

class CoursesInline(admin.TabularInline):
    model = Course
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
        'fields': ['created_at'], 
        'fields': ['collapse'],
        }),
    ]
    inlines = [CoursesInline]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
