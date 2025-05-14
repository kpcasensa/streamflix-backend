from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField(upload_to='videos/')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title