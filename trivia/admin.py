from django.contrib import admin

# Register your models here.
from .models import questions, answers
admin.site.register(questions)
admin.site.register(answers)
