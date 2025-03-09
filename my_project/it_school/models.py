from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(default=0, validators=[MinValueValidator(12), MaxValueValidator(70)],
                                           null=True, blank=True)
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

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'


class It(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Articles(models.Model):
    image = models.ImageField(upload_to='article_image')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    it = models.ForeignKey(It, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class AboutUsImage(models.Model):
    image = models.ImageField(null=True, blank=True)
    about_us = models.ForeignKey(AboutUs, related_name='images', on_delete=models.CASCADE)


class Certificate(models.Model):
    name = models.CharField(max_length=24, default=0)
    description = models.TextField()
    certificate = models.ImageField(upload_to='certificate_image')
    about_us = models.ForeignKey(AboutUs, related_name='certificate', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AboutSchool(models.Model):
    about_school = models.CharField(max_length=200)

    def __str__(self):
        return self.about_school


class AboutSchoolSecond(models.Model):
    title = models.CharField(max_length=50, default=0)
    school_description = models.TextField(default=0)
    about = models.ForeignKey(AboutSchool, on_delete=models.CASCADE, related_name='school')

    def __str__(self):
        return self.title


class Courses(models.Model):
    name = models.CharField(max_length=24, default=0)
    course_name = models.CharField(max_length=100)
    description = models.TextField()
    access = models.CharField(max_length=100, default=0, null=True,blank=True)
    included  = models.CharField(max_length=24, default=0)
    about_school = models.ForeignKey(AboutSchool, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.course_name


class MasterClass(models.Model):
    name = models.CharField(max_length=24, default=0)
    master_name = models.CharField(max_length=100, default=0)
    description = models.TextField(default=0)
    access = models.CharField(max_length=24, default=0, null=True, blank=True)
    included  = models.CharField(max_length=24, default=0)
    school = models.ForeignKey(AboutSchool, on_delete=models.CASCADE, related_name='master_class')

    def __str__(self):
        return self.master_name


class Paket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    about_school = models.ForeignKey(AboutSchool, on_delete=models.CASCADE, related_name='packets')

    def __str__(self):
        return self.title


class PaketSecond(models.Model):
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
    paket = models.ForeignKey(Paket, on_delete=models.CASCADE, related_name='paket')

    def __str__(self):
        return self.time


class Question(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Courses, related_name='question_course', on_delete=models.CASCADE, null= True, blank=True)
    master_class = models.ForeignKey(MasterClass, related_name='question_master', on_delete=models.CASCADE, null=True, blank=True)
    it = models.ForeignKey(It, on_delete=models.CASCADE, null=True, blank=True, related_name='question_it')
    paket = models.ForeignKey(Paket, on_delete=models.CASCADE, null=True, blank=True, related_name='question_paket')

    def __str__(self):
        return self.title


class QuestionSecond(models.Model):
    question = models.CharField(max_length=100)
    description = models.TextField()
    questions = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='all_question', null=True, blank=True)

    def __str__(self):
        return self.question


class Rating(models.Model):
    title = models.CharField(max_length=100)
    about_us = models.ForeignKey(AboutUs, related_name='rating_about', on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Courses, related_name='rating_course', on_delete=models.CASCADE, null=True, blank=True)
    master_class = models.ForeignKey(MasterClass, related_name='rating_master', on_delete=models.CASCADE, null=True, blank=True)
    about_school = models.ForeignKey(AboutSchool, on_delete=models.CASCADE, related_name='school_rating', null=True, blank=True)

    def __str__(self):
        return self.title


class RatingUser(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='rating_image')
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, related_name='rating_user')

    def __str__(self):
        return self.name


class AboutCourses(models.Model):
    course = models.ForeignKey(Courses, related_name='about_courses', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=24, default=0)
    about = models.TextField(default=0)
    description = models.TextField(null=True, blank=True)
    master_class = models.ForeignKey(MasterClass, on_delete=models.CASCADE, related_name='about_master_class', null=True, blank=True)

    def __str__(self):
        return self.title


class AboutSecond(models.Model):
    title = models.CharField(max_length=64, default=0)
    description = models.TextField(default=0)
    about_course  = models.ForeignKey(AboutCourses, on_delete=models.CASCADE, related_name='about_second')

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    contact_number = PhoneNumberField()
    email = models.CharField(max_length=64)
    address = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.contact_number}'


class SocialNetwork(models.Model):
    network_name = models.CharField(max_length=64)
    network_url = models.URLField()
    contact = models.ForeignKey(ContactInfo, on_delete=models.CASCADE, related_name='contact')