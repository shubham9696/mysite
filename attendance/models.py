# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=200)
    student_DOB = models.DateTimeField()
    student_prog = models.CharField(max_length=200)
    student_branch = models.CharField(max_length=200)
    student_semester = models.IntegerField(default=0)
    student_year = models.IntegerField(default=0)
    student_id = models.IntegerField(default=0)
    def __str__(self):
        return '%s %s %s' % (self.student_name, self.student_prog,self.student_branch)


class course(models.Model):
    course_id = models.IntegerField(default=0)
    course_name = models.CharField(max_length=200)
    course_sem = models.IntegerField(default=0)
    course_year = models.IntegerField(default=0)
    course_deptid = models.IntegerField(default=0)
    course_facid = models.IntegerField(default=0)
    course_prog = models.CharField(max_length=200)
    def __str__(self):
        return '%s %s' % (self.course_name, self.course_prog)

class faculty(models.Model):
    faculty_id = models.IntegerField(default=0)
    faculty_name = models.CharField(max_length=200)
    faculty_cont = models.IntegerField(default=0)
    faculty_joindate = models.DateTimeField(default=0)
    faculty_deptid = models.IntegerField(default=0)
    faculty_desig = models.CharField(max_length=200)
    def __str__(self):
        return '%s %s' % (self.faculty_name, self.faculty_desig)

class attendance(models.Model):
    total = models.IntegerField(default=0)
    total_clas = models.IntegerField(default=0)
    course_id = models.IntegerField(default=0)
    student_id = models.IntegerField(default=0)

    def __str__(self):
        return '%d %d' % (self.course_id, self.student_id)

class login(models.Model):
    login_id = models.IntegerField()
    login_pass = models.CharField(max_length=200)
    login_role = models.CharField(max_length=200)
    def __str__(self):
        return '%s %s' % (self.login_id, self.login_role)