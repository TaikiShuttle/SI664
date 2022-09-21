from django.db import models

# Create your models here.
class Eva_record(models.Model):
    course_id = models.CharField(max_length = 10)
    course_name = models.CharField(max_length = 200)
    instructor = models.CharField(max_length = 200)
    enroll_semester = models.CharField(max_length = 30)
    credit = models.FloatField()
    rate = models.FloatField()
    comment = models.CharField(max_length = 1024)

