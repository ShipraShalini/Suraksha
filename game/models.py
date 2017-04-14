# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.db import models

from geoposition.fields import GeopositionField


class User(models.Model):
    GENDER_CHOICES = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
        ('Unspecified', "Don't want to disclose")
    )
    username = models.CharField(max_length=120, null=True)
    password = models.CharField(max_length=150, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(110)])
    city = models.CharField(max_length=120)


class Subject(models.Model):
    name = models.CharField(max_length=120,unique=True)
    desc = models.TextField()

class Question(models.Model):
    subject = models.ForeignKey(Subject, related_name='subject')
    level = models.IntegerField()
    seq = models.IntegerField()
    text = models.CharField(max_length=360)
    desc = models.TextField()
    correctAnswer = models.CharField(max_length=120)
    wrongAnswer1 = models.CharField(max_length=120)
    wrongAnswer2 = models.CharField(max_length=120)
    wrongAnswer3 = models.CharField(max_length=120)
    correctAnswerUrl = models.URLField()
    wrongAnswer1Url = models.URLField()
    wrongAnswer2Url = models.URLField()
    wrongAnswer3Url = models.URLField()


class Answer(models.Model):
    CHOICES = (
        (0, "correctAnswer" ),
        (1, "wrongAnswer1"),
        (2, 'wrongAnswer2'),
        (3, 'wrongAnswer3'),
    )
    user = models.ForeignKey(User, related_name='user')
    question = models.ForeignKey(Question, related_name='question')
    answer = models.IntegerField(choices=CHOICES)


class Hospital(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    ratingHygiene = models.FloatField()
    ratingStaff = models.FloatField()
    ratingFacilities = models.FloatField()
    reviewLink = models.URLField()



