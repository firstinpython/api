from django.db import models


# Create your models here.

class Videos(models.Model):
    name = models.CharField(max_length=20)
    video_file = models.FileField(upload_to="video")

    def __str__(self):
        return f"{self.name}"