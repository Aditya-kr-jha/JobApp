from django.contrib import admin

from app.models import Author, Location, Skills, jobPost

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "salary", "date")
    list_filter = ('date', 'salary')
    search_fields = ('title',)
    fieldsets = (("basic Information",
                  {'fields': ('title', 'description')}),
                 ('more Information',
                  {'classes': ('collapse',), 'fields': ('salary', 'slug')})
                 )


admin.site.register(jobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
