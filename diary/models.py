from django.db import models
from django.utils.six import python_2_unicode_compatible

class Diary(models.Model):
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text