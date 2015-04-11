from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class MyUser(models.Model):
    class Meta():
        db_table = 'my_user'
    user = models.OneToOneField(User)
    file_number = models.IntegerField(default=0)


class UserFiles(models.Model):
    class Meta():
        db_table = 'name_hash'
    file_user = models.ForeignKey(MyUser) #TODO:Must be changed to User
    file_name = models.CharField(max_length=200)
    file_hash = models.CharField(max_length=200)
