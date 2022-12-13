
from django.db import models


class Portfolio(models.Model):
    caption = models.CharField(max_length=200)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.caption

