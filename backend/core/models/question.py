from django.db import models
from datetime import datetime
from django.conf import settings
from django.db.models import Q

class ActiveQuestionManager(models.Manager):
    def get_qeryset(self):
        return super().get_queryset().filter(Q(start_date_lte=datetime.now(), end_adte_gte= datetime.now()))
    
class ClosedQuestionManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(end_date_lte=datetime.now(),)
    
class Question(models.Model):
    text = models.CharField(max_length=200)
    creation_date = models.DateTimeField(default=datetime.now)
    start_date = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=datetime.now)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = models.Manager()
    active = ActiveQuestionManager()
    closed = ClosedQuestionManager()
    
    def __str__(self):
        return self.text