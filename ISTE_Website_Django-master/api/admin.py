from django.contrib import admin
from .models import Question,Mentor,Answer,Category

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display=['mentor_name','question','category','expected_answer']
    search_fields=['mentor__name','question']
    ordering=['mentor__name']

    def mentor_name(self,obj):
        return obj.mentor.name



class MentorAdmin(admin.ModelAdmin):
    list_display=['name','company','year']


class AnswerAdmin(admin.ModelAdmin):
    readonly_fields=['user','question','answer']
    search_fields=['user__first_name']
    list_display=['user_name','question_brief','points']
    ordering=['points','question']
    
    def user_name(self,obj):
        return obj.user.first_name+" "+obj.user.last_name
    def question_brief(self,obj):
        return obj.question.question[0:50]




admin.site.register(Question,QuestionAdmin)
admin.site.register(Mentor,MentorAdmin)
admin.site.register(Answer,AnswerAdmin)
admin.site.register(Category)