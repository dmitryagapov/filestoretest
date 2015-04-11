from django.db import models
from time import time
import random
# Create your models here.


def file_name(instance, filename):
    return '%s%s' % (str(random.randint(100000, 999999)), filename)


class File(models.Model):
    class Meta():
        db_table = 'file'
    content = models.FileField(upload_to=file_name)
    file_links = models.IntegerField(default=0)
