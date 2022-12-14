from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.CharField(max_length = 10)
    course_name = models.CharField(max_length = 200)
    instructor = models.CharField(max_length = 200)
    last_offered = models.CharField(max_length = 30)
    credit = models.FloatField()
    category = models.CharField(max_length = 200)
    avg_rating = models.FloatField()