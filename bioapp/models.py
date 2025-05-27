from django.db import models

class Bio(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    profession = models.CharField(max_length=100)
    short_bio = models.TextField()
    hobbies = models.TextField()

    def __str__(self):
        return self.full_name