from django.conf import settings
from django.db import models
# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=120)


class Choice(models.Model):
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=120)

    def __str__(self):
        return(self.choice_text)

class Log(models.Model):
    response = models.ForeignKey(Choice, on_delete=models.CASCADE)
    date = models.DateField('date')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

