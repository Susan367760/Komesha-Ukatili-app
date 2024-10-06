from django.db import models

class Report(models.Model):
    description = models.TextField()
    media_file = models.FileField(upload_to='uploads/')
    timestamp = models.DateTimeField(auto_now_add=True)

