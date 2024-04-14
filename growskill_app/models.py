from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_instructor = models.BooleanField(default=False)
    speciality = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=100)
    zoom_link = models.URLField()
    is_completed = models.BooleanField(default=False)
    recording_link = models.URLField()
    
    def __str__(self):
        return self.topic


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Certificate(models.Model):
    enrollment = models.OneToOneField(Enrollment, on_delete=models.CASCADE)
    is_generated = models.BooleanField(default=False)
    download_link = models.URLField()

    def __str__(self):
        return self.enrollment.user.username
