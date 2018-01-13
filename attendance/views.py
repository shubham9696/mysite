# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from .models import attendance,student,faculty

def index(request):
    attendance_list = attendance.objects.order_by('-course_id')
    template = loader.get_template('attendance/index.html')
    context = {
        'attendance': attendance_list,
    }
    return HttpResponse(template.render(context, request))

