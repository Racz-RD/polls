from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# Default form representation
# admin.site.register(Question)

""" class QuestionAdmin(admin.ModelAdmin):
    fields=['pub_date', 'question_text'] """

# It takes a lot of screen space to display all the fields for entering related Choice objects.  
""" class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3 """

# Django offers a tabular way of displaying inline related objects. 
# With that TabularInline (instead of StackedInline), 
# the related objects are displayed in a more compact, table-based format. 
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields':['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']

# Create a model admin class, then pass it as the second argument to admin.site.register() – 
# any time you need to change the admin options for a model.
# This particular change above makes the “Publication date” come before the “Question” field:   
admin.site.register(Question, QuestionAdmin)

