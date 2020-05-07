from django.db import models

class Data(models.Model):
    category = models.CharField(max_length = 10, 
        choices = [('A', 'A'), ('B', 'B'), ('C', 'C')])
    quantity = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now=True)