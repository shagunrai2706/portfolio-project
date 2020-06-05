from django.db import models

class Blog(models.Model):
    image=models.ImageField(upload_to='image/')
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    body=models.TextField(max_length=200)
