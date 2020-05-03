from django.db import models

class Data(models.Model):
    title = models.CharField(max_length = 100)
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)