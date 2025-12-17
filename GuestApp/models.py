from django.db import models

# Create your models here.
class Tbl_login(models.Model):
    loginid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    role = models.CharField(max_length=25)