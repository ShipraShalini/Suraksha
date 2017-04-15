# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subject, Answer, Hospital, User, Level, Question
# Register your models here.

admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(Hospital)
admin.site.register(User)
admin.site.register(Level)
admin.site.register(Question)
