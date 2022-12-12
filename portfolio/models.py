
from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    Body = models.TextField()
    image = models.ImageField(upload_to='images/')


