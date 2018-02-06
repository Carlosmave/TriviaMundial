from django.db import models
from datetime import datetime

# Create your models here.
class questions(models.Model):
    question = models.CharField(max_length=250)
    #body = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    def __str__(self):
        return self.question
    class Meta:
        verbose_name_plural = "Questions"

class answers(models.Model):
    answer = models.CharField(max_length=200)
    score = models.CharField(max_length=200)
    def __str__(self):
        return self.answer
    class Meta:
        verbose_name_plural = "Answers"
#class posts(models.Model):
#    title = models.CharField(max_length=200)
#    body = models.TextField()
#    created_at = models.DateTimeField(default=datetime.now, blank=True)
