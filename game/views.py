# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic import FormView

from game.forms import UserForm


class User(FormView):
    template_name = 'notification_form.html'
    form_class = UserForm

    def form_valid(self, form):
        job_id = form.schedule_notification()
        return render_to_response("success.html", context={"job_id_scheduled": job_id})
    pass





