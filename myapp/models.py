from django.db import models

class Record(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content
