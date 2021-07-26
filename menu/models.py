from django.db import models


class DB(models.Model):
    question = models.TextField()
    answer = models.BooleanField()
