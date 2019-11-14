from django.db import models
import datetime

class Review(models.Model):
    RATING_CHOICES = {
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    }

    date_visited = models.DateField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATING_CHOICES)

    #Interface between Model and Database
    objects = models.Manager()
   
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name
