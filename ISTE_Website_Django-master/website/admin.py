from django.contrib import admin
from .models import Board,Feedback,Category,Event,Event_Date, Developer

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    ordering=['pk']
    list_display=['pk','name','position']
    list_display_links=['pk','name']
    #list_display_links=['pk','name']
    search_fields=['name','position']
    
    
class DeveloperAdmin(admin.ModelAdmin):
    ordering=['pk']
    list_display=['pk','name']
    list_display_links=['pk','name']
    #list_display_links=['pk','name']
    search_fields=['name',]
    
    
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['name','email','message']
    search_fields=['name','email']
    ordering=['pk']
    readonly_fields=['name','email','phone','rating','message']


def mark_completed(modeladmin,request,queryset):
    queryset.update(is_completed=True)
    modeladmin.message_user(request,"Selected Events were marked as completed Successfully")

def mark_not_completed(modeladmin,request,queryset):
    queryset.update(is_completed=False)
    modeladmin.message_user(request,"Selected Events were marked as not completed Successfully")

mark_completed.short_description="Mark as Completed"

class DateInline(admin.StackedInline):
    model=Event_Date

class EventAdmin(admin.ModelAdmin):
    list_display=['name','category_name','is_completed']
    search_fields=['name','category__name']
    ordering=['category','is_completed']
    actions=[mark_completed,mark_not_completed]
    inlines=[DateInline,]
    
    def category_name(self,obj):
        return obj.category.name




admin.site.register(Category)
admin.site.register(Event,EventAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Event_Date)