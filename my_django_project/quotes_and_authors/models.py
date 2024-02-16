from django.db import models

# Create your models here.
class Authors(models.Model):
    fullname = models.CharField()
    born_date = models.DateField()
    born_location = models.CharField()
    description = models.TextField(null=True)

class Tag(models.Model):
    name = models.CharField()

class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Authors, on_delete=models.PROTECT)
    quote = models.TextField()
