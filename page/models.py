from django.db import models

class conference(models.Model):
    name = models.CharField(max_length=100, default="")
    startdate = models.CharField(max_length=20, default="")
    level = models.CharField(max_length=10, default="")
    deadline = models.CharField(max_length=20, default="")
    location = models.CharField(max_length=20, default="")
    url = models.CharField(max_length=200, default="")
    filename = models.CharField(max_length=150, default="")
    notifytime = models.CharField(max_length=20, default="")

class paper(models.Model):
    author = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=100, default="")
    conferencename = models.CharField(max_length=100, default="")
    publishdate = models.CharField(max_length=100, default="")
    filename = models.CharField(max_length=150, default="")
    level = models.CharField(max_length=10, default="")


