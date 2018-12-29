from django.db import models

# Create your models here.


class Question(models.Model):
    text = models.CharField(max_length=256, null=False)
    published = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    text = models.CharField(max_length=128)
    votes = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.text
