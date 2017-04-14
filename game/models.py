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
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=150)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(110)])
    city = models.CharField(max_length=120)


class Question(models.Model):
    level = models.IntegerField()
    seq = models.IntegerField()
    text = models.CharField(max_length=360)
    desc = models.CharField()
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
    is_idk = models.BooleanField(default=False)
    is_correct = models.BooleanField(default=False)


class Hospital(models.Model):
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    position = GeopositionField()
    ratingHygiene = models.FloatField()
    ratingStaff = models.FloatField()
    ratingFacilities = models.FloatField()
    reviewLink = models.URLField()



