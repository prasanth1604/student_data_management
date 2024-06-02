from django.db import models
from django.db.models import UniqueConstraint


class Student(models.Model):
    roll_no = models.CharField(max_length=8, unique=False)
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, default='NA')
    parent = models.CharField(max_length=30, default='NA')
    address = models.CharField(max_length=50, default='NA')
    subjectCode = models.CharField(max_length=20, default='NA', unique=False)
    assignment1 = models.IntegerField(default=0)
    assignment2 = models.IntegerField(default=0)
    total = models.IntegerField(default=0)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['roll_no', 'subjectCode'], name='unique_roll_no_subject_code')
        ]


    def __str__(self):
        return self.subjectCode + " " + self.roll_no


class Faculty(models.Model):
    fId = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=30)
    subjectName = models.CharField(max_length=50)
    subjectCode = models.CharField(max_length=20)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name






