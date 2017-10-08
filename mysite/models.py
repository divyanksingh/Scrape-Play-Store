from django.db import models

# Create your models here.

# App ID, app name, developer name, developer email, icon url

class Result(models.Model):
    app_id = models.CharField(max_length=200, unique=True)
    app_name = models.CharField(max_length = 200)
    developer_name = models.CharField(max_length = 200)
    developer_email = models.CharField(max_length = 200)
    icon_url = models.CharField(max_length = 200)


class Search(models.Model):
    keyword = models.CharField(max_length=200, unique=True)
    results = models.ManyToManyField(Result)
