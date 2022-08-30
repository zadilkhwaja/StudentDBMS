from django.db import models

class StudentData(models.Model):
    StudentName = models.CharField(max_length=100)
    CollegeName = models.CharField(max_length=100)
    RollNo = models.IntegerField(primary_key=True)
    Language = models.CharField(max_length=100)

    objects = models.Manager()
