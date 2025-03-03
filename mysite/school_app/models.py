from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    STATUS_GENDER = (
        ('man', 'Man'),
        ('woman', 'Woman')
    )
    TYPE_CHOICES = (
        ('admin', 'admin'),
        ('student', 'student')
    )
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, default='admin')
    status = models.CharField(max_length=10, choices=STATUS_GENDER, default='woman')
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class It(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()


class Articles(models.Model):
    image = models.ImageField(upload_to='article_image')
    title = models.CharField(max_length=100)
    description = models.TextField()


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)
    certificate = models.URLField()


class AboutUsImage(models.Model):
    image = models.ImageField(null=True, blank=True)
    about_us = models.ForeignKey(AboutUs, related_name='images', on_delete=models.CASCADE)


class Certificate(models.Model):
    description = models.TextField()
    certificate = models.ImageField(upload_to='certificate_image')
    about_us = models.ForeignKey(AboutUs, related_name='about_us', on_delete=models.CASCADE)


class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    access = models.CharField(max_length=100)


class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.CharField(max_length=100)
    description = models.TextField()
    course = models.ForeignKey(Courses, related_name='question_course', on_delete=models.CASCADE)


class MasterClass(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Rating(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='rating_image')
    about_us = models.ForeignKey(AboutUs, related_name='rating_about', on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Courses, related_name='rating_course', on_delete=models.CASCADE)
    master_class = models.ForeignKey(MasterClass, related_name='rating_master', on_delete=models.CASCADE)


class AboutCourses(models.Model):
    course = models.ForeignKey(Courses, related_name='about_courses', on_delete=models.CASCADE)
    description = models.TextField()


class Paket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    TIME_CHOICES = (
        ('Ежемесячно', 'Ежемесячно'),
        ('Ежегодно', 'Ежегодно')
    )
    choices = models.CharField(max_length=100, choices=TIME_CHOICES, default='Ежегодно')
    STATUS_CHOICES = (
        ('Все статьи', 'Все статьи'),
        ('Все мастер классы', 'Все мастер классы'),
        ('6 новых статей каждый месяц', '6 новых статей каждый месяц'),
        ('Доступ к курсу “DevOps - инженер”', 'Доступ к курсу “DevOps - инженер”')
    )
    status = MultiSelectField(choices=STATUS_CHOICES)