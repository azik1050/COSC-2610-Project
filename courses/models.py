from django.utils import timezone
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    SENIORITIES = [
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior')
    ]
    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, default='', null=True, blank=True)
    lastname = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=100, choices=GENDERS, blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=100)
    seniority = models.CharField(max_length=25, choices=SENIORITIES)
    start_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.firstname


class Timetable(models.Model):
    DAYS = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ]
    PERIODS = [
        ('9.00 - 11.20', '9.00 - 11.20'),
        ('11.30 - 13.50', '11.30 - 13.50'),
        ('14.00 - 16.20', '14.00 - 16.20'),
        ('16.30 - 18.50', '16.30 - 18.50'),
        ('19.00 - 21.20', '19.00 - 21.20')
    ]
    LEVELS = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day = models.CharField(max_length=25, choices=DAYS)
    time = models.CharField(max_length=25, choices=PERIODS)
    room = models.CharField(max_length=100, null=True, blank=True)
    student_level = models.CharField(max_length=1, choices=LEVELS, default='1')

    def __str__(self):
        return f'{self.pk}'
