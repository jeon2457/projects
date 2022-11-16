from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']   # 검색기능 추가!


admin.site.register(Question, QuestionAdmin)
