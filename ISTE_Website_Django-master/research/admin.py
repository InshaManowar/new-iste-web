from django.contrib import admin
from .models import Department,Professor,Project,Category
# Register your models here.
admin.site.register(Department)
#admin.site.register(Project)


class ProjectInline(admin.StackedInline):
    model=Project
    filter_horizontal=['categories']

class ProfessorAdmin(admin.ModelAdmin):
    inlines=[ProjectInline,]
    ordering=['department']
    list_display=['name','department','position']
    search_fields=['name','department__name','project__name','position']

admin.site.register(Professor,ProfessorAdmin)
admin.site.register(Category)
#admin.site.register(Project,ProjectAdmin)