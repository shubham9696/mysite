# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import faculty
from .models import student
from .models import course
from .models import attendance
from .models import login
admin.site.register(faculty)
admin.site.register(student)
admin.site.register(course)
admin.site.register(attendance)
admin.site.register(login)

# Register your models here.
