from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Quiz, Question, Option, Result

# Register your models here.
# Add options when editing the questions on Django Admin
class OptionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [OptionInline]


admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Result)